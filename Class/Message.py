
class Message_Info:
    def __init__(self, type, boatinfo):
        self.type = type
        self.boatinfo = boatinfo
        self.channels=[]

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_boatinfo(self):
        return self.boatinfo

    def set_boatinfo(self, boatinfo):
        self.boatinfo = boatinfo

    def set_channels(self, channels):
        self.channels = channels

    def get_channels(self):
           return self.channels

    def __str__(self):
        return f"Message Type: {self.type}, Boat Info: {self.boatinfo}, {self.channels}"
