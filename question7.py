class Example:
    def __init__(self,enumber,ename,esalary,ecity):
        self.enumber=enumber
        self.ename=ename
        self.esalary=esalary
        self.ecity=ecity
    def information(self):
        print ("Employee Number is: ", self.enumber)
        print ("Employee name is: ", self.ename)
        print ("Employee salary is: ", self.esalary)
        print ("Employee city is: ", self.ecity)
        print('*'*25)
object=Example(101, "John",1000,"California")
object.information()
object=Example(102, "Mark",1000,"SanDiego")
object.information()
object=Example(103, "Debojith",1000,"Chicago")
object.information()
object=Example(104, "Anna",1000,"Seattle")
object.information()


'''
    7. A class constructed by Employee and four class variables
    enumber, ename, esalary and ecity. Using class
    constructor (def __init__(self)), obtain below output
        101, ‘John’,1000,’California
        102, ‘Mark’,1000,’SanDiego
        103, ‘Debojith’,1000,’Chicago
        104, ‘Anna’,1000,’Seattle
        '''
