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
                if aux.get_type()=="ParkPermission":
                    print("Recebi um pedido para estacionar um barco no farol")
                    pl_info = aux.get_boatinfo()
                    #print(pl_info)
                    empty_channels=self.agent.getemptychannels()


                    if len(empty_channels) > 0:
                        if pl_info.get_type() == "Private":
                            if self.agent.get("CaisOccupied") < self.agent.get("CaisTotal"):
                                print(f"Permission to park conceded - {str(msg.sender)}")
                                permission = Permission_Cais(pl_info, empty_channels)
                                self.agent.add_behaviour(permission)
                        else:
                            if self.agent.get("DescargasOccupied") < self.agent.get("DescargasTotal"):
                                print(f"Permission to unload conceded - {str(msg.sender)}")
                                permission = Permission_Cais(pl_info, empty_channels)
                                self.agent.add_behaviour(permission)
                elif aux.get_type()=="ADD2RANDCAIS":
                    msg2 = Message(to=self.agent.get("caismanager"))
                    msg2.body = msg.body
                    msg2.set_metadata("performative", "request")
                    await self.send(msg2)


                elif aux.get_type()=="MARINEINFO":
                    #print("pediram-me marineinfo no farol")

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

                    reply_msg.body = f"Cais Privados> {self.agent.get('CaisTotal')} \n Cais Occupied> {self.agent.get('CaisOccupied')} \n Commercial Cais > {self.agent.get('DescargasTotal')} \n Commercial Cais Occupied> {self.agent.get('DescargasOccupied')} \n Airport Queue> {queue} \n Boats In Operation> {info_channels}"
                    reply_msg.set_metadata("performative", "inform")
                    #print("respondi")
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

                    res = Message(to=aux.get_boatinfo().get_jid())
                    res.body = f"{cais}"
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




