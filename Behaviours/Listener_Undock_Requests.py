import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from TPMarina.Behaviours.ConfirmUndock import *
from TPMarina.Behaviours.infofullchannels import *

class Listerer_Undock_Requests(CyclicBehaviour):

    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux = jsonpickle.decode(msg.body)
                partida=aux.get_type().split("&")
                info=partida[0]
                if info=="ASK2UNDOCK":
                    print("recebi pedido undock")
                    cais = aux.get_boatinfo().get_cais()

                    #print(cais)
                    pistas=self.agent.getemptychannels()
                    print("Pistas vazias" + str(pistas))
                    if len(pistas) >0:
                        print("tamanho das pistas maior que 0")
                        pistaescolhida=self.agent.choose_channel_undock(aux.get_boatinfo())
                        count = self.agent.get("QueueCount")
                        print("queue antes: " + str(self.agent.get("Queue")))
                        self.agent.set("Queue", [i for i in self.agent.get("Queue") if
                                                 i[1].get_id() != aux.get_boatinfo().get_id()])

                        print("queue depois: " + str(self.agent.get("Queue")))

                        if aux.get_boatinfo().get_type()=="Private":
                            cais_occupation = self.agent.get(f"CaisOccupied")
                            if cais_occupation > 0:
                                self.agent.set(f"CaisOccupied", cais_occupation - 1)
                        else :
                            cais_occupation = self.agent.get(f"DescargasOccupied")
                            if cais_occupation > 0:
                                self.agent.set(f"DescargasOccupied", cais_occupation - 1)

                        behav1 = ConfirmUndock(aux.get_boatinfo())
                        self.agent.add_behaviour(behav1)

                    elif len(pistas) == 0:
                        print("Não ha canais vazios no listener de undock")
                        queue = self.agent.get("Queue")
                        count = self.agent.get("QueueCount")

                        if not any(item[1].get_id() == aux.get_boatinfo().get_id() for item in queue):
                            queue.append(("WAITING2UNDOCK", aux.get_boatinfo(), count))
                            self.agent.set("QueueCount", count + 1)
                            self.agent.set("Queue", queue)
                            behav3 = FullChannels(aux.get_boatinfo())
                            self.agent.add_behaviour(behav3)