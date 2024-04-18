import random

from spade.behaviour import OneShotBehaviour
import jsonpickle
from spade.behaviour import PeriodicBehaviour
from spade.message import Message


class SubscribeBehav(OneShotBehaviour):
    async def run(self):
        message = Message(to=f"manager@{self.agent.XMPP}")
        message.set_metadata("performative", "inform")
        message.body = jsonpickle.encode(self.agent.myinfo)
        await self.send(message)


class SubscribeSensor(OneShotBehaviour):
    async def run(self):
        info=self.agent.myinfo
        print(info.getjid())
        message = Message(to=f"sensor{info.getroad()}@{self.agent.XMPP}")
        message.set_metadata("performative", "inform")
        message.body = jsonpickle.encode(self.agent.myinfo)
        await self.send(message)


class CarPassing(OneShotBehaviour):
    async def run(self):
        info=self.agent.myinfo
        print(info.getjid())
        message = Message(to=f"sensor{info.getstart()}@{self.agent.XMPP}")
        message.set_metadata("performative", "request")
        message.body = jsonpickle.encode(self.agent.myinfo)
        await self.send(message)




