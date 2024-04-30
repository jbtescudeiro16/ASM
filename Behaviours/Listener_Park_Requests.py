import jsonpickle
from spade.behaviour import *

from TPMarina.Behaviours.Permission_Cais import Permission_Cais
from TPMarina.Behaviours.infofullchannels import *


class Listener_Park_Requests(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux = jsonpickle.decode(msg.body)
                if aux.get_type() == "PARKPERMISSION":
                    #print("Recebi um pedido para estacionar um barco no farol, no listener de pedidos de estacionamento ")
                    boat = aux.get_boatinfo()
                    # print(pl_info)
                    canais= self.agent.get("channels")

                    empty_channels = self.agent.getemptychannels()
                    print("Neste momento estão vazios : "+ str(empty_channels))
                    if len(empty_channels) > 0:
                        if boat.get_type() == "Private":
                            if self.agent.get("CaisOccupied") < self.agent.get("CaisTotal"):
                                print(f"Permission to park conceded - {str(msg.sender)}")
                                permission = Permission_Cais(boat, empty_channels)
                                self.agent.add_behaviour(permission)
                            else:
                                queue = self.agent.get("Queue")
                                count = self.agent.get("QueueCount")
                                if not any(item[1].get_id() == aux.get_boatinfo().get_id() for item in queue):
                                    queue.append(("WAITING2PARK", aux.get_boatinfo(), count))
                                    self.agent.set("QueueCount", count + 1)
                                    self.agent.set("Queue", queue)
                                    behav3 = FullChannels(aux.get_boatinfo())
                                    self.agent.add_behaviour(behav3)
                        else:
                            if self.agent.get("DescargasOccupied") < self.agent.get("DescargasTotal"):
                                print(f"Permission to unload conceded - {str(msg.sender)}")
                                permission = Permission_Cais(boat, empty_channels)
                                self.agent.add_behaviour(permission)
                            else:
                                queue = self.agent.get("Queue")
                                count = self.agent.get("QueueCount")
                                if not any(item[1].get_id() == aux.get_boatinfo().get_id() for item in queue):
                                    queue.append(("WAITING2PARK", aux.get_boatinfo(), count))
                                    self.agent.set("QueueCount", count + 1)
                                    self.agent.set("Queue", queue)
                                    behav3 = FullChannels(aux.get_boatinfo())
                                    self.agent.add_behaviour(behav3)

                    elif len(empty_channels)==0:
                        print("Não ha canais vazios no listener de parque")
                        queue = self.agent.get("Queue")
                        count = self.agent.get("QueueCount")

                        if not any(item[1].get_id() == aux.get_boatinfo().get_id() for item in queue):
                            queue.append(("WAITING2PARK", aux.get_boatinfo(), count))
                            self.agent.set("QueueCount", count + 1)
                            self.agent.set("Queue", queue)
                            behav3 = FullChannels(aux.get_boatinfo())
                            self.agent.add_behaviour(behav3)





