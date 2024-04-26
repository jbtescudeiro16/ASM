import random


class Cais:
    def __init__(self, type, jid):
        self.jid = jid
        self.id= self.jid.split("@")[0]
        self.x = "%.2f" % random.randint(0, 100)
        self.y = "%.2f" % random.randint(0, 100)
        self.available = True
        self.type = type
        self.boat = None

    def get_id(self):
        return self.id

    def get_jid(self):
        return self.jid

    def get_coords(self):
        return self.x, self.y

    def get_availability(self):
        return self.available

    def set_boat(self, boat):
        self.available = False
        self.boat = boat

    def remove_boat(self):
        self.available = True
        self.boat = None

    def __str__(self):
        return f'''Cais JId: {self.jid}+ |Type: {self.type} | X: {str(self.x)} | Y: {str(self.y)} | Livre {self.available}'''
