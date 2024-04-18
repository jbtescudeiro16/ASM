from spade import agent
from  TP.Class.CarInfo import *
import random
from   TP.Behaviours.SendRequests import *

class CarAgent(agent.Agent):

    PASSWORD = "NOPASSWORD"
    XMPP =  "jbtescudeiro16-vivobook-asuslaptop-x1605za-f1605za"
    myinfo=""

    def destino_do_carro(self,letra, numero):
        if letra == 'A':
            if numero == 1:
                return "B3"
            elif numero == 2:
                return random.choice(['C3', 'D3'])
        elif letra == 'B':
            if numero == 1:
                return "C3"
            elif numero == 2:
                return random.choice(['D3', 'A3'])
        elif letra == 'C':
            if numero == 1:
                return "D3"
            elif numero == 2:
                return random.choice(['B3', 'A3'])
        elif letra == 'D':
            if numero == 1:
                return "A3"
            elif numero == 2:
                return random.choice(['B3', 'C3'])
            else:
                return "Número de faixa inválido para a letra D"
        else:
            return "Letra inválida"

    async def setup(self):
        print("Agent Car starting...")
        letra_aleatoria = random.choice(['A', 'B', 'C', 'D'])

        numero_aleatorio = random.randint(1, 2)

        resultado = letra_aleatoria + str(numero_aleatorio)

        aux=self.destino_do_carro(letra_aleatoria, numero_aleatorio)

        self.myinfo=carinfo(resultado,aux,self.jid)


        print("sou o carro"+ self.myinfo.tostring())
        carpassing=CarPassing()
        self.add_behaviour(carpassing)
