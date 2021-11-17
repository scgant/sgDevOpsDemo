'''x=10
if(x==10):
    print("Value of x is ",x)
#runtime error
number=int(input("Enter a number: "))
if (number<10 or number>20):
        print ("The entered number is: ", number)

num1=float(input("Enter a number: "))
num2=int(input("Enter 2nd number: "))
print(num1/num2)
'''
'''try:
    num1=float(input("Enter a number: "))
    num2=int(input("Enter 2nd number: "))
    print(num1/num2)
except:
    print("An exception handled")
    print("Because you divided by 0")
    print("Can't divide by 0")

try:
    print(x)
except Exception as e:
    print(e)
    print("variable x is not defined")
except NameError:
    print("something else went wrong")
'''
try:
    print(steve)
except Exception as joe:
    print(joe)
    
import os
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    os._exit(0)
    print(num1/num2)
except ZeroDivisionError:
    print("do not divide by zero")
except ValueError as msg:
    print("please input numbers only")
    print("ValueErrorDescription",msg)
finally:
    print("This program contains ZeroDivisonError")
    print("Also ValueError exception")
    
