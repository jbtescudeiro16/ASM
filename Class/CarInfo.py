class carinfo:
    def __init__(self,start,to,jid):
        self.start=start
        self.to=to
        self.jid=jid

    def getstart(self):
        return self.start

    def getto(self):
        return self.to

    def setstart(self,start):
         self.start=start

    def setto(self,to):
         self.to=to

    def getjid(self):
         return self.jid

    def tostring(self):
        return ("Inicio :"+str(self.start) +"| Para :"+str(self.to)+"| ID:"+str(self.jid))