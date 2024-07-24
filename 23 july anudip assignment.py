print("line 1")
print("line 2")
print("line 3")
print("line 4")
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
try:
    print(num1/num2)
    print("line 5")
except ZeroDivisionError as e:
    print(e)
print("***********************************************")
#num1=int(input("enter an integer:"))
#num2=int(input("enter an integer:"))
try:
    num1=int(input("enter an integer:"))
    num2=int(input("enter an integer:"))
    print(num1/num2)
except ValueError as e:
    print(e)
