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








