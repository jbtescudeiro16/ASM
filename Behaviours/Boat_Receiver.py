from spade.behaviour import CyclicBehaviour

class Boat_Receiver(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:

            if msg.get_metadata("performative") == ("inform"):
                cais = msg.body
                self.agent.set("cais", cais)
                print("\033[92mDefini o meu cais no barco:" + str(self.agent.jid) + "\033[0m")
                print("Agora estou em : "+ self.agent.get("cais"))
