import json
import random

from spade import  agent
from TPMarina.Class.Channel import *
from TPMarina.Behaviours.Light_Receive_Park import *
class LightHouse(agent.Agent):

    async def setup(self):
        print("LightHouse Starting")
        f = open("settings.json")
        conf = json.load(f)

        self.set("Queue", [])
        self.set("maxboats2park", conf["maxboats2park"])
        self.set("Arrivals", 0)
        self.set("Departures", 0)
        self.set("Canceled Arrivals", 0)
        self.set("CaisTotal", conf["cais"])
        self.set("DescargasTotal", conf["descargas"])


        channels_array= []
        for index in range(conf["channels"]):
            x = "%.2f" % random.randint(0, 1000)
            y = "%.2f" % random.randint(0, 1000)
            channel = Channel(x, y, index)
            channels_array.append(channel)

        self.set("channels", channels_array)
        self.set("DescargasOccupied", 0)
        self.set("CaisOccupied", 0)

        for i in self.get("channels"):
              print(i)

        beh1=ReceiveParking()
        self.add_behaviour(beh1)


    def getemptychannels(self):
        ret = []
        ret2 = []
        for channel in self.get("channels"):
            if channel.get_available() == True:
                ret.append((channel.get_id(),channel.get_coords()))
                ret2.append(channel.get_id())
        return ret