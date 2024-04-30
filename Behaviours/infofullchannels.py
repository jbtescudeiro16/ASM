import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from TPMarina.Class.Msg import *

class FullChannels(OneShotBehaviour):
    def __init__(self, boat):
        self.boat = boat
        super().__init__()
    async def run(self):
        response = Message(to=self.boat.get_jid())
        response.set_metadata("performative","refuse")
        response.body = jsonpickle.encode(Message_Info("ADDED2QUEUE",self.boat))
        await self.send(response)

