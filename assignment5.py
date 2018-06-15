print("question1")
year=int(input("Enter the year:"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("not a leap year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("not a leap year")
print("\n")
print("question2")
x=int(input("Enter the length:"))
y=int(input("Enter the Breadth:"))
if x==y:
    print("Square")
else :
    print("Rectangle")
print("\n")
print("question3")
x=int(input("Enter the age of person x:"))
y=int(input("Enter the age of person y:"))
z=int(input("Enter the age of person z:"))
if x>y:
    if x>z:
        print("x is older")
    else:
        print("z is older")
else:
    if y>z:
        print("y is older")
    else:
        print("z is older")
print("\n")
print("question4")
a=int(input("Enter the points:"))
f=1
if a<200:
    if 1<a<50:
        f=0
        print("No Prize")
    elif 50<a<150:
        prize="Wooden Box"
    elif 150<a<180:
        prize="Book"
    elif 180<a<200:
        prize="Chocolate"
    if f!=0:
        print("Congratulations! You won a {}".format(prize))
print("\n")

print("question5")
n=int(input("Enter the n units:"))
p=n*100
if p>1000:
    disc=p*.1
    r=p-disc
    print('Total price=',r)
print("\n")