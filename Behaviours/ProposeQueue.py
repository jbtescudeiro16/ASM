import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from TPMarina.Class.Msg import *


class ProposeQueue(OneShotBehaviour):
    def __init__(self, boat,size,myid,max2wait):
        self.boat = boat
        self.size=size
        self.myid=myid
        self.max2wait=max2wait
        super().__init__()

    async def run(self):
        response = Message(to=self.boat.get_jid())
        response.set_metadata("performative","propose")

        response.body = jsonpickle.encode(Message_Info(f"ADD2QUEUE?&{self.size}&{self.myid}&{self.max2wait}",self.boat))
        await self.send(response)
