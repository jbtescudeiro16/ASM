from spade.agent import *
from TPMarina.Behaviours.MarineInfo import *
from TPMarina.Behaviours.ReceiveUpdatesPolice import *

class Marine_Police(Agent):

    async def setup(self):
        print("MarinePolice Manager starting...")
        self.set("Queue" ,[])

        behav1 = Marine_Info(period=3)
        self.add_behaviour(behav1)

        behav2=PoliceReceive()
        self.add_behaviour(behav2)



