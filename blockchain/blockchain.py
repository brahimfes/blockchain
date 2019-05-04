import hashlib
from time import time
import json
import os.path
import datetime
import requests
from urllib.parse import urlparse
import boto3
import botocore

import cloudinary.uploader
from urllib.request import urlopen
from urllib.error import URLError

cloudinary.config( 
  cloud_name = "dqp6vrabj", 
  api_key = "317375665231954", 
  api_secret = "MATdVdcrC1ddK0ZGaoG-Vz6NjuU" 
)

class Blockchain:

    def __init__(self, config):
        self.current_transactions = []
        self.chain = []
        self.nodes = []
        
        self.bucket_name = 'its2019'
        self.key_object = 'data.json'

        self.s3 = boto3.resource(
            's3',
            aws_access_key_id='AKIAWFD52SAVQ2BZIU6Q',
            aws_secret_access_key='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',
        )

        cloudinary.config( 
            cloud_name = "dqp6vrabj", 
            api_key = "317375665231954", 
            api_secret = "MATdVdcrC1ddK0ZGaoG-Vz6NjuU" 
        )


        # Create the genesis block
        # try:
        #     obj = self.s3.Object(self.bucket_name, self.key_object)
        #     data = obj.get()['Body'].read()
        #     self.chain = json.loads(data)
        #     if len(self.chain) == 0:
        #         self.new_block(previous_hash='1', proof=100)
        # except botocore.exceptions.ClientError as e:
        #     self.new_block(previous_hash='1', proof=100)

        try:
            response = urlopen('http://res.cloudinary.com/dqp6vrabj/raw/upload/v1557140356/blockchain.json')
            data = response.read()
            self.chain = json.loads(data)
            if len(self.chain) == 0:
                self.new_block(previous_hash='1', proof=100)
        except URLError as e:
            self.new_block(previous_hash='1', proof=100)

        # load configuration
        nodes = None
        if os.path.isfile(config):
            with open(config, 'r') as f:
                nodes = f.read().splitlines()
                print("Nodes: ", nodes)

        # registrer loaded nodes
        if nodes:
            for node in nodes:
                print("register_node: ", node)
                self.register_node(node)


    def register_node(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.append(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.append(parsed_url.path)
        else:
            raise ValueError('Invalid URL')

    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            last_block_hash = self.hash(last_block)
            if block['previous_hash'] != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof'],
                                    last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'https://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        with open('resources/mydata.json', 'w') as file:
            file.write(json.dumps(self.chain))
        cloudinary.uploader.upload(
            'resources/mydata.json', 
            public_id = "blockchain",
            resource_type = "raw"
        )
        #self.s3.Bucket(self.bucket_name).put_object(Key=self.key_object, Body=json.dumps(self.chain))

        return block

    def new_transaction(self, message):
        """
        Creates a new transaction to go into the next mined Block

        :param message: message HL7
        :return: The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'message': message
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
