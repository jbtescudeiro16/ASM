import json

from spade import agent
from TPMarina.Class.Cais import *
from TPMarina.Behaviours.CaisReceive import *


class CaisManager(agent.Agent):
    async def setup(self):
       print("Cais Manager Starting")
       f = open("settings.json")
       conf = json.load(f)
       self.set("cais", [])
       self.set("nr_cais", conf["cais"])
       self.set("nr_descargas", conf["descargas"])
       self.set("max_parks", self.get("nr_cais") + self.get("nr_descargas"))

       for i in range(self.get("max_parks")):
           if i < self.get("nr_cais"):
               cais = Cais("Private", f"cais{i}")
               self.get("cais").append(cais)
           else:
               descargas = Cais("Commercial", f"cais{i}")
               self.get("cais").append(descargas)

       aux=self.get("cais")

       behav1=CaisReceive()
       self.add_behaviour(behav1)

    def closest_available(self, type, boat, available_channels):
        cais_available = None
        channel = None
        #print(type)
        for id_channel, xy in available_channels.items():
            for cais in self.get("cais"):
                #print(cais)
                if type=="Private" and cais.type=="Private" and cais.available == True :
                    #print("entrei em private")
                    if cais_available == None:
                        cais_available = cais
                        channel = id_channel
                    elif ((pow(float(xy[0]) - float(cais.x), 2) + pow(float(xy[1]) - float(cais.y), 2)) < (
                            pow(float(xy[0]) - float(cais_available.x), 2) + pow(
                        float(xy[1]) - float(cais_available.y), 2))):
                        cais_available = cais
                        channel = id_channel
                elif cais.type=="Commercial"and (type=="Passenger Transport" or type=="Cargo Transport") and cais.available == True:
                        #print("Entrei em baixo")
                        if cais_available == None:
                            cais_available = cais
                            channel = id_channel
                        elif ((pow(float(xy[0]) - float(cais.x), 2) + pow(float(xy[1]) - float(cais.y), 2)) < (
                                pow(float(xy[0]) - float(cais_available.x), 2) + pow(
                            float(xy[1]) - float(cais_available.y), 2))):
                            cais_available = cais
                            channel = id_channel
        if cais_available != None:
            cais_available.set_boat(boat)
        return channel, cais_available

    def parkboat(self, type, boat):
        for cais in self.get("cais"):
            # print("HANGAR ID =", hangar.get_id(), " | AVAILABLE = ", hangar.get_availability())
            if type == cais.type and cais.get_availability() == True:
                cais.set_plane(boat)
                return cais


    def freepark(self, boat):
        for cais in self.get("cais"):
            if boat == cais.boat:
                cais.remove_boat()
