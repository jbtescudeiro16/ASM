import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from TPMarina.Behaviours.ConfirmUndock import *

class Listerer_Undock_Requests(CyclicBehaviour):

    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux = jsonpickle.decode(msg.body)
                partida=aux.get_type().split("&")
                info=partida[0]
                if info=="ASK2UNDOCK":
                    cais = aux.get_boatinfo().get_cais()

                    #print(cais)
                    pistas=self.agent.getemptychannels()

                    if len(pistas) >0:
                        pistaescolhida=self.agent.choose_channel_undock(aux.get_boatinfo())
                        #print(pistaescolhida)

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