print("labani")
  Labani
student = "sam"
student
  sam
student= "labani"
student 
  Labani
a1= 22

# Type
a2 = 3+4j
type (a2)
  complex

# Operators 
a=32
b=33
a+b
  56
a-b
 -1
a/b
  0.9696969696969697
a==b
  False
a!=b
  True
a= True 
b=False
b & b 
  False
a & a
  True
a|b
 True
a|a
  True

# String operations 
str1= """ this is my first string"""
str1[3]
len (str1)

str1.upper() # this is for change capital letter .
str1.lower() # this is for change small letter 
str1.replace('y','a')
string= "hello hello world"
string.count ("hello")
mystring= "hello world"
mystring.find("w")
mystring.split ("l") # split l 

# Tuple operetions
tup1= ("hsh","SD",1)
type(tup1)
tuple 
tup2 = ("labani",123)
tup2*3
('labani', 123, 'labani', 123, 'labani', 123)
tup2*3 + tup1
('labani', 123, 'labani', 123, 'labani', 123, 'hsh', 'SD', 1)
tup1 = (23,6753,82)
max(tup1)
6753

# List operation 
l1= [12,3,"e"]
type (l1)
list
l1[2]=322
l1
[12, 3, 322]
l1.reverse()
l1
[322, 3, 12]
l1.insert(1,'lal')
l1
[322, 'lal', 3, 12]
l2=["kasd","app","car","bal"]

# Dictionary Operations
d1 = {"apple": 34,"bell":22}
d1["apple"]= 99
d1
{'apple': 99, 'bell': 22}
type (d1)
dict
d1.keys()
dict_keys(['apple', 'bell'])
d1["apple"]=32
d1
d1.values()
dict_values([34, 22])

d1["apple"]=32
d1
{'apple': 32}

f1= {"a":12,"o":22,"d":121}
f2= {"dd":23,"ed":122}
f1.update(f2)
f1
{'a': 12, 'o': 22, 'd': 121, 'dd': 23, 'ed': 122}

f1= {"a":12,"o":22,"d":121}
f1.pop("a")
f1
{'o': 22, 'd': 121}

d1={"t":12,"g":43,"f": 23}
d2={"b":54,"r":6,"s":78}
d1.update(d2)
d1
{'t': 12, 'g': 43, 'f': 23, 'b': 54, 'r': 6, 's': 78}

d1.pop('g')
43

s1={1,'s',32,}
s1.update([11,'fr',43])
s1{1, 11, 32, 43, 'fr', 's'}

s1.remove(11)
s1
{1, 32, 43, 'fr', 's'}
s1
{1, 32, 43, 'fr', 's'}

s2= {2,3,4,4}
s1.union(s2)
{1, 2, 3, 32, 4, 43, 'fr', 's'}

# If Else Condition 
a= 23
b= 232
if b>a:
    print("b greater than a ")
  b greater than a 

a= 56
b= 23
c= 34
if (a>b) & (b<c):
    print("false")
elif(b<c) & (a<c):
    print("true")
else:
    print("false")
  false

tup1 = ('a','b', 23)
if 'z' in tup1:
    print("z is present in tup1")
else:
    print("z is not present in tup1")
  z is not present in tup1

l1 = ['a','b','c']
d1= {'k1':56,'k2':87,'k3':98}
if d1['k2']==87:
    d1['k2']=d1['k2']+100
  d1
{'k1': 56, 'k2': 187, 'k3': 98}

i = 1 
n= 2 
while i<= 10:
    print(n, "*" ,i ,"=", n*i )
    i = i+1
 2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18

2 * 10 = 20l1 = [1,2,3,4,5]
i=0 

while i<len(l1):
    l1[i]=l1[i]+100
    i=i+1
 l1
[101, 102, 103, 104, 105]

#Multiple task function  
def hello():
    print ("Labani")
 hello()
def hello ():
    print ('my name is Labani')
 hello ()
my name is Labani

def add (x):
    return (x+3+2)
add (15)
20
add (200)
205

def odd_even (x):
    if x%2==0:
        print ("even")
    if x%2!=0:
        print("odd")
     odd_even(23)
odd
odd_even(44)
even

g=lambda x : x*x*x
g(23)
12167
g(3)
27

# Filter Function 
final_list=list(filter(lambda y: (y%2==0),l1))
l1
[2, 45, 89, 43, 56, 124, 26, 74, 45]
final_list
[2, 56, 124, 26, 74]
l2= [12,43,22,56,21,11,33,111]

# Lamda with Map
new_final=list(map(lambda x: x*3,l2))
new_final
[36, 129, 66, 168, 63, 33, 99, 333]

# Reduce use got final result on sequence 
from functools import reduce
sum=(reduce(lambda x,y : x+y,l2)) # akhane error ache 
new_list

class phone:
    def make_call (self):
        print("phone call")
     class phone:
    def make_call (self):
        print("phone call")
     p1=phone()
p1.make_call()
phone call

#Here first parameter is self .inbuid parameter ko invoked karna hai object ke sath.
class Phone: #creating the phonr class
    def make_call(self):
        print("phone call")
     class Game:
    def game(self):
        print ("now play game")
    p2=Game() #ininitializing p2 project 
    p2.game() # invoking methods through object
now play game

class Good :
    def make_game(self):
        print("now i am playing")
    def water (self):
        print("i drinking lemon water ")
     p3=Good()
p3.water()
i drinking lemon water

class Home: # with extra parameter 
    def set_color (self,color):
        self.color=color
    def set_cost (self,cost):
        self.cost= cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost 
    def father(self):
        print("my father name is Labani Haldar,Father name is Prodip Haldar")
    def address(self):
        print("Gangarampur,Dakshin Dinajpur")
     p5= Home()
p5.father()
my father name is Labani Haldar,Father name is Prodip Haldar
p5.address()
Gangarampur,Dakshin Dinajpur
p5.set_color("blue")
p5.show_color()
'blue'
p5.set_cost(49859)
p5.show_cost()
49859

#Creating a class with constructor 
class Employee: # inint method acts as the connstructor
    def __init__(self,name,address,phone_no,age,cost):
        self.name= name
        self.address= address
        self.phone_no= phone_no
        self.age= age
        self.cost = cost
    def show_employee_details (self):
        print ("my name is ",self.name)
        print ("my address is ",self.address)
        print ("my phone_no is ",self.phone_no)
        print ("my age is ",self.age)
        print("total cost is ",self.cost)
     e1= Employee('Labani','Dakshin Dinajpur',93442,20,9000000000000)#instantiating the e1 object here with value pass
e1.show_employee_datails() #invokes the emplpoyee_details method (AKHANE AKTU ERRRO ACHE )

#inheritance 
# here one superclass and another is sub class .with inheritance one class can derive the properties of another class .
# man inheritance features from his father.
# here grandfather er jeen father . 
# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage= mileage
#         self.cost = cost

# def show_details(self):
#     print("vehicle mileage is ",self.mileage)
#     print("vehicle cost is ",self.cost)
# v1 = Vehicle (24,43533)
# v1.show_details()
class Vehicle :
    def __init__ (self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_vehicle_details(self):
        print("mileage of vehicle is ",self.mileage)
        print("cost is ",self.cost)
        print("you are vehicle")
v1= Vehicle (120,3423)
# v1.show_vehicle_details()
# class Car(Vehicle):#child class car inheritant property of the class Vehicle.
#     def show_car_details(self):
#         print("you are a car")
# c1= Car(344,3231)
# c1.show_vehicle_details()
# c1.show_car_details()
class Car(Vehicle):
    def __init__ (self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres= tyres
        self.hp = hp 
    def show_car_details(self):
        print ("car's mileage is ",self.tyres)
        print ("car hp is ",self.hp)
     c2= Car(231,421,35,1267)
c1.show_car_details()
you are a car
c2.show_car_details()
car's mileage is  35
car hp is  1267

# difference type of Inheritance 
# single inheritance 
# multiple inheritance 
# multilevel inheritance
# hybrid inheriitance

# multiple inheritance : the child inheritance from more than 1 parent class
# parent 1             parent2 
#           child 

class Parent1 ():                   #parent class one
      def assign_string_one (self,str1):
          self.str1= str1
      def show_string_one(self):
          return self.str1

class Parent2 ():
    def assign_string_two (self,str2):           #parent class two 
        self.str2= str2

    def show_string_two(self):
        return self.str2
     
     class Child(Parent1, Parent2):
    def assign_string_three (self,str3):             # child class 
        self.str3= str3
    def show_string_three(self):                #this child class is inheritance of parent 1 and paren 2.
        return self.str3
     d2= Child() # invoked the parent class 

d2.assign_string_one ("i am string of parent 1")
d2.assign_string_two ("i am string of parent 2")   
d2.assign_string_three ("i am a string odf child ")

d2.show_string_one ()
'i am string of parent 1
d2.show_string_two()
'i am string of parent 2
d2.show_string_three()
'i am a string odf child '

# in multi level inheritance ,we have parent ,child ,grand child relationship .

            # Parent 

            # Child            # relationship # Child parent se inherit kar raha hai
 
            # Grand- Child     # Grand-Child child se inherit kar raha hai 
class Parent ():
    def assign_name (self,name):
        self.name = name
    def show_details_name (self):
        return self.name

class Child(Parent):
    def assign_age (self,age):
        self.age = age 
    def show_details_age(self):
        return self.age
     class GrandChild (Child):
    def assign_gender(self,gender):
        self.gender= gender
    def show_details_gender(self):
        return self.gender
d3 = GrandChild()
d3.assign_name("my name is Labani Haldar")
d3.assign_age("my age is 20")
d3.assign_gender("Female") 

d3.show_details_name()
'my name is Labani Haldar'
d3.show_details_gender()
'Female'
d3.show_details_age ()
'my age is 20'

class Labani():
    def assign_bari(self,name):
        self.name = name 
    def show_details_bari (self):
        return self.name
     
class Shrabani(Labani):
    def assign_ghar(self,jaiga):
        self.jaiga= jaiga
    def show_details_ghar(self):
        return self.jaiga
     
 class Parama (Shrabani):
    def assign_sec(self,sec):
        self.sec= sec
    def show_details_sec (self):
        return self.sec
     
b1= Parama()

b1.assign_bari("My bari is Gangarampur")
b1.assign_ghar("chad kno asena amar ghore ")
b1.assign_sec("i am reading in class 2")

b1.show_details_sec ()
'i am reading in class 2'
b1.show_details_ghar()
'chad kno asena amar ghore '

# Python Libraries 

# Pandas-> Data manupulation  
# Numpy->  numerical 
# Matplolib-> Data visualization 

# Numpy 
# scientific computing 
# numerical python (core library)
# multidemsinonal array object and a collection of routines for processing those arrays 

import numpy as np
l1=[1,2,3]
n1= np.array(l1)
n1
array([1, 2, 3])
type (n1 )
numpy.ndarray

import numpy as np 
l2 = ([1,2,3,4],[4,3,2,1])
n2=np.array(l2)
n2
array([[1, 2, 3, 4],
       [4, 3, 2, 1]])
type(n2)
numpy.ndarray
import numpy as np 

# initialize a zeroes 

import numpy as np 
n1 = np.full((1,2),(10))
n1

array([[10, 10]])
import numpy as np 
n1= np.full((5,5),(0))
n1
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
import numpy as np
n1 = np.full((2,2),10)
n1 
array([[10, 10],
       [10, 10]])

import numpy as np 
n1 = np.full ((5,5),22)
n1
array([[22, 22, 22, 22, 22],
       [22, 22, 22, 22, 22],
       [22, 22, 22, 22, 22],
       [22, 22, 22, 22, 22],
       [22, 22, 22, 22, 22]])


# initialize Numpy array within a range 
import numpy as np 
n1 = np.arange (10,20)
n1
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

import numpy as np 
n1 = np.arange (10,50,5) 
n1
array([10, 15, 20, 25, 30, 35, 40, 45])
n1 = np.arange (50,100)
n1
array([50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
       67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
       84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])

n1 = np.arange (50,500,10)
n1
array([ 50,  60,  70,  80,  90, 100, 110, 120, 130, 140, 150, 160, 170,
       180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
       310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430,
       440, 450, 460, 470, 480, 490])

# initializing Numpy array with random numbers 
import numpy as np
n4=np.random.randint (1,100,5)
print(n4)
[95  8 70 91 85]

import numpy as np 
np.random.randint(2,20,5) #every time get different output
array([ 5, 10, 17, 11, 17])

import numpy as np 
n1 = np.array([[1,2,3,4],[2,3,5,6]])
n1
array([[1, 2, 3, 4],
       [2, 3, 5, 6]])
n1.shape
n1
array([[1, 2],
       [3, 4],
       [2, 3],
       [5, 6]])

n1.shape = (8,1)
n1
array([[1],
       [2],
       [3],
       [4],
       [2],
       [3],
       [5],
       [6]])


#  joining a numpy array 
# 1. vertical_stack using short form vstack .
# 2. horizontal_stack using short form hstack .
# 3. column_stack using form column_stack .

import numpy as np 
n1=np.array([1.2,3,2])
n2=np.array([2,4,3,5])
np.vstack((n1,n2))

array([[1, 2, 4],
       [2, 4, 3]])

import numpy as np 
n1= np.array([12,21,33])
n2= np.array ([21,32,55,43])
np.hstack((n1,n2))

array([12, 21, 33, 21, 32, 55, 43])

np.column_stack ((n1,n2)) #here the one arrayindex 0 has size three and another array index has size 4 
# here column stack index i same necessary
n2 = np.array([22,32])
n3= np.array ([23,22])
np.column_stack((n2,n3))

array([[22, 23],
       [32, 22]])


#Intersection and difference 
import numpy as np
n1 = np.array ([12,14,47,43,21])
n2 =np.array ([23,21,43])
np.intersect1d(n1,n2)

array([21, 43])


n1 = np.array([21,23]) 
n2= np.array ([32,78])
np.intersect1d (n1,n2)

array([], dtype=int32)

n1 = np.array ([12,14,47,43,21])
n2 =np.array ([23,21,43])
np.setdiff1d (n1,n2)

array([12, 14, 47])
np.setdiff1d (n2,n1)

array([23])

#Adittion of numpy array 
#Numpy array mathematics 
import numpy as np 
n1 = np.array ([1,1,1])    # here all elments is sum 
n2 = np.array ([1,1,1])
np.sum ([n1,n2])

6

#here only each column is added (sum)
np.sum ([n1,n2],axis=0)

array([2, 2, 2])

# here only each rows is added (sum)
np.sum ([n1,n2],axis =1)

array([3, 3])


#Basic addition 
import numpy as np 
n1= np.array ([1,2,4,5])
n1= n1+1
n1


#Basic multiplication 
n1 = np.array ([1,2,3,4])
n1 = n1*2
n1

#Basic subtraction 
n1= np.array ([1,4,2,1])
n1 = n1-1
n1

n1= np.array ([1,4,2,1])
n1 = n1-2
n1


#Basic addition 
import numpy as np 
n1= np.array ([1,2,4,5])
n1= n1+1
n1


#Basic multiplication 
n1 = np.array ([1,2,3,4])
n1 = n1*2
n1

#Basic subtraction 
n1= np.array ([1,4,2,1])
n1 = n1-1
n1

n1= np.array ([1,4,2,1])
n1 = n1-2
n1

 #Basic division 
n2 = np.array ([1,2,4])
n2 = n2/2
n2


#basic i want found mean then i do 
import numpy as np 
n1 =np.array ([1,2,3,4,5])
np.mean (n1)

# Standard deviiation  
n1 = np.array ([2,4,2,1])
np.std (n1)

# i found median 
n1 = np.array ([1,2,3,4])
np.median(n1)

2.5

n1= np.random.randint (1,10,3)
n1
array([1, 6, 8])
np.mean(n1)
5.0

n1= np.random.randint (1,10,3)
n1
array([1, 4, 2])

np.median (n1)
2.0


# Numpy save or load 
import numpy as np
n1 = np.array ([1,2,34,4])
np.save('my_numpy',n1) 

# Numpy load 
import numpy as np 
n2 = np.load('my_numpy.npy')
n2

array([ 1,  2, 34,  4])

#numerical computing is end then start how data manupulation with the help of pandas
# Pandas stands for Panel Data and is the core library for data manupulation and data analysis .

# it consists of single and multi-dimensional data structure for data manupulaton .
# or give some method for help of data manupulation 

# single dimentional array  -> series object
# multidimentinal array  -> Data Frame 

# Series object is one dimentional labeled aray

import pandas as pd 
s1  = pd.Series ([1,23,4,45])   # here 0 1 2 3 is index 
s1

0     1
1    23
2     4
3    45
dtype: int64

type (s1)
pandas.core.series.Series

s1= pd.Series ([1,2,3,4] , index= ['a','b','c','d'])
s1
a    1
b    2
c    3
d    4
dtype: int64

# i can also create a series object from dictionary
import pandas as pd 
s2 = pd.Series ({"a": 12, "b": 32, "c" : 23, "d" : 34 }) # here keys convert to index and values ar convert to series object 
# series's S is capital 
s2
a    12
b    32
c    23
d    34
dtype: int64

import pandas as pd
s3 = pd.Series ({"a":23,"b":32,"d":43}, index= ["a","d","c","b"]) # you can change index  
s3 
a    23.0
d    43.0
c     NaN
b    32.0
dtype: float64

# Extracting Indivisual Elements 
#  1. Extracting a single element 
#  2. Extracting elements from back 
#  3. Extracting a sequence of elements 
# Extracting a single element 
import pandas as pd 
s1 = pd.Series ([1,12,3,3,4])
s1[3]
3









