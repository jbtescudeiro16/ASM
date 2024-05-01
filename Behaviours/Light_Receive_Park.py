import jsonpickle
from spade.behaviour import *
from termcolor import colored

from TPMarina.Behaviours.Permission_Cais import *
from TPMarina.Behaviours.empty_queue import *


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
                    info_channels = ""
                    queue=""

                    if len(self.agent.get("Queue"))==0:
                        queue+="Empty"
                    else :
                        for barcofila in self.agent.get("Queue"):

                            info = str(
                                barcofila[1].get_id()) + " ➡️ " + barcofila[0]
                            queue += " "   + info + " $ "

                    for channel in self.agent.get("channels"):
                        if channel.get_boat() == None:
                            if channel.get_state_channel()=="Open":
                                info = "Empty"
                            elif channel.get_state_channel()=="Closed":
                                info = "Closed"
                        else:
                            info = str(
                                channel.get_boat()) + " ➡️ " + channel.get_state_boat()
                        info_channels += "    " + str(colored(channel.get_id(), "yellow")) + ". " + info + " $ "

                    reply_msg.body = f"Cais Privados> {self.agent.get('CaisTotal')}"+ " " * 130+"\033[34m Weather: \033[0m"+self.agent.get('Weather') +f" \n Cais Occupied> {self.agent.get('CaisOccupied')} \n Commercial Cais > {self.agent.get('DescargasTotal')} \n Commercial Cais Occupied> {self.agent.get('DescargasOccupied')} \n Queue> {queue} \n Boats In Operation> {info_channels}"
                    reply_msg.set_metadata("performative", "inform")
                    await self.send(reply_msg)


            elif msg.get_metadata("performative") == ("confirm"):
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

                    #print("idcanal:"+canal)

                    for i in self.agent.get("channels"):
                         if i.get_id()==canal:
                            i.set_boat(aux.get_boatinfo(),"BOAT COMING TO PARK")
                    if aux.get_boatinfo().get_type()=="Private":
                        antes=self.agent.get("CaisOccupied")
                        self.agent.set("CaisOccupied",antes+1)
                    else :
                        antes = self.agent.get("DescargasOccupied")
                        self.agent.set("DescargasOccupied", antes + 1)

                    count = self.agent.get("QueueCount")
                    self.agent.set("Queue",[i for i in self.agent.get("Queue") if i[1].get_id() != aux.get_boatinfo().get_id()])
                    self.agent.set("QueueCount", count - 1)
                    res = Message(to=aux.get_boatinfo().get_jid())
                    res.body=jsonpickle.encode( Message_Info(f"PARKCONCEDED&{cais}&{canal}",aux.get_boatinfo()))

                    res.set_metadata("performative", "inform")


                    await self.send(res)

            elif msg.get_metadata("performative") == ("inform"):

                aux = jsonpickle.decode(msg.body)
                tipomsg = aux.get_type()
                if tipomsg=="UNDOCKFINISHED":
                    print("Undock Confirmation received Farol: "+ aux.get_boatinfo().get_id())
                    self.agent.removeboat_channel(aux.get_boatinfo().get_id())
                    dep= self.get("Departures")
                    self.set("Departures", dep+1)
                    if len(self.agent.get("Queue"))>0:
                        behav5=EmptyQueue("UNDOCKCOMPLETED")
                        self.agent.add_behaviour(behav5)




                elif tipomsg=="PARKCOMPLETED":
                    print("ParkFinished Confirmation received Farol: "+ aux.get_boatinfo().get_id())
                    self.agent.removeboat_channel(aux.get_boatinfo().get_id())
                    dep= self.get("Arrivals")
                    self.set("Arrivals", dep+1)
                    if len(self.agent.get("Queue")) > 0:
                        behav5 = EmptyQueue("PARKCOMPLETED")
                        self.agent.add_behaviour(behav5)

            elif msg.get_metadata("performative") == ("refuse"):

                aux = jsonpickle.decode(msg.body)
                tipomsg = aux.get_type()
                if tipomsg=="NOFREECAIS":
                    print("falta tratar o no free cais no light receive park")




