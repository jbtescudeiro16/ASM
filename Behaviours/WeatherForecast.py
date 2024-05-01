import random

from spade.behaviour import *
from TPMarina.Behaviours.empty_queue import *

class WeatherForecast(PeriodicBehaviour):
    async def run(self):
        tempo= self.agent.get("Weather")


        condicoes_meteorologicas = ['Sunny', 'Stormy', 'Rainy', 'Cloudy']
        pesos = [5, 5, 75, 75]

        condicao_escolhida = random.choices(condicoes_meteorologicas, weights=pesos, k=1)[0]
        self.agent.set("Weather",condicao_escolhida)

        pistas=self.agent.get("channels")


        if condicao_escolhida=="Rainy":
            livres=self.agent.getemptychannels()
            if len(livres)-1 >= 1:
                flag= False
                for i in pistas:
                    if flag==False:
                         if i.get_available()==True:
                            i.set_chuvoso()
                            flag=True
            self.agent.set("channels", pistas)
        elif condicao_escolhida == "Stormy":
            for i in pistas:
                if i.get_available()==True:
                    i.set_chuvoso()
            self.agent.set("channels", pistas)

        elif condicao_escolhida == "Sunny" or condicao_escolhida == "Cloudy" :
                for i in pistas:
                    if i.get_state_channel()=="Closed" :
                        i.set_state_channel("Open")
                        i.set_available(True)
                self.agent.set("channels", pistas)
                beh1=EmptyQueue("")
                self.agent.add_behaviour(beh1)
