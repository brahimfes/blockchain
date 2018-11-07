class Patient:
    def __init__(self):
        self.ip = ""
        self.nom = ""
        self.prenom = ""
        self.date_naissance = ""
        self.sexe = ""
        self.adresse = ""

    def __str__(self):
        return "Patient(ip: %s, nom: %s, prenom: %s, date naissance: %s, sexe: %s, adresse: %s)" % \
            (self.ip, self.nom, self.prenom, self.date_naissance, self.sexe, self.adresse)