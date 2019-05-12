from flask import Flask, Blueprint, request
from .db import MysqlDatabase
from api.auth import check_auth, authenticate, requires_auth

patient_api = Blueprint("patient_api", __name__)

#connector = MysqlDatabase(host='localhost', user='root', password='', database='sih')
db = MysqlDatabase('u615qyjzybll9lrm.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', 'znrv09cif9r6878k', 'besy5nu30n3u1hrh', 'ffl0zhvdujs4a0wc')


@patient_api.route('/patients', methods=['GET'])
def getPatients():
    result = db.execute(query="SELECT * FROM patient")
    return result


@patient_api.route('/patients/<pid>', methods=['GET'])
def getPatient(pid):
    select = "SELECT * FROM patient where pid like '%s'" % pid
    result = db.execute(query=select)
    return result

@patient_api.route('/patients/<pid>/rendezvous', methods=['GET'])
def getRendezVousPatient(pid):
    select = "SELECT * FROM rendez_vous where pid like '%s'" % pid
    result = db.execute(query=select)
    return result

@patient_api.route('/patients/<pid>/resultats', methods=['GET'])
def getResults(pid):
    select = "SELECT * FROM obx where pid like '%s'" % pid
    result = db.execute(query=select)
    return result

@patient_api.route('/patients/<pid>/reports', methods=['GET'])
def getReports(pid):
    select = "SELECT * FROM rapport where pid like '%s'" % pid
    result = db.execute(query=select)
    return result

@patient_api.route('/valises', methods=['GET'])
def getValises():
    select = "SELECT * FROM valise"
    result = db.execute(query=select)
    return result

@patient_api.route('/valises', methods=['POST'])
def ajouterValise():
    body = request.get_json()
    select = "insert into valise(checkout, date) values('%s', '%s')" % (body['checkout'], body['date'])
    result = db.insert(query=select)
    return 'OK'

@patient_api.route('/patients/<pid>/rapports', methods=['POST'])
@requires_auth
def ajouterRapport(pid):
    auth = request.authorization
    print(auth)
    body = request.get_json()
    select = "insert into rapport(contenu, pid, date, user) values('%s', '%s', '%s', '%s')" % (body['contenu'], pid, body['date'], auth.username)
    result = db.insert(query=select)
    return 'OK'

@patient_api.route('/patients/<pid>/rapports', methods=['GET'])
def listeRapports(pid):
    select = "select * from rapport where pid like '%s'" % pid
    result = db.execute(query=select)
    return result