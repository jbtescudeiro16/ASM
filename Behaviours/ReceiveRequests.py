
import jsonpickle
from spade.behaviour import CyclicBehaviour
from spade.message import Message


"""
class ManagerStart(PeriodicBehaviour):
    async def run(self):

        if self.agent.semaforos :
            print("comecei luzes")
            letra=random.choice(["A","B","C","D"])
            message = Message(to=f"semaforo{letra}1@{self.agent.XMPP}")
            message.set_metadata("performative", "inform")
            print("começa o verde em 1"+letra)
            await self.send(message)
            message2 = Message(to=f"semaforo{letra}2@{self.agent.XMPP}")
            message2.set_metadata("performative", "inform")
            print("começa o verde em 2" + letra)
            await self.send(message2)
        else:
            print(" n comecei luzes")
"""
class ReceiveRequestsBehaviourMan(CyclicBehaviour):
    def countoccor(self,letra, lista):
        count = 0
        for elem in lista:
            if elem.getroad()[0] == letra:
                count += 1
        return count
    async def run(self):

        msg = await self.receive(timeout=5)
        if msg:
            if msg.get_metadata("performative") == ("inform"):
                print("Recebi um inform do Semaforo no manager")
                self.agent.semaforos.append(jsonpickle.decode(msg.body))
                if (self.agent.flag==False):
                    print("ainda nao comecei")
                    for i in self.agent.semaforos:
                        if self.countoccor(i.getroad()[0],self.agent.semaforos)==2:
                         self.agent.flag=True
                         letra=i.getroad()[0]
                         print("Vou comecar o verde em "+letra)
                         message = Message(to=f"semaforo{letra}1@{self.agent.XMPP}")
                         message.set_metadata("performative", "inform")
                         print("começa o verde em 1" + letra)
                         await self.send(message)
                         message2 = Message(to=f"semaforo{letra}2@{self.agent.XMPP}")
                         message2.set_metadata("performative", "inform")
                         print("começa o verde em 2" + letra)
                         await self.send(message2)
                else:
                    print("ja comecei")



class ReceiveRequestsBehaviourSensor(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=5)
        if msg:
            if msg.get_metadata("performative") == ("inform"):
                self.agent.semaforo=(jsonpickle.decode(msg.body))
                print("Recebi um inform do Semaforo no sensor")
                print( self.agent.semaforo.getroad())


class ReceiveCarsBehaviourSensor(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=5)
        if msg:
            if msg.get_metadata("performative") == ("request"):
                print("Recebi um rquest de um carro no sensor "+self.agent.myinfo.getroad())
                if (self.agent.semaforo.getcolour()== "RED") :
                    self.agent.myinfo.addnafila(jsonpickle.decode(msg.body))
                    print("Esta rouge,"+str(len(self.agent.myinfo.getnafila()))+" ns fila DO"+self.agent.myinfo.getroad() )
                    #falta informar o manager que esta um men na fila

                elif (self.agent.semaforo.getcolour()== "YELLOW") :
                    self.agent.myinfo.addnafila(jsonpickle.decode(msg.body))
                    print("Esta amarelo,"+str(len(self.agent.myinfo.getnafila()))+" ns fila do"+self.agent.myinfo.getroad())
                    #falta informar o manager que esta um men na fila

                elif (self.agent.semaforo.getcolour()== "GREEN") :
                    print("Esta verde,"+str(len(self.agent.myinfo.getfila()))+"ignorei")
                    #falta informar o manager que esta um men na fila


