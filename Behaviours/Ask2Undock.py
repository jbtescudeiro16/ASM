import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import  *

from TPMarina.Class.BoatInfo import BoatInfo
from TPMarina.Class.Message import *
class Ask2Undock(OneShotBehaviour):
    async def run(self):
        msg = Message(to=self.agent.get("lighthouse"))
        msg.set_metadata("performative", "request")
        cais=self.agent.get("cais")
        msg.body=jsonpickle.encode(Message_Info(f"ASK2UNDOCK&{cais}",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),cais,self.agent.get("channel"))))
        await self.send(msg)
