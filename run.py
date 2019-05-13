import requests
import datetime
from requests.auth import HTTPBasicAuth

host = "https://middleware-its.herokuapp.com"

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

def ajouterPatient():
    message = "MSH|^~\&|ITS Tablette||ITS Middleware||20160102101112||ADT^A28|ABC0000000001|P|2.4\n"
    message = message + "PID|||332222333||touati^^talal^^||19700101|M|||^101, Jean Jaures^Vitry^^^||||||||||||||||||||\n"

    api_url = '%s/transactions' % (host)

    response = requests.post(
        url=api_url, 
        data=message,
        headers={'Content-Type': 'text/plain'}
    )

    print('%s, %s' % (response.status_code, response.text))


def ajouterObservation():
    pid = '222'
    nom_du_patient = 'toto'
    nom_du_medecin = 'titi'
    id = '123'
    date = '01/01/2019'
    acte = 'acte abc'

    message = 'MSH|^~\&|ITS Tablette||ITS Middleware||200202150930||ORU^R01|CNTRL-3456|P|2.4\n'
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

def nouveauRendezVous():
    agenda = 'Prise constante'
    acte = 'ecg'
    dateRendezVous = '201411201231'
    dateFinRendezVous = '201411201232'
    nom_du_medecin = '^Jones^Stuart^James^^Dr'

    message = 'MSH|^~\&|ITS Tablette||ITS Middleware||201303080949||SIU^S12|ABC0000000001|P|2.4\n'
    message = message + 'PID|||555||Smith^John^Joe^^Mr||19700101|M|||My flat name^1, The Road^London^London^SW1A 1AA^GBR||john.smith@hotmail.com^NET~01234567890^PRN~07123456789^PRS|john.smith@company.com^NET~01234098765^WPN||||||||||||||||N|\n'
    message = message + 'SCH|ID000||||||^Prise constante^ECG||||^^^201411201231^201411201232|||||||||||||||\n'
    message = message + 'AIP|||^Jones^^James^^Dr|^Doctor\n'

    api_url = '%s/transactions' % (host)

    response = requests.post(
        url=api_url, 
        data=message,
        headers={'Content-Type': 'text/plain'}
    )
    print(response.text)    

def ajouterValise():
    api_url = '%s/valises' % (host)

    body = {
        'checkout': 'test',
        'date': str(datetime.datetime.now())
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

def login():
    api_url = '%s/users' % (host)
    response = requests.request("GET", api_url, auth=HTTPBasicAuth('Mouna', 'secret'))
    print(response.text)

def recupererUserParBiometry():
    api_url = '%s/users/biometry' % (host)
    body = {
        'biometry': '1234',
    }
    
    response = requests.post(
        url = api_url, 
        json = body,
        headers = {'Content-Type': 'application/json'}
    )

    print(response.text)

def loginByBiometry():
    api_url = '%s/users' % (host)
    response = requests.request("GET", api_url, auth=HTTPBasicAuth('rachid', 'bio:1234'))
    print(response.text)

def ajouterRapportByBiometry():
    pid = "555444451"
    api_url = '%s/patients/%s/rapports' % (host, pid)
    body = {
        'contenu': 'contenu du rapport de test',
        'date': str(datetime.datetime.now())
    }
    
    response = requests.post(
        url = api_url, 
        json = body,
        headers = {'Content-Type': 'application/json'},
        auth = HTTPBasicAuth('rachid', 'bio:1234')
    )

    print(response.text)
    
def ajouterRapport():
    pid = "555444451"
    api_url = '%s/patients/%s/rapports' % (host, pid)
    body = {
        'contenu': 'contenu du rapport de test',
        'date': str(datetime.datetime.now())
    }
    
    response = requests.post(
        url = api_url, 
        json = body,
        headers = {'Content-Type': 'application/json'},
        auth = HTTPBasicAuth('ASLAN', 'secret')
    )

    print(response.text)

def listeDesRapports():
    pid = "555444451"
    api_url = '%s/patients/%s/rapports' % (host, pid)
    response = requests.request("GET", api_url)
    print(response.text)

#listPatients()
#recherchePatient()
#rendezVousPatient()
#listeDesResultatsPatient()
#ajouterObservation()
#ajouterPatient()
#nouveauRendezVous()
#ajouterValise()
#listeDesValises()
#login()
recupererUserParBiometry()
ajouterRapportByBiometry()
#loginByBiometry()
#ajouterRapport()
#listeDesRapports()