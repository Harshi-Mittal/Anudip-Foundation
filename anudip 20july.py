#count()
str="hello how r u"
oc=str.count('a',8,15)
print(oc)

print("***********************************************************************")
str="hello how r u"
oc=str.endswith("d",0,6)
print(oc)
print("***********************************************************************")
str="hello how r u"
oc=str.endswith(" ",0,6)
print(oc)
print("***********************************************************************")
str="welcome to python class"
str2=str.find("p")
print(str2)
str2=str.find("c",9,14)
print(str2)
print("***********************************************************************")
str="welcome to python class"
str2=str.isalnum()
print(str2)
str="harshi."
str2=str.isalpha()
print(str2)
str="6767@"
str2=str.isnumeric()
print(str2)
print("***********************************************************************")
str="py8thon"
if str.isalpha()==True:
    print("string contains alphabet")
else:print("string contains others characters too")
print("***********************************************************************")
str="welcome to python class"
str2=str.upper()
print(str2)
str2=str.isupper()
print(str2)
str2=str.lower()
print(str2)
str2=str.islower()
print(str2)
print("***********************************************************************")
string="HARSHI MITTAL"
str=string.isupper()
print(str)
print("***********************************************************************")
str="-------------harshi___________"
str2=str.lstrip("-")
print(str2)
print("***********************************************************************")
str="-------------harshi----------------"
str2=str.rstrip("-")
print(str2)
print("***********************************************************************")
str="python is a programming language"
str2=str.replace("python","java")
print(str2)
print("***********************************************************************")
str="python LANGUAGE"
str2=str.swapcase()
print(str2)
print("***********************************************************************")
str="python LANGUAGE"
str2=str.title()
print(str2)

