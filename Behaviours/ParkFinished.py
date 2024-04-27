import jsonpickle
from spade.behaviour import TimeoutBehaviour
from spade.message import Message
from TPMarina.Class.Message import *
from TPMarina.Class.BoatInfo import *

import datetime


class ParkFinished(TimeoutBehaviour):
    async def run(self):
        msg = Message(to=self.agent.get("lighthouse"))
        msg.set_metadata("performative", "inform")
        msg.body = jsonpickle.encode( Message_Info("PARKCOMPLETED",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))

        print("Ja estacionei e vou abandonar o canal"+ self.agent.get("jid"))
        await self.send(msg)


