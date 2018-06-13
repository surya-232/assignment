print("question1")
print("enter the list items")
list=[]
x=input("1")
y=input("2")
z=input("3")
print("the list is")
list=[x,y,z]
print(list)
print("\n")

print("question2")
#['google','apple','facebook','microsoft','tesla']
list2=['google','apple','facebook','microsoft','tesla']
print(list2)
print(list.extend(list2))
print(list)
print("\n")

print("question3")

print(list.count('1'))
print("\n")

print("question4")
l=[2,4,3,1,6]
print(l)
print(l.sort())
print(l)
print("\n")

print("question5")
list3=[1,2,4,3,5]
print(list3)
list4=[6,8,7,9,0]
print(list4)
list3.sort()
list4.sort()
print(list3)
print(list4)
print("\n")
tdlist=[list3,list4]
print(tdlist)
print("\n")

print("question6")
print("stack")
list5=["I","me","myself"]
print(list5)
list5.append("attitude")
list5.append("Ego")
print(list5)
print(list5.pop())
print(list5)
print(list5.pop())
print(list5)
print("\n")
print("queue")
from collections import deque
list6 = deque(["three", "five", "four", "long"])
print(list6)
list6.append("two")
print(list6)
list6.append("one")
print(list6)
print(list6.popleft())				 
print(list6.popleft())				 
print(list6)

print("\n")

print("questio7")
x=int(input("enter any number"))
if(x%2==0):
   print("the number is even")
else:
    print("the number is odd")   
