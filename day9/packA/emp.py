class Employee:
    def __init__(self, eid,ename, salary):
        self.eid = eid
        self.name = ename
        self.salary = salary
    def displayemp(self):
        print(self.eid,self.name,self.salary)