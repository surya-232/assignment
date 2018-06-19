#q1 What is Time Tuple?

print("question1")
import time

print(time.gmtime(0))
print("\n")
#method2
import time

print(time.localtime(0))
print("\n")

#q2  Write a program to get formatted time.
print("question2")
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time is", localtime)
print("\n")



#q3 Extract month from the time.
print("question3")
from datetime import datetime

now=datetime.now()

print("month",now.strftime("%B"))
print("\n")

#q4 Extract day from the time.

print("question4")
from datetime import datetime

now=datetime.now()

print("day",now.strftime("%A"))
print("\n")


#q5 Extract date (ex : 11 in 11/01/2021) from the time.
print("question5")

import datetime

d= datetime.date.today()
print(d)
print(d.day)
print("\n")

#q6 Write a program to print time using localtime method.
print("question6")
import time

print(time.asctime(time.localtime()))
print("\n")

#q7 Find the factorial of a number input by user using math package functions.
print("question7")
import math

n=int(input("enter the number whose factorial you want to calculate:"))

print("answer is:",math.factorial(n))
print("\n")

#q8 Find the GCD of a number input by user using math package functions.
print("question8")
import math

n=int(input("enter the first number:"))
p=int(input("enter the second number:"))

print("result:",math.gcd(n,p))
print("\n")

#q9 Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.
print("question9")
import os

print("current working directory:",os.getcwd())
print("environment variables are:",os.environ)
print("\n")