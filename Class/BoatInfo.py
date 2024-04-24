class BoatInfo:
    def __init__(self,jid,type,brand, origin, destination, fuel, status,dock,channel):
        self.jid = jid
        self.brand = brand
        self.type=type
        self.origin = origin
        self.destination = destination
        self.fuel = fuel
        self.status = status
        self.dock = dock
        self.channel=channel

    def get_jid(self):
        return self.jid

    def get_type(self):
        return self.type


    def get_brand(self):
        return self.brand

    def get_origin(self):
        return self.origin

    def get_destination(self):
        return self.destination

    def get_fuel(self):
        return self.fuel

    def get_status(self):
        return self.status

    def set_dock(self, dock):
        self.dock = dock

    def get_dock(self):
        return self.dock

    def get_channel(self):
        return self.channel


    def __str__(self):
        return "Boat: "+str(self.jid) +"|Type+"+ self.type + "| Brand :" + self.brand +"| Origin:" +self.origin +"| Destination:" +self.destination + "| Fuel:" + str(self.fuel) + "| Dock:" +str(self.dock)