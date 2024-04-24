import jsonpickle
from spade.behaviour import OneShotBehaviour
from spade.message import *
from TPMarina.Class.Message import *

class Permission_Cais(OneShotBehaviour):
    # f'''Plane: {self.get("id")} | Jid: {self.get("jid")} | Type: {self.get("Type")} | Company: {self.get("Company")} | Origin: {self.get("Origin")} | Destination: {self.get("Destination")} | Fuel: {self.get("Fuel")} | Status: {self.get("status")}'''

    def __init__(self, boat, channels):
        self.boat = boat
        self.list_channels = channels

        super().__init__()


    async def run(self):
        msg = Message(to=self.agent.get("caismanager"))
        aux=Message_Info("FreePark?", self.boat)
        aux.set_channels(self.list_channels)
        msg.body=jsonpickle.encode(aux)
        msg.set_metadata("performative", "request")
        await self.send(msg)