from spade.behaviour import OneShotBehaviour
from spade.message import *

from TPMarina.Behaviours.ConfirmUndock import ConfirmUndock
from TPMarina.Behaviours.Permission_Cais import Permission_Cais
from TPMarina.Behaviours.Refuse import Refuse
from TPMarina.Class import *
from termcolor import colored

class EmptyQueue(OneShotBehaviour):

    def __init__(self, type):
        self.type = type
        super().__init__()


    def getoldest(self, queue):
        oldest = None
        min_age = float('inf')
        for item in queue:
            if isinstance(item, tuple) and len(item) == 3:
                if item[2] < min_age:
                    min_age = item[2]
                    oldest = item
        return oldest


    async def run(self):
        print("Tratar a queue")
        queue=self.agent.get("Queue")
        if len(queue)>0:

            old=self.getoldest(queue)
            type= old[0]

            if type=="WAITING2PARK":
                print("o tipo de quem vou tratar é waiting 2 park")
                boat=old[1]
                empty_channels = self.agent.getemptychannels()
                if len(empty_channels) > 0:
                    if boat.get_type() == "Private":
                        if self.agent.get("CaisOccupied") < self.agent.get("CaisTotal"):
                            print("aceitei privado")
                            permission = Permission_Cais(boat, empty_channels)
                            self.agent.add_behaviour(permission)
                        else :
                            print("recusei pq n ha parques privados")
                            self.agent.set("Queue",
                                           [i for i in self.agent.get("Queue") if i[1].get_id() != boat.get_id()])
                            behav3 = Refuse(boat, "NOPARKS")
                            self.agent.add_behaviour(behav3)
                            can = self.agent.get("Canceled")
                            self.agent.set("Canceled", can+1)

                    else:
                        if self.agent.get("DescargasOccupied") < self.agent.get("DescargasTotal"):
                            permission = Permission_Cais(boat, empty_channels)
                            self.agent.add_behaviour(permission)
                        else:

                            self.agent.set("Queue",
                                           [i for i in self.agent.get("Queue") if i[1].get_id() != boat.get_id()])
                            behav3 = Refuse(boat, "NOPARKS")
                            self.agent.add_behaviour(behav3)
                            can= self.agent.get("Canceled")
                            self.agent.set("Canceled",can+1)


            elif type=="WAITING2UNDOCK":
                boat=old[1]
                empty_channels = self.agent.getemptychannels()
                if len(empty_channels) > 0:
                    pistaescolhida = self.agent.choose_channel_undock(boat)
                    count = self.agent.get("QueueCount")
                    self.agent.set("Queue",
                                   [i for i in self.agent.get("Queue") if i[1].get_id() != boat.get_id()])
                    if boat.get_type() == "Private":
                        cais_occupation = self.agent.get(f"CaisOccupied")
                        if cais_occupation > 0:
                            print("reduzi no emptyqueue cais")
                            self.agent.set(f"CaisOccupied", cais_occupation - 1)
                    else:
                        cais_occupation = self.agent.get(f"DescargasOccupied")
                        if cais_occupation > 0:
                            print("reduzi no emptyqueue descargas")
                            self.agent.set(f"DescargasOccupied", cais_occupation - 1)

                    behav1 = ConfirmUndock(boat)
                    self.agent.add_behaviour(behav1)

        else:
            print("Queue Vazia, Ignorar")



