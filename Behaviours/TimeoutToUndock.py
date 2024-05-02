from spade.behaviour import TimeoutBehaviour
from spade.message import Message
from TPMarina.Behaviours.Ask2Undock import *

class TimeoutToUndock(TimeoutBehaviour):

    async def run(self):
        print("comecei timeout to undock"+ self.agent.get("id"))
        beh1 = Ask2Undock()
        self.agent.add_behaviour(beh1)