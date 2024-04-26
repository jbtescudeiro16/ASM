import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import *
from TPMarina.Class.Message import *
from TPMarina.Class.BoatInfo import *
class AddTOrandCais(OneShotBehaviour):
    async def run(self):
        #print("Behaviour add to random cais Starting")
        msg = Message(to=self.agent.get("lighthouse"))
        msg.body=jsonpickle.encode(Message_Info("ADD2RANDCAIS",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
        msg.set_metadata("performative", "request")
        await self.send(msg)
