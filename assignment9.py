#creat a class of area and circumference of circle
print("question1")


class Circle():
    def __init__(self, r):
        self.radius = r

    def getarea(self):
        return self.radius ** 2 * 3.14

    def getcircumference(self):
        return 2 * self.radius * 3.14


NewCircle = Circle(int(input("enter the radius")))
print("the area is:",NewCircle.getarea())
print("the circumference is:",NewCircle.getcircumference())
print("\n")

#display the student details
print("question2")
class student():
    def __init__ (self,name,rollno):
       self.name = name
       self.rollno = rollno
    def show(self):
        print(self.name,self.rollno)
rollno=int(input("enter roll number"))
name=(input("enter name"))
s1=student(rollno,name)
s1.show()
print("\n")

#temp. converter
print("question3")
class temperature:
    def convert_Fahrenheit(self):
        c_temp=int(input("enter the temprature in celcious"))
        print(c_temp,"C")
        print("temprature in Fahrenheit:",(c_temp*1.8)+32,"F")
    def convert_Celcius(self):
        f_temp=int(input("enter the temprature in fahrenheit"))
        print(f_temp,"F")
        print("temprature in celcius:",(f_temp-32)/1.8,"C")
obj=temperature()
obj.convert_Fahrenheit()
obj.convert_Celcius()
print("\n")

#movie details
print("question4")
class MovieDetails():
    def __init__ (self,movie_name,artist_name,releasing_date,ratings):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.releasing_date=releasing_date
        self.ratings=ratings

    def update(self, movie_name, artist_name, releasing_date, ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.releasing_date = releasing_date
        self.ratings = ratings

    def show(self):
         print(self.movie_name,self.artist_name,self.ratings,self.releasing_date)
movie_name=input("enter movie name")
artist_name=input("enter artist name")
ratings=int(input("enter the ratings out of 5"))
releasing_date=input("enter releasing date")
s1=MovieDetails(movie_name,artist_name,ratings,releasing_date)
s1.show()
s1.update("abcd","dance","5","1999")
s1.show()
print("\n")

#expenditure
print("question5")
class expenditure():
    def __init__(self,exp,save):
        self.exp=exp
        self.save=save
    def totalsalary(self):
        t=self.exp+self.save
        return t
    def salary(self,b):
        self.b=b
        print(self.b)
exp=2000
save=3000
obj=expenditure(exp,save)
a=obj.totalsalary()
obj.salary(a)