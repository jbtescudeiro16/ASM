from spade import agent

from TP.Behaviours.ReceiveRequests import *
from TP.Class.SensorInfo import *

class SensorAgent(agent.Agent):
    PASSWORD = "NOPASSWORD"
    XMPP = "jbtescudeiro16-vivobook-asuslaptop-x1605za-f1605za"
    semaforo=""
    myinfo=""
    async def setup(self):
        print("Agent Sensor  starting...")
        username = str(self.jid).split('@')[0]
        username = username.replace("sensor", "").capitalize()

        self.myinfo = SensorInfo(username, "RED", 3,[], self.jid)
        print("sou o sensor" + self.myinfo.tostring())
        receive=ReceiveRequestsBehaviourSensor()
        self.add_behaviour(receive)

        cars=ReceiveCarsBehaviourSensor()
        self.add_behaviour(cars)
