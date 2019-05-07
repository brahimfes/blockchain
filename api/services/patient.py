from hl7parser.parser import Parser
from api.db import MysqlDatabase

#db = MysqlDatabase('localhost', 'root', '', 'sih')
db = MysqlDatabase('u615qyjzybll9lrm.chr7pe7iynqr.eu-west-1.rds.amazonaws.com', 'znrv09cif9r6878k', 'besy5nu30n3u1hrh', 'ffl0zhvdujs4a0wc')

class PatientService:

    def save(self, hl7_message):
        parser = Parser()
        parser.parse(hl7_message)
        msg_type = parser.getMessageType()

        # traiter le message selon son type
        obx = parser.obx
        pid = parser.pid
        sch = parser.sch
        aip = parser.aip

        if msg_type == 'ORU^R01':
            query = "insert into obx (set_id, value, units, references_range, result, pid) values('%s', '%s', '%s', '%s', '%s', '%s')" % (obx.set_id, obx.value, obx.units, obx.references_range, obx.result, pid.ip )
            print(query)
            db.insert(query)

            updateAppointmentQuery = "update rendez_vous set etat = 'finalise' where id = '%s'" % sch.id
            print(updateAppointmentQuery)
            return db.insert(updateAppointmentQuery)

        elif msg_type == 'ADT^A28':
            query = "insert into patient(pid, nom, prenom, date_naissance, sexe, adresse) values('%s', '%s', '%s', '%s', '%s', '%s')" % (pid.ip, pid.nom, pid.prenom, pid.date_naissance, pid.sexe, pid.adresse)
            print(query)
            db.insert(query)

        elif msg_type == 'SIU^S12':
            query = "insert into rendez_vous(pid, nom_du_medecin, dates, agenda, acte) values('%s', '%s', '%s', '%s', '%s')" % (pid.ip, aip.nom, sch.date_debut, sch.agenda, sch.acte)
            print(query)
            db.insert(query)

        else:
            print('Désolé ! votre message n\'est pas reconnu par notre API')