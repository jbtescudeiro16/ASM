import json
import time

import pyfiglet

from Agents.Boat import *
from  Agents.CaisManager import *
from Agents.LightHouse import *
from Agents.MarinePolice import *
from colorama import init, Fore
from Behaviours.chooserandcais import *
from Behaviours import askParkPermission

class Marine:
    def runMarine(self):
        f = open("settings.json")
        conf = json.load(f)
        if conf["leaving"] > conf["cais"] + conf["descargas"]:
            print(
                "Conf file is not well defined.",
                "red")
        else:
            print("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Agentes e Sistemas Multiagente%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            text = pyfiglet.figlet_format("Porto de Leixoes", font="big")
            print(text)

            text = pyfiglet.figlet_format("Eduardo Rocha | João Escudeiro | Hugo Martins", font="small")
            print(" Grupo 2- Eduardo Rocha | João Escudeiro | Hugo Martins")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

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
            print("Agent Lighthouse Started |"+lighthousejid)
            #lighthouse.web.start(hostname="127.0.0.1", port="8080")


            marinepolicejid="marinepolice"+jid
            marinepolice = Marine_Police(marinepolicejid, pwd)
            marinepolice.set("jid", marinepolicejid)
            marinepolice.set("lighthouse",lighthousejid)
            marinepolice_res = marinepolice.start()
            marinepolice_res.result()
            print("Agent MarinePolice Started |" + marinepolicejid)

            caismanagerjid = "caismanager" + jid
            caismanager = CaisManager(caismanagerjid, pwd)
            caismanager.set("jid", caismanagerjid)
            rescais=caismanager.start(auto_register=True)
            rescais.result()

            lighthouse.set("caismanager",caismanagerjid)
            print("Agent CaisManager Started |" + caismanagerjid)


            for i in range(nr_boats):

                boat_jid = f'boat{i}{jid}'
                boat = Boat(boat_jid, pwd)
                boat.set("jid", boat_jid)
                boat.set("lighthouse", lighthousejid)
                if i < 6:
                    boat.set("status", "permission2Park")
                    #boat.set("status", "permission2Leave")

                #else:
                #boat.set("status", "permission2Leave")

                boats[f'boat{i}'] = boat
                boat.start()

                if boat.get("status") == "permission2Leave":
                    while boat.get("type") == None:
                        time.sleep(1)
                    print(boat.get("type"))
                    print("DescargasOccupied"+str(lighthouse.get("DescargasOccupied")))
                    print("CaisOccupied"+str(lighthouse.get("CaisOccupied")))
                    if boat.get("type")=="Private":
                            if lighthouse.get("CaisOccupied")== lighthouse.get("CaisTotal"):
                                lista = ["Passenger Transport", "Cargo Transport"]
                                random_element = random.choice(lista)
                                boat.set("type",random_element)
                                aux=lighthouse.get("DescargasOccupied")
                                lighthouse.set("DescargasOccupied",aux+1)
                                print(lighthouse.get("DescargasOccupied"))
                            else :
                                aux= lighthouse.get("CaisOccupied")
                                lighthouse.set("CaisOccupied",aux+1)
                    elif boat.get("type")=="Passenger Transport" or  boat.get("type")=="Cargo Transport" :
                        if lighthouse.get("DescargasOccupied")== lighthouse.get("DescargasTotal"):
                            boat.set("type","Private")
                            aux = lighthouse.get("CaisOccupied")
                            lighthouse.set("CaisOccupied", aux + 1)

                        else:
                            aux = lighthouse.get("DescargasOccupied")
                            lighthouse.set("DescargasOccupied", aux + 1)
                    behav1=AddTOrandCais()
                    boat.add_behaviour(behav1)
                elif boat.get("status") == "permission2Park":
                    while boat.get("type") == None:
                        time.sleep(1)
                    print(boat)
                    permission2Park = Permission2Park()
                    boat.add_behaviour(permission2Park)


            print("####################################################################################")
            while lighthouse.is_alive():
                time.sleep(2)
        except KeyboardInterrupt:
            for id, p in boats.items():
                print(id)
                p.stop()
            caismanager.stop()
            lighthouse.stop()
            lighthouse.results()
            print("Agents finished")

if __name__ == "__main__":
    marine= Marine()
    marine.runMarine()
