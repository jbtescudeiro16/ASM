from spade import agent
from  TP.Class.LightInfo import *
import random
from TP.Behaviours.SendRequests import *
from spade.behaviour import CyclicBehaviour
import time




class TrafficLightSystem(CyclicBehaviour):

    def avancar_proximo(self):
        letras = ['A', 'B', 'C', 'D']
        indice_atual = letras.index(self.agent.myinfo.getroad()[0])
        proximo_indice = (indice_atual + 1) % len(letras)  # Próximo índice circularmente
        proxima_letra = letras[proximo_indice]
        return proxima_letra

    async def run(self):

        msg = await self.receive(timeout=5)
        if msg:
            if msg.get_metadata("performative") == ("inform"):
                self.agent.myinfo.setcolour("GREEN")
                print("Está verde em "+ self.agent.myinfo.getroad())
                tempo=self.agent.myinfo.gettime()
                while tempo > 0:
                    time.sleep(1)
                    tempo -= 1
                    print("Faltam " + str(tempo) +"Para ficar Amarelo")
                self.agent.myinfo.setcolour("YELLOW")
                time.sleep(1)
                print("Vai ficar vermleho")
                self.agent.myinfo.setcolour("RED")

                proximo1=self.avancar_proximo()
                print("##############")
                print("O proximo é : "+proximo1)
                message1 = Message(to=f"semaforo{proximo1}1@{self.agent.XMPP}")
                message1.set_metadata("performative", "inform")
                message1.body = jsonpickle.encode("TurnGreen")
                print("mandei para o next")
                await self.send(message1)

                message2 = Message(to=f"semaforo{proximo1}2@{self.agent.XMPP}")
                message2.set_metadata("performative", "inform")
                message2.body = jsonpickle.encode("TurnGreen")
                print("amndei para o next")
                await self.send(message2)
