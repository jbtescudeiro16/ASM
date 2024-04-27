import jsonpickle
from spade.behaviour import CyclicBehaviour
from termcolor import colored

from TPMarina.Behaviours.Permission_Cais import *


class ReceiveParking(CyclicBehaviour):
    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                aux=jsonpickle.decode(msg.body)
                if  aux.get_type()=="ADD2RANDCAIS":
                    msg2 = Message(to=self.agent.get("caismanager"))
                    msg2.body = msg.body
                    msg2.set_metadata("performative", "request")
                    await self.send(msg2)


                elif aux.get_type()=="MARINEINFO":
                    reply_msg = msg.make_reply()
                    queue = ""
                    info_channels = ""

                    for channel in self.agent.get("channels"):
                        if channel.get_boat() == None:
                            info = "Empty"
                        else:
                            info = str(
                                channel.get_boat()) + " ➡️ " + channel.get_state_boat()
                        info_channels += "    " + str(colored(channel.get_id(), "yellow")) + ". " + info + " $ "

                    reply_msg.body = f"Cais Privados> {self.agent.get('CaisTotal')} \n Cais Occupied> {self.agent.get('CaisOccupied')} \n Commercial Cais > {self.agent.get('DescargasTotal')} \n Commercial Cais Occupied> {self.agent.get('DescargasOccupied')} \n Queue> {queue} \n Boats In Operation> {info_channels}"
                    reply_msg.set_metadata("performative", "inform")
                    await self.send(reply_msg)


            elif msg.get_metadata("performative") == ("confirm"):
                print("recebi confirm manager")
                aux=jsonpickle.decode(msg.body)
                tipomsg=aux.get_type()

                corpo= tipomsg.split(" & ")
                if corpo[0]=="Beginning Cais":
                    cais=corpo[1]
                    answer=Message(to=aux.get_boatinfo().get_jid())
                    answer.set_metadata("performative", "inform")
                    answer.body=jsonpickle.encode(Message_Info(f"Cais& {cais}",aux.get_boatinfo()))
                    await self.send(answer)

                else :
                    cais = corpo[0].strip()
                    canal = corpo[1].strip()

                    print("idcanal:"+canal)

                    for i in self.agent.get("channels"):
                         if i.get_id()==canal:
                            i.set_boat(aux.get_boatinfo(),"BOAT COMING TO PARK")
                    if aux.get_boatinfo().get_type()=="Private":
                        antes=self.agent.get("CaisOccupied")
                        self.agent.set("CaisOccupied",antes+1)
                    else :
                        antes = self.agent.get("DescargasOccupied")
                        self.agent.set("DescargasOccupied", antes + 1)
                    res = Message(to=aux.get_boatinfo().get_jid())
                    res.body=jsonpickle.encode( Message_Info(f"PARKCONCEDED&{cais}&{canal}",aux.get_boatinfo()))

                    res.set_metadata("performative", "inform")


                    print("enviei o inform de lhe conceder o parque")
                    await self.send(res)

            elif msg.get_metadata("performative") == ("inform"):

                aux = jsonpickle.decode(msg.body)
                tipomsg = aux.get_type()
                if tipomsg=="UNDOCKFINISHED":
                    print("Undock Confirmation received Farol: "+ aux.get_boatinfo().get_id())

                    self.agent.removeboat_channel(aux.get_boatinfo().get_id())

                    dep= self.get("Departures")
                    self.set("Departures", dep+1)
                elif tipomsg=="PARKCOMPLETED":
                    print("ParkFinished Confirmation received Farol: "+ aux.get_boatinfo().get_id())
                    self.agent.removeboat_channel(aux.get_boatinfo().get_id())
                    print("limpei o canal onde estava o barco"+aux.get_boatinfo().get_id() )
                    dep= self.get("Arrivals")
                    self.set("Arrivals", dep+1)

            elif msg.get_metadata("performative") == ("refuse"):

                aux = jsonpickle.decode(msg.body)
                tipomsg = aux.get_type()
                if tipomsg=="NOFREECAIS":
                    print("falta tratar o no free cais no light receive park")




