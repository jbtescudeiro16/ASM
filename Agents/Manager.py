import time

from spade import agent

from TP.Behaviours.ReceiveRequests import *
from TP.Behaviours.SendRequests import *


class ManagerAgent(agent.Agent):
    PASSWORD = "NOPASSWORD"
    XMPP = "jbtescudeiro16-vivobook-asuslaptop-x1605za-f1605za"
    semaforos= []
    flag = False

    async def setup(self):

        print("Agent Manager starting...")
        receive=ReceiveRequestsBehaviourMan()
        self.add_behaviour(receive)

