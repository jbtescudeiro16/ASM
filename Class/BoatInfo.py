class BoatInfo:
    def __init__(self,jid,type,brand, origin, destination, fuel, status,cais,channel):
        self.jid = jid
        self.id= self.jid.split("@")[0]
        self.brand = brand
        self.type=type
        self.origin = origin
        self.destination = destination
        self.fuel = fuel
        self.status = status
        self.cais = cais
        self.channel=channel

    def get_id(self):
        return self.id

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

    def set_cais(self, cais):
        self.cais = cais

    def get_cais(self):
        return self.cais

    def get_channel(self):
        return self.channel


    def __str__(self):
        return "Boat: "+str(self.id) +"|Type: "+ self.type + "| Brand :" + self.brand +"| Origin:" +self.origin +"| Destination:" +self.destination + "| Fuel:" + str(self.fuel)