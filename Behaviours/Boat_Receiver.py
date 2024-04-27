import datetime

import jsonpickle
from spade.behaviour import CyclicBehaviour
from TPMarina.Behaviours.Ask2Undock import *
from TPMarina.Behaviours.UndockFinished import *
from TPMarina.Behaviours.ParkFinished import *

class Boat_Receiver(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:

            if msg.get_metadata("performative") == ("inform"):
                aux=jsonpickle.decode(msg.body)

                info=aux.get_type().split("&")
                if info[0]== "Cais":
                    print("Cais")

                    self.agent.set("cais",info[1])
                    print("\033[92mDefini o meu cais Inicial no barco:" + str(self.agent.jid) + "\n Cais :"+ self.agent.get("cais")+"\033[0m")


                    behav1=Ask2Undock()
                    self.agent.add_behaviour(behav1)
                elif info[0]=="PARKCONCEDED":
                    cais=info[1]
                    channel=info[2]
                    self.agent.set("cais", cais)
                    print("\033[92mDefini o meu cais estacionado no barco:" + str(self.agent.jid) + "\033[0m")

                    start_At = datetime.datetime.now() + datetime.timedelta(seconds=10)
                    print("foi me concedido parque e vou adicionar o comportamento")
                    confirmation = ParkFinished(start_at=start_At)
                    self.agent.add_behaviour(confirmation)




            elif msg.get_metadata("performative") == ("confirm"):
                aux=jsonpickle.decode(msg.body)
                info=aux.get_type()
                if info=="UNDOCKCONCEDED":
                    print(aux.get_boatinfo().get_id()+"-> Undocking")
                    self.agent.set("cais", None)
                    start_At = datetime.datetime.now() + datetime.timedelta(seconds=10)

                    confirmation = UndockFinished(start_at=start_At)
                    self.agent.add_behaviour(confirmation)


