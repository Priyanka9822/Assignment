class emp:
    count=1
    def __init__(self,name,sal):
        emp.count+=1
        self.id=emp.count
        self.NAME=name
        self.SALARY=sal
    def showdata(self):
        print("EMP ID:{0}".format(self.id))
        print("EMP NAME:{0}".format(self.NAME))
        print("SALARY:{0}".format(self.SALARY))