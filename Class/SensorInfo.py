class SensorInfo:
    def __init__(self,road,colour,time,nafila,jid):
        self.road=road
        self.colour=colour
        self.nafila=[]
        self.time=time
        self.jid=jid

    def getroad(self):
        return self.road

    def getcolour(self):
        return self.colour

    def getjid(self):
         return self.jid

    def gettime(self):
        return self.time

    def getnafila(self):
       return self.nafila
    def setroad(self,road):
         self.road=road

    def setcolour(self,colour):
         self.colour=colour

    def settime(self,time):
         self.time=time

    def addnafila(self,car):
        self.nafila.append(car)

    def emptyfila(self):
        self.nafila=[]

    def tostring(self):
        return (" Estrada "+str(self.road) +"| Cor Atual :"+str(self.colour)+"| ID:"+str(self.jid)+"Time:"+str(self.time))