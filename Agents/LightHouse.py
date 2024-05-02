import json
import random

from spade import  agent

from TPMarina.Behaviours.Listener_Park_Requests import Listener_Park_Requests
from TPMarina.Class.Channel import channel
from TPMarina.Behaviours.Light_Receive_Park import *
from TPMarina.Behaviours.Listener_Undock_Requests import *
from TPMarina.Behaviours.WeatherForecast import *
class LightHouse(agent.Agent):

    async def setup(self):
        print("LightHouse Starting")
        f = open("settings.json")
        conf = json.load(f)
        self.set("QueueCount",0)
        self.set("Queue", [])
        self.set("maxboats2park", conf["maxboats2park"])
        self.set("Weather", conf["weather"])
        self.set("Arrivals", 0)
        self.set("Departures", 0)
        self.set("Canceled", 0)
        self.set("CaisTotal", conf["cais"])
        self.set("DescargasTotal", conf["descargas"])
        self.set("occupiedchannels", [])


        channels_array= []

        for index in range(conf["channels"]):
            x = "%.2f" % random.randint(0, 1000)
            y = "%.2f" % random.randint(0, 1000)
            canal = channel(x, y, index)
            channels_array.append(canal)

        self.set("channels", channels_array)
        self.set("DescargasOccupied", 0)
        self.set("CaisOccupied", 0)



        beh1=ReceiveParking()
        self.add_behaviour(beh1)

        beh2 = Listerer_Undock_Requests()
        self.add_behaviour(beh2)

        beh3=Listener_Park_Requests()
        self.add_behaviour(beh3)

        beh4 = WeatherForecast(period=10)
        self.add_behaviour(beh4)

    def getemptychannels(self):
        ret = []
        for channel in self.get("channels"):
            if channel.get_available() == True and channel.get_state_channel()=="Open":
                ret.append((channel.get_id(),channel.get_coords()))
        return ret

    def removeboat_channel(self,id):
        for channel in self.get("channels"):
            if channel.get_available()==False and channel.get_boat()!=None:
                if (channel.get_boat().get_id()== id):
                    channel.remove_boat()
                    channel.set_available(True)

    def choose_channel_undock(self,boat):
            channel_chosen = None
            for channel in self.get("channels"):
                if channel.available==True:
                    x, y = channel.get_coords()
                    if channel_chosen == None:
                        channel_chosen = channel
                    elif ((pow(float(x) - float(channel.x), 2) + pow(float(y) - float(channel.y), 2)) < (
                            pow(float(x) - float(channel_chosen.x), 2) + pow(float(y) - float(channel_chosen.y), 2))):
                        channel_chosen = channel

            if channel_chosen != None:
                channel_chosen.set_boat(boat, "UNDOCKING")
                channel_chosen.set_available(False)

            return channel_chosen
    def results(self):
        with open("results.json", "w") as outfile:
            dictionary = {}
            dictionary["Parks"] = self.get("Arrivals")
            dictionary["Undocks"] = self.get("Departures")
            dictionary["Canceled"] = self.get("Canceled")
            json.dump(dictionary, outfile)
            outfile.flush()