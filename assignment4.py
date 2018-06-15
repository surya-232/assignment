
print("question1")
# An empty tuple
empty_tuple = ()
print (empty_tuple)

# Creating non-empty tuple
tup = ('jai', 'ho')
print(tup)
print("\n")
# Code for printing the length of a tuple
 
tuple2 = ('jai', 'ho')
print(len(tuple2))

print("question2")
tuple3 =(45, 70, 36)
print ("Max value element : ", max(tuple3))
print("\n")
tuple4=(45, 70, 36)
print ("Min value element : ", min(tuple4))
print("\n")\

print("question3")
def pro(t):
    r=1
    for i in t:
        r=r*i
    return r
t=(1,2,3,4)
p=pro(t)
print(p)
print("\n")









print("SET")
print("enter the value of set")
a=input("1.")
b=input("2.")
c=input("3.")
s1=set([a,b,c])
print(s1)
print("enter the value of set")
x=input("1.")
y=input("2.")
z=input("3.")
s2=set([x,y,z])
print(s2)
print("\n")
print("difference")
print(s1-s2)
print("\n")
print("compare")
print("\n")
print("intersection")
print(s1 & s2)

print("\n")

print("dictonary")
print("dictonary to store name")
d={}
for i in range (10)
   name=input("enter your name")
   marks=int(input("enter your number"))
   d[name]=marks
print(d)

print("question2")

print("\n")
print("question3")
#7.Sorting of Dictionary
d={'a':60,'b':100,'c':80}
print(d)
value_list=list(d.values())
print(value_list)
value_list.sort()
print(value_list)
print("\n")
print("question4")
l=list("MISSISSIPPI")
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['P']=l.count('P')
print(d)