import requests

host = "http://localhost:8000"
#host = "https://middleware-its.herokuapp.com"

def listeDesPatients():
    url = "%s/patients" % (host)
    response = requests.request("GET", url)
    print(response.text)

def recherchePatient():
    pid = "555444444"
    url = "%s/patients/%s" % (host, pid)
    response = requests.request("GET", url)
    print(response.text)

def listeDesRendezVousPatient():
    pid = "555444444"
    url = "%s/patients/%s/rendezvous" % (host, pid)
    response = requests.request("GET", url)
    print(response.text)

def listeDesResultatsPatient():
    pid = "555444444"
    url = "%s/patients/%s/resultats" % (host, pid)
    response = requests.request("GET", url)
    print(response.text)

#listPatients()
#recherchePatient()
#rendezVousPatient()
listeDesResultatsPatient()