# variables in python 
#Syntax for Variable Assignment:
a=10
b=20

x=5 # Assigning an integer value to the variable x
y="Hello"  # Assigning a string value to the variable y


name="nisarga"
is_switch_on=True
print(a)
print(b)
print(a+b)

print("a")
print("b")

print(name)
print(is_switch_on)

# Assigning Values to Multiple Variables
a,b,c=10,20,30
print(a)
print(b)
print(c)
# assign the same value to multiple variables 
a=b=c=100
print(a)
print(b)
print(c)

#Variable Naming Rules:
# Variable names can contain letters (a-z, A-Z), numbers (0-9), and underscores (_).

string="hello world"
_college="ait"
_123="123"
print(string)
print(_college)
print(_123)

# Variable names must start with a letter or an underscore.

_animal="dog"
language="python"
_1name="computer"
print(_animal)
print(language)
print(_1name)

# Variable names are case-sensitive
Name="hello world"
name="HELLO WORLD"
print(name)
print(Name)

# . Data Types in Python
name="nisarga" # string
age =20 # int 
is_student=True # bool
weight=50.0 # float
print(name)
print(age)
print(is_student)
print(weight)

#Type Checking:
print(type(name))
print(type(age))
print(type(is_student))
print(type(weight))

# Type Conversion
is_student="yes"
print(is_student)
print(type(is_student))

age =20
age_float=float(age)
print(age_float)


s="100"
age=20
print(int(s)+age) # converting string to int and adding it to age
print(str(age)+s) # converting int to string and concatenating it with s

x="10"
y=int(x)
z=float(y)
print(x)
print(y)
print(z)

#Variable Reassignment
x=10
print(x)
x=20 #Variable Reassignment
print(x)

#  Arithmetic Operators
a=10
b=3
print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) # Floor Division
print(a%b) # Modulus
print(a**b) # Exponentiation

print((a+b-a+b*a/b)) 
print(a+b*a**b/(a-b)/a)

# Swapping Variables using a temporary variable
a=100
b=300
temp =b
b=a
a=temp
print(a)
print(b)

# swapping variables without using a temporary variable
a=10
b=30
a,b=b,a
print(a)
print(b)