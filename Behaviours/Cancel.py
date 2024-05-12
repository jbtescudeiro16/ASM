import jsonpickle
from spade.behaviour import TimeoutBehaviour
from spade.message import Message

from TPMarina.Class.BoatInfo import BoatInfo
from TPMarina.Class.Msg import *

class Cancel(TimeoutBehaviour):

    async def run(self):
        if self.agent.get("inqueue") == True:
            if self.agent.get("flag") == True:
                msg = Message(to=self.agent.get("lighthouse"))
                msg.body = jsonpickle.encode(Message_Info("CANCELOPERATION",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
                msg.set_metadata("performative", "cancel")
                await self.send(msg)
                #await self.agent.stop()
