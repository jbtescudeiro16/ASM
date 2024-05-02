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

            elif msg.get_metadata("performative") == ("refuse"):
                aux=jsonpickle.decode(msg.body)
                info=aux.get_type()
                if info=="FULLQUEUE":
                    print("Queue cheia. a terminar agente")
                if info=="NOPARKS":
                    print("Não há parques livres ")

            elif msg.get_metadata("performative") == ("propose"):
                aux=jsonpickle.decode(msg.body)
                info=aux.get_type()
                partido=info.split("&")
                if partido[0]=="ADD2QUEUE?":

                    if int(partido[1]) +1 <= int(partido[3]):
                        print("ACcEPT QUEUE " + self.agent.get("id"))
                        response = Message(to= self.agent.get("lighthouse"))
                        response.set_metadata("performative", "accept_proposal")
                        response.body = jsonpickle.encode(
                        Message_Info(f"ACCEPTQUEUE&{partido[2]}", BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
                        await self.send(response)



                    else:
                        response = Message(to=self.agent.get("lighthouse"))
                        response.set_metadata("performative", "reject_proposal")
                        response.body = jsonpickle.encode(
                            Message_Info(f"REJECTQUEUE&{partido[2]}", BoatInfo(self.agent.get("jid"),self.agent.get("type"),self.agent.get("brand"),self.agent.get("origin"),self.agent.get("destination"),self.agent.get("fuel"),self.agent.get("status"),self.agent.get("cais"),self.agent.get("channel"))))
                        print("mandei para REJEITAR ")
                        await self.send(response)




