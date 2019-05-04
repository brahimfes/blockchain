import cloudinary.uploader
from urllib.request import urlopen
from urllib.error import URLError


cloudinary.config( 
  cloud_name = "dqp6vrabj", 
  api_key = "317375665231954", 
  api_secret = "MATdVdcrC1ddK0ZGaoG-Vz6NjuU" 
)


result = cloudinary.uploader.upload("resources/data.json", 
  public_id = "blockchain",
  overwrite = 'true',
  resource_type = "raw")

print(result['url'])
try:
    response = urlopen('http://res.cloudinary.com/dqp6vrabj/raw/upload/v1557140356/blockchain.json')
    data = response.read()
except URLError as e:
    print("erreur")