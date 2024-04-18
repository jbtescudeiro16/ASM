from spade import agent
from  TP.Class.LightInfo import *

import random
from TP.Behaviours.SendRequests import *
from TP.Behaviours.TrafficLightSystem import *

class Light_Agent(agent.Agent):

    PASSWORD = "NOPASSWORD"
    XMPP =  "jbtescudeiro16-vivobook-asuslaptop-x1605za-f1605za"
    myinfo=""

    async def setup(self):
        print("Agent Traffic Light starting...")
        username = str(self.jid).split('@')[0]
        username = username.replace("semaforo", "").capitalize()

        self.myinfo=LightInfo(username,"RED",3,self.jid)
        print("sou o semaforo" + self.myinfo.tostring())


        #Behaviour para informar o manager da sua chegada
        subscribe_behaviour = SubscribeBehav()
        self.add_behaviour(subscribe_behaviour)

        subscribe_sensor_behaviour = SubscribeSensor()
        self.add_behaviour(subscribe_sensor_behaviour)

        lightsystem=TrafficLightSystem()
        self.add_behaviour(lightsystem)




       # buy_behaviour = SendRequestsBehaviour(period=5)
       # wait_behaviour = ReceiveConfirmationsBehaviour()
       # self.add_behaviour(buy_behaviour)
       # self.add_behaviour(wait_behaviour)