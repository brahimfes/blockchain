import cloudinary.uploader
from urllib.request import urlopen
from urllib.error import URLError


cloudinary.config( 
  cloud_name = "dqp6vrabj", 
  api_key = "317375665231954", 
  api_secret = "MATdVdcrC1ddK0ZGaoG-Vz6NjuU" 
)

def upload():
  result = cloudinary.uploader.upload("resources/blockchain.json", 
    public_id = "blockchain",
    overwrite = 'true',
    resource_type = "raw")
  print(result['url'])


def download():
  try:
      response = urlopen('http://res.cloudinary.com/dqp6vrabj/raw/upload/v1557190840/blockchain.json')
      data = response.read()
      print(data)
  except URLError as e:
      print("erreur")

download()