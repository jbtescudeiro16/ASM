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

            color = "yellow"
            print(colored("*" * 188, color))

            body = msg.body.split(" \n ")
            for b in body:
                b = b.split("> ")

                if b[0] == "Boats In Operation":
                    new_b = b[1].split(" $ ")
                    print(colored(b[0] + ": \n", color, attrs=["bold"]))
                    if b[1]:
                        for item in new_b:
                            print(item)
                    else:
                        print("    Empty\n")
                elif b[0] == "Marine Queue":
                    new_b = b[1].split(" $ ")
                    print(colored(b[0] + ": \n", color, attrs=["bold"]))
                    if b[1]:
                        for item in new_b:
                            print(item)
                    else:
                        print("    Empty\n")
                else:
                    print(colored(b[0] + ": ", color, attrs=["bold"]) + " " + b[1] + "\n")

            # print(msg.body)
            print(colored("*" * 188, color))
            self.counter += 1
