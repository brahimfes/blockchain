from flask import Flask
from db import MysqlDatabase
app = Flask(__name__)

connector = MysqlDatabase(host='localhost', user='root',
                          password='', database='sih')


@app.route('/')
def main():
    return "Microservice (patient) en marche !"


@app.route('/patients', methods=['GET'])
def getPatients():
    result = connector.execute(query="SELECT * FROM patient")
    return result


@app.route('/patients/<pid>', methods=['GET'])
def getPatient(pid):
    select = "SELECT * FROM patient where pid like '%s'" % pid
    result = connector.execute(query=select)
    return result


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=2001,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
