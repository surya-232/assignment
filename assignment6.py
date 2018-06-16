#enter ten values
print("question1")
print("enter the ten values")
for i in range(10):
   x=int(input("enter your number"))
   d=x
print(d)
print("\n")

#infinite loop
print("question2")
i=1
while i<10:
  print("hello world")
  
print(i)  
print("\n")

print("question3")


#list square

l = []
s = []

for x in range(3):
	l.append(int(input("Enter a number: ")))

for x in l:
		s.append(x**2)

print(l)
print(s)





print("\n")


print("question4")
#seprate the list of string, int and float
list = []
for x in range(0, 3):
    x = int(input("enter numbers"))
    list.append(x)
for x in range(3, 6):
    x = input("enter strings")
    list.append(x)
for x in range(6, 9):
    x = float(input("enter floats"))
    list.append(x)
print(l)
a = []
b = []
c = []
for x in l:
    if type(x) == int:
        a.append(x)
    elif type(x) == str:
        b.append(x)
    elif type(x) == float:
        c.append(x)
print(a)
print(b)
print(c)

print("\n")

	
print("question5")
#range of even and odd
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
       even.append(i)
    else:
        odd.append(i)
print(even,"\n",odd)		


print("question6")
#print the pattern 
i = 1
while (i <= 10):
    j = 1
    while (j <= i):
        print("*", end="")
        j = j + 1
    i = i + 1
    print()
print("\n")	
print("question7")
#user define dictonary
d = {}
for x in range(5):
    keys = int(input("enter the keys"))
    values = input("enter value items")
    d[keys] = values
print(d)
print("\n")
print("question8")
#list input search delete

l = []
flag = 0
for x in range(5):
    x = int(input("enter the numbers"))
    l.append(x)
print(l)
y = int(input("select any number you want to search"))
for x in l:
    if x == y:
        l.remove(x)
        flag = 1
print(l)
if flag == 0:
    print("the number you entered is not in the list")
