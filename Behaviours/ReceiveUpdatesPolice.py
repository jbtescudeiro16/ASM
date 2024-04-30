from spade.behaviour import CyclicBehaviour
from spade.message import Message
from termcolor import colored


class PoliceReceive(CyclicBehaviour):

    async def on_start(self):
        self.counter = 0

    async def run(self):
        msg = await self.receive()
        if msg:
            msg.get_metadata('performative')=="inform"

            print("\033[34m" + "*" * 188 + "\033[0m")


            body = msg.body.split(" \n ")
            for b in body:
                b = b.split("> ")

                if b[0] == "Boats In Operation":
                    new_b = b[1].split(" $ ")
                    print("\033[1;34m" + b[0] + ": \n" + "\033[0m")
                    if b[1]:
                        for item in new_b:
                            print(item)
                    else:
                        print("    Empty\n")
                elif b[0] == "Marine Queue":
                    new_b = b[1].split(" $ ")
                    print("\033[1;34m" + ": \n"+"\033[0m")
                    if b[1]:
                        for item in new_b:
                            print(item)
                    else:
                        print("    Empty\n")
                else:
                    print("\033[1;34m" + b[0] + ": " + "\033[0m" + b[1] + "\n")



            # print(msg.body)
            print("\033[34m" + "*" * 188 + "\033[0m")
            self.counter += 1
