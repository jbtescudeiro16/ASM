from spade.behaviour import TimeoutBehaviour
from spade.message import Message
from TPMarina.Behaviours.Ask2Undock import *

class TimeoutToUndock(TimeoutBehaviour):

    async def run(self):
        beh1 = Ask2Undock()
        self.agent.add_behaviour(beh1)