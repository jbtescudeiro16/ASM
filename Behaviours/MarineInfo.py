import jsonpickle
from spade.behaviour import *
from TPMarina.Class.Msg import *
import datetime

class Marine_Info(PeriodicBehaviour):
    async def on_start(self):
        self.counter = 0

    async def run(self):

        print(f"Marine Info at {datetime.datetime.now().time()}: {self.counter}")

        self.counter += 1

        msg = Message(to=self.agent.get("lighthouse"))
        msg.set_metadata("performative", "request")
        msg.body= jsonpickle.encode( Message_Info("MARINEINFO",""))
        await self.send(msg)