import jsonpickle
from spade.behaviour import TimeoutBehaviour
from spade.message import Message
from TPMarina.Class.Msg import *
from TPMarina.Class.BoatInfo import *
from TPMarina.Behaviours.TimeoutToUndock import *

import datetime


class ParkFinished(TimeoutBehaviour):
    async def run(self):
        msg = Message(to=self.agent.get("lighthouse"))
        msg.set_metadata("performative", "inform")
        msg.body = jsonpickle.encode( Message_Info("PARKCOMPLETED",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))

        #print("Ja estacionei e vou abandonar o canal"+ self.agent.get("jid"))
        await self.send(msg)

        origin = self.agent.get("Origin")
        destination = self.agent.get("Destination")
        self.agent.set("Origin", destination)
        self.agent.set("Destination", origin)
        self.agent.set("Fuel", 100)
        self.agent.set("status","permission2Leave")
        start_At = datetime.datetime.now() + datetime.timedelta(seconds=15)
        beh1 = TimeoutToUndock(start_at=start_At)
        self.agent.add_behaviour(beh1)
