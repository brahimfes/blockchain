import hl7
from api.models.patient import Patient
from api.models.observation import Observation
from api.models.appointment import Appointment
from api.models.doctor import Doctor

class Parser:
    __msg = None
    pid = Patient()
    obx = Observation()
    sch = Appointment()
    aip = Doctor()

    def parse(self, hl7_message):
        self.__msg = hl7.parse(hl7_message)
        self.parsePatient()
        self.parseObservation()
        self.parseAppointment()
        self.parseDoctor()

    def getMessageType(self):
        try:
            return str(self.__msg.segment('MSH')[9])
        except KeyError as e:
            print(str(e))

    def parsePatient(self):
        try:
            self.pid.ip = self.__msg.segment('PID')[3][0]
            self.pid.nom = self.__msg.segment('PID')[5][0][0]
            self.pid.prenom = self.__msg.segment('PID')[5][0][2]
            self.pid.date_naissance = self.__msg.segment('PID')[7][0]
            self.pid.sexe = self.__msg.segment('PID')[8][0]
            self.pid.adresse = self.__msg.segment('PID')[11][0]
        except KeyError as e:
            print(st(e))
    
    def parseObservation(self):
        try:
            self.obx.set_id = self.__msg.segment('OBX')[1][0]
            self.obx.value = self.__msg.segment('OBX')[5][0]
            self.obx.units = self.__msg.segment('OBX')[6][0]
            self.obx.references_range = self.__msg.segment('OBX')[7][0]
            self.obx.result = self.__msg.segment('OBX')[11][0]
        except KeyError as e:
            print(str(e))

    def parseAppointment(self):
        try:
            self.sch.id = self.__msg.segment('SCH')[1][0]
            self.sch.agenda = self.__msg.segment('SCH')[7][0][1]
            self.sch.acte = self.__msg.segment('SCH')[7][0][2]
            self.sch.date_debut = self.__msg.segment('SCH')[11][0][3]
            self.sch.date_fin = self.__msg.segment('SCH')[11][0][4]
        except KeyError as e:
            print(str(e))

    def parseDoctor(self):
        try:
            self.aip.nom = self.__msg.segment('AIP')[3][0][1]
        except KeyError as e:
            print(str(e))

# print("------------ Patient ----------")
# print("Patient Identifier:", msgObject.segment('self.pid')[3][0])
# print("Patient name:", msgObject.segment('self.pid')[5][0])
# print("Mother's Maiden Name:", msgObject.segment('self.pid')[6][0])
# print("Date/time birthday:", msgObject.segment('self.pid')[7][0])
# print("Administrative sex:", msgObject.segment('self.pid')[8][0])
# print("Patient Address:", msgObject.segment('self.pid')[11][0])


# print("------------ Observation ----------")

# print("Observation Identifier:", msgObject.segment('OBX')[3][0])
# print("Observation value:", msgObject.segment('OBX')[5][0])
# print("Units:", msgObject.segment('OBX')[6][0])
