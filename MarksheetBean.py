class MarksheetBean():
    rollNo = 0
    name = ""
    phy = 0
    chem = 0
    maths = 0

    def setRollNo(self, rollNo):
        self.rollNo = rollNo

    def getRollNo(self):
        return self.rollNo

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPhy(self, phy):
        self.phy = phy

    def getPhy(self):
        return self.phy

    def setChem(self, chem):
        self.chem = chem

    def getChem(self):
        return self.chem

    def setMaths(self, maths):
        self.maths = maths

    def getMaths(self):
        return self.maths
