import time
from Agents.Car import *
from Agents.Traffic_Light import *
from Agents.Manager import *
from  Agents.Sensor import *
from  Behaviours.SendRequests import *

PASSWORD = "NOPASSWORD"
XMPP = "jbtescudeiro16-vivobook-asuslaptop-x1605za-f1605za"

if __name__ == "__main__":

    manager_agent = ManagerAgent(f"manager@{XMPP}", f"{PASSWORD}")
    manager = manager_agent.start(auto_register=True)
    manager.result()


    semaforos = ["A1","A2","B1","B2","C1","C2","D1","D2"]

    for i in semaforos:
        sensor = SensorAgent(f"sensor{i}@{XMPP}", f"{PASSWORD}")  # Adjust JID based on the iteration
        t = sensor.start(auto_register=True)
        t.result()

    for i in semaforos:
        semafor = Light_Agent(f"Semaforo{i}@{XMPP}", f"{PASSWORD}")  # Adjust JID based on the iteration
        t = semafor.start(auto_register=True)
        t.result()

    print("####################################################################################")
    """
        num_carros = 5
    
        for i in range(num_carros):
            car = CarAgent(f"car{i + 1}@{XMPP}", f"{PASSWORD}")  # Adjust JID based on the iteration
            t = car.start(auto_register=True)
            t.result()
    """
    while (manager_agent.is_alive()):
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            sensor.stop()
            semafor.stop()
            #car.stop()
            manager_agent.stop()
            break