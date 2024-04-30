import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import *
from TPMarina.Class.Msg import *

class ConfirmUndock(OneShotBehaviour):

    def __init__(self, boat):
        self.boat = boat
        super().__init__()


    async def run(self):
        msg = Message(to=self.boat.get_jid())
        msg.set_metadata("performative", "confirm")
        msg.body = jsonpickle.encode(Message_Info("UNDOCKCONCEDED",self.boat))


        free_cais = Message(to=self.agent.get("caismanager"))
        free_cais.set_metadata("performative", "inform")
        free_cais.body = jsonpickle.encode(Message_Info("BOAT_UNDOCKING",self.boat))

        await self.send(free_cais)
        await self.send(msg)
