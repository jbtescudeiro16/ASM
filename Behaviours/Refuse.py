

import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from TPMarina.Class.Msg import *


class Refuse(OneShotBehaviour):
    def __init__(self, boat,info):
        self.boat = boat
        self.info=info
        super().__init__()

    async def run(self):
        response = Message(to=self.boat.get_jid())
        response.set_metadata("performative","refuse")
        response.body = jsonpickle.encode(Message_Info(self.info,self.boat))
        await self.send(response)

