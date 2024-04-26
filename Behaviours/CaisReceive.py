import jsonpickle
from spade.message import  *
from spade.behaviour import *
from TPMarina.Class.Message import *


class CaisReceive(CyclicBehaviour):


    async def run(self):
        msg = await self.receive()
        if msg:
            if msg.get_metadata("performative") == ("request"):
                #print("REcebi msg no cais ")
                aux = jsonpickle.decode(msg.body)
                if aux.get_type()=="FreePark?":
                    channels= aux.get_channels()
                    cleanchannels = {}
                    for c in channels:
                        id_c, xy = c
                        cleanchannels[id_c] = xy

                    id_channel, available = self.agent.closest_available(aux.get_boatinfo().get_type(), aux.get_boatinfo().get_jid(), cleanchannels)

                    if available == None:
                        available = "All Cais Occupied"
                        a2=Message_Info(available,aux.get_boatinfo())
                    else:

                        available = str(available) + " & " + id_c
                        #print("Available")
                        #print(available)
                        a2 = Message_Info(available, aux.get_boatinfo())

                    response = Message(to=str(msg.sender))
                    response.body = jsonpickle.encode(a2)
                    response.set_metadata("performative", "confirm")
                    await self.send(response)

                if aux.get_type() == "ADD2RANDCAIS":

                  cais = self.agent.add_boattocais(aux.get_boatinfo())
                  resp = Message(to=str(msg.sender))

                  resp.set_metadata("performative", "confirm")
                  resp.body=jsonpickle.encode( Message_Info(f"Beginning Cais & {cais}",aux.get_boatinfo()))
                  await self.send(resp)

            if msg.get_metadata("performative") == ("inform"):
                aux=jsonpickle.decode(msg.body)
                type=aux.get_type()
                if type=="BOAT_UNDOCKING":
                    self.agent.clearcais(aux.get_boatinfo())

