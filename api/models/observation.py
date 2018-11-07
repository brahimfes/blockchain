class Observation:
    def __init__(self):
        self.set_id = ""
        self.value = ""
        self.units = ""
        self.references_range = ""
        self.result = ""

    def __str__(self):
        return "Observation(id: %s, value: %s, units: %s, references range: %s, result: %s)" % \
            (self.set_id, self.value, self.units, self.references_range, self.result)