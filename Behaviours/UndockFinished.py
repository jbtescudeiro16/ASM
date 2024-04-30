import jsonpickle
from spade.behaviour import TimeoutBehaviour
from spade.message import *
from TPMarina.Class.Msg import *
from TPMarina.Class.BoatInfo import *


class UndockFinished(TimeoutBehaviour):
    async def run(self):
        msg = Message(to=self.agent.get("lighthouse"))
        msg.set_metadata("performative", "inform")
        msg.body=jsonpickle.encode(Message_Info("UNDOCKFINISHED",BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
        await self.send(msg)
        await self.agent.stop()