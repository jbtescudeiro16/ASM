import jsonpickle
from spade.behaviour import CyclicBehaviour
from TPMarina.Behaviours.Permission_Cais import *


class ReceiveParking(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux=jsonpickle.decode(msg.body)
                if aux.get_type()=="ParkPermission":
                    print("Recebi um pedido para estacionar um barco no farol")
                    pl_info = aux.get_boatinfo()
                    #print(pl_info)
                    empty_channels=self.agent.getemptychannels()


                    if len(empty_channels) > 0:
                        if pl_info.get_type() == "Private":
                            if self.agent.get("CaisOccupied") < self.agent.get("CaisTotal"):
                                print(f"Permission to park conceded - {str(msg.sender)}")
                                permission = Permission_Cais(pl_info, empty_channels)
                                self.agent.add_behaviour(permission)
                        else:
                            if self.agent.get("DescargasOccupied") < self.agent.get("DescargasTotal"):
                                print(f"Permission to unload conceded - {str(msg.sender)}")
                                permission = Permission_Cais(pl_info, empty_channels)
                                self.agent.add_behaviour(permission)


            elif msg.get_metadata("performative") == ("confirm"):

                print("recebi confirm manager")
                aux=jsonpickle.decode(msg.body)
                tipomsg=aux.get_type()

                corpo= tipomsg.split(" & ")

                cais = corpo[0].strip()

                res = Message(to=aux.get_boatinfo().get_jid())
                res.body = f"{cais}"
                res.set_metadata("performative", "inform")
                await self.send(res)




