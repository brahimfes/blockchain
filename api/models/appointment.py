class Appointment:
    def __init__(self):
        self.id = ""
        self.agenda = ""
        self.acte = ""
        self.date_debut = ""
        self.date_fin = ""
        self.etat = ""


    def __str__(self):
        return "Appointment(id: %s)" % \
            (self.id)