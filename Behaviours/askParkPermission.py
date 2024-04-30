import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import *
from TPMarina.Class.BoatInfo import*
from TPMarina.Class.Msg import *

class Permission2Park(OneShotBehaviour):


    async def run(self):
        msg = Message(to=self.agent.get("lighthouse"))
        msg.body=jsonpickle.encode(Message_Info("PARKPERMISSION",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
        msg.set_metadata("performative", "request")
        await self.send(msg)