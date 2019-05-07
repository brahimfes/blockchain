class Doctor:
    def __init__(self):
        self.nom = ""

    def __str__(self):
        return "Docteur(nom: %s)" %  (self.nom)