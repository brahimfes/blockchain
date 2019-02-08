class Appointment:
    def __init__(self):
        self.id = ""

    def __str__(self):
        return "Appointment(id: %s)" % \
            (self.id)