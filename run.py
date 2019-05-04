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

def prendreRDV():
    pid = '222'
    nom_du_patient = 'toto'
    nom_du_medecin = 'titi'
    id = '123'
    date = '01/01/2019'
    acte = 'acte abc'

    message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\n'
    message = message + 'PID|||' + pid + '|||' + nom_du_patient + '|196203520||||' + nom_du_medecin + '||||||||| 67 - A4335 ^ OH ^ 20030520\n'
    message = message + 'SCH|' + id + '||||||||20|MIN||||||JOHN|||||||||ARRIVED|\n'
    message = message + 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||' + date +'||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\n'
    message = message + 'OBX|1|SN| ' + acte + '||^182|mg/dl|70_105|H|||F\n'

    api_url = '%s/transactions' % (host)

    response = requests.post(
        url=api_url, 
        data=message,
        headers={'Content-Type': 'text/plain'}
    )

    print(response.text)


#listPatients()
#recherchePatient()
#rendezVousPatient()
#listeDesResultatsPatient()
prendreRDV()