#program for creat function calculate the radius of the circle
print("question1")
def area():
 x=int(input("enter the radius"))
 area=3.14*x*x
 print(area)
area()
print("\n")
#program for perfect() function


print("question2")
def perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum = sum + i
    if sum == n:
        return True
    else:
        return False
for i in range(i):
    if perfect(i):
        print(i)
print("\n")

#Print multiplication table of 12 using recursion.
print("question3")
def table(n,i):
  print (n*i)
  i=i+1
  if i<=10:
    table(n,i)
table(12,1)
print("\n")

 #Write a function to calculate power of a number raised to other ( a^b ) using recursion.
print("question4")
def power(a,b):
  if b == 1:
    return a
  else:
    return a*power(a,b-1)
print (power(6,2))
print("\n")
print("question5")
#Write a function to find factorial of a number but also store the factorials calculated in a dictionary

def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
c=factorial(n)
l="output"
d={}
d[l]=c
print(d)
print("\n")