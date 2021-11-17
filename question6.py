class Arithmatic:
    #begin constructor
    def __init__(self,ename,ename2):
        self.ename=ename
        self.ename2=ename2
    #end constructor begin creating 4 methods below
    def addition(self,num1,num2):
        print ("this is the add operation: ", num1 + num2)
    def subtraction(self,num1, num2):
        print ("this is the subtract operation: ", num1 - num2)
    def multiplication(self,num1,num2):
        print ("this is the multiplication operation: ", num1 * num2)
    def division(self,num1,num2):
        print ("this is the divide operation: ", num1 / num2)
    #end method creation...time to get output
#*******MUST call object and class first...IMPORTANT!!!!********
Object=Arithmatic('Steve','Frederick')
#End object call begin method calls next
#************NOW WE call methods next*************************

Object.addition(10,20)
Object.addition(20,30)
Object.addition(30,40)
Object.addition(40,50)
Object.addition(50,60)
Object.addition(60,70)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Object.subtraction(10,20)
Object.subtraction(20,30)
Object.subtraction(30,40)
Object.subtraction(40,50)
Object.subtraction(50,60)
Object.subtraction(60,70)
#======================================================
Object.multiplication(10,20)
Object.multiplication(20,30)
Object.multiplication(30,40)
Object.multiplication(40,50)
Object.multiplication(50,60)
Object.multiplication(60,70)
#==============================================
Object.division(10,20)
Object.division(20,30)
Object.division(30,40)
Object.division(40,50)
Object.division(50,60)
Object.division(60,70)
