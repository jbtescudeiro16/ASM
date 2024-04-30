import random

from spade import agent
from TPMarina.Class.BoatInfo import *
from TPMarina.Behaviours.askParkPermission import *
from TPMarina.Behaviours.Boat_Receiver import *


class Boat(agent.Agent):
    #myinfo = ""

    def __str__(self):
        return f'''Boat:Jid: {self.get("jid")}  |Type:{self.get("type")} | Brand: {self.get("brand")} | Origin: {self.get("origin")} | Destination: {self.get("destination")} | Fuel: {self.get("fuel")} | status: {self.get("status")}| Cais: {self.get("cais")},Channel: {self.get("channel")}'''
    async def setup(self):
        brands = ["Sunseeker", "Beneteau", "Azimut", "Ferretti Yachts", "Princess Yachts",
                  "Sea Ray", "Jeanneau", "Bayliner", "Boston Whaler", "Riva"]

        ports = ["Roterdão", "Xangai", "Cingapura", "Antuérpia", "Hamburgo", "Los Angeles", "Long Beach", "Busan",
                 "Dubai", "Qingdao", "Tianjin", "Singapura", "Ningbo-Zhoushan"]

        types = {1: "Private", 2: "Passenger Transport", 3: "Cargo Transport"}

        self.set("brand", brands[random.randint(0, 9)])
        self.set("fuel", random.randint(0, 100))
        self.set("cais", None)
        self.set("id", self.get("jid").split("@")[0])
        self.set("channel", None)
        self.set("type",types[random.choices([1, 2, 3], [2, 1, 1])[0]])

        if self.get("status") == "permission2Leave":
            self.set("destination", ports[random.randint(0,12)])

            self.set("origin", "Leixões")


        elif self.get("status") == "permission2Park":
           self.set("destination","Leixṍes")
           self.set("origin",ports[random.randint(0,12)])


        receiver = Boat_Receiver()
        self.add_behaviour(receiver)




        #self.myinfo = BoatInfo(self.jid, brand, origin,destination,fuel,self.get("status"),dock,channel)
        #print(self.myinfo.to_string())


