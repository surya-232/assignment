# Write a Python program to read last n lines of a file
print("question1")
f=open("f1.txt",encoding="utf8")
content=f.readlines()
# print(content)
f.close()
n=int(input("enter the last line number from where u want to read: "))
while n>0:
 print(content[-n])
 n=n-1

print("question2")
#  Write a Python program to count the frequency of words in a file.

words = open("f1.txt", "r", encoding="utf8").read().split()
print(words)
print(type(words))
uniqWords = sorted(set(words))
print(type(uniqWords))
for word in uniqWords:
    print(words.count(word), word)
print("question3")
# Write a Python program to copy the contents of a file to another file

with open("file1.txt","r",encoding="utf8") as f1:
 with open("file2.txt","w") as f2:
  for line in f1:
   f2.write(line)

print("question4")
# Write a Python program to combine each line from first file with the corresponding line in second file.

with open("file3.txt","r",encoding="utf8") as f1:
   with open("file4.txt","r") as f2:
     for line1,line2 in zip(f1,f2):
       print(line1+line2)

print("question5")
# Write a Python program to write 10 random numbers into a file.
#  Read the file and then sort the numbers and then store it to another file.

import random

with open("file5.txt", "w") as f:
    for i in range(10):
        numbers = str(random.randint(1, 100))
        f.writelines(numbers + '\n')
        print(numbers)

with open("file5.txt") as f1, open("file6.txt", "w") as f2:
    numbers = f1.read().split()
    numbers.sort()
    print(numbers)
    for n in numbers:
        f2.write(n)
        f2.write("\n")