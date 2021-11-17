class Question5:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def method(self):
        print("my firstname is: ",self.fname)
        print("my lastname is: ",self.lname)
    def triangle1(self,num1,num2):
        print("The area of rectable1 is: ", num1*num2)
    def triangle2(self,num1,num2):
        print("The area of rectable1 is: ", num1*num2)
    def triangle3(self,num1,num2):
        print("The area of rectable1 is: ", num1*num2)
    def triangle4(self,num1,num2):
        print("The area of rectable1 is: ", num1*num2)
    def triangle5(self,num1,num2):
        print("The area of rectable1 is: ", num1*num2)
Object=Question5('Steve','Gant')
Object.triangle1(12,10)
Object.triangle2(14,12)
Object.triangle3(16,14)
Object.triangle4(18,16)
Object.triangle5(20,18)
