import requests

host = "https://middleware-its.herokuapp.com"
 

def ajouterValise():
    api_url = '%s/valises' % (host)

    body = {
        'checkout': 'test',
        'date': '12/01/2019'
    }

    response = requests.post(
        url=api_url, 
        json=body,
        headers={'Content-Type': 'application/json'}
    )
    print(response.text)

def listeDesValises():
    api_url = '%s/valises' % (host)
    response = requests.request("GET", api_url)
    print(response.text)

#ajouterValise()
listeDesValises()