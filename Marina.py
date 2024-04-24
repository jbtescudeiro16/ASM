import json
import time
from Agents.Boat import *
from  Agents.CaisManager import *
from Agents.LightHouse import *
from colorama import init, Fore


class Marine:
    def runMarine(self):
        f = open("settings.json")
        conf = json.load(f)
        if conf["leaving"] > conf["cais"] + conf["descargas"]:
            print(
                "Conf file is not well defined.",
                "red")
        else:
            text = ("MARINE")
            print(text)

        pwd = conf["pass"]
        jid = conf["jid"]
        boats = {}

        nr_boats = 10

        try:


            lighthousejid = "lighthouse" + jid
            lighthouse = LightHouse(lighthousejid, pwd)
            lighthouse.set("jid", lighthousejid)
            res_lighthouse = lighthouse.start()
            res_lighthouse.result()
            #lighthouse.web.start(hostname="127.0.0.1", port="8080")

            caismanagerjid = "caismanager" + jid
            caismanager = CaisManager(caismanagerjid, pwd)
            caismanager.set("jid", caismanagerjid)
            rescais=caismanager.start(auto_register=True)
            rescais.result()

            lighthouse.set("caismanager",caismanagerjid)


            for i in range(nr_boats):

                boat_jid = f'boat{i}{jid}'
                boat = Boat(boat_jid, pwd)
                boat.set("jid", boat_jid)
                boat.set("lighthouse", lighthousejid)
                if i < 3:
                    boat.set("status", "permission2Park")
                else:
                    boat.set("status", "permission2Leave")

                boats[f'boat{i}'] = boat
                boat.start()

                print(boat)
                if boat.get("status") == "permission2Leave":
                    while boat.get("Type") == None:
                        time.sleep(1)
                    type = boat.get("type")
                    print("TYPE Boat: ", type)

            print("####################################################################################")

        except KeyboardInterrupt:
            for id, p in boats.items():
                print(id)
                p.stop()
            caismanager.stop()
            print("Agents finished")

if __name__ == "__main__":
    marine= Marine()
    marine.runMarine()
