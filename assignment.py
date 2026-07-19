def addition (a,b):
    print (f"{a} + {b} is", a + b)
def subtraction (a,b):
    print (f"{a} - {b} is", a - b)
def multiplication (a,b):
    print (f"{a} x {b} is", a * b)
def division (a,b):
    print (f"{a} / {b} is", a / b)
def modulus (a,b):
    print (f"{a} % {b} is", a % b)
def exponent (a,b):
    print (f"{a} ^ {b} is", a ** b)

print ("Enter number 1")
num_1 = int(input())
print ("Enter number 2")
num_2 = int(input())
addition (num_1, num_2)
subtraction (num_1, num_2)
multiplication (num_1, num_2)
division (num_1, num_2)
modulus (num_1, num_2)
exponent (num_1, num_2)

