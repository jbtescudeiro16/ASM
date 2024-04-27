import jsonpickle
from spade.behaviour import *

from TPMarina.Behaviours.Permission_Cais import Permission_Cais


class Listener_Park_Requests(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux = jsonpickle.decode(msg.body)
                if aux.get_type() == "PARKPERMISSION":
                    print("Recebi um pedido para estacionar um barco no farol, no listener de pedidos de estacionamento ")
                    boat = aux.get_boatinfo()
                    # print(pl_info)
                    canais= self.agent.get("channels")

                    empty_channels = self.agent.getemptychannels()

                    if len(empty_channels) > 0:
                        if boat.get_type() == "Private":
                            if self.agent.get("CaisOccupied") < self.agent.get("CaisTotal"):
                                print(f"Permission to park conceded - {str(msg.sender)}")
                                permission = Permission_Cais(boat, empty_channels)
                                self.agent.add_behaviour(permission)
                        else:
                            if self.agent.get("DescargasOccupied") < self.agent.get("DescargasTotal"):
                                print(f"Permission to unload conceded - {str(msg.sender)}")
                                permission = Permission_Cais(boat, empty_channels)
                                self.agent.add_behaviour(permission)

