'''
MAIN CONCEPTS OF OOPS 

CLASS 
OBJECTS 

4 MAIN PILLARS OF OOPS:

POLYMORPHISM
ENCAPSULATION
INHERITANCE 
ABSTRACTION

''' 
'''
CLASSES ARE CREATED BY KEYWORD class 
attributes are variables that belong to class 
attributes are by default public and can be accessed through dot(.) operator 
'''
#
#class Dog :
#    attr1 = 'dog'
#    def __init__(self,name): # Construvtor
#        self.name =  name  
#
#    def speak(self):
#        print('my name is {}'.format(self.name))
#
#dog1 = Dog('Tommy') 
#dog2 = Dog('Rodger') 
#
#print(dog1.name) #accessing instance variable
#print(dog2.name) 

#dog1.speak() # accessing class methods
#dog2.speak() 

'''
VARIABLE 

1. INSTANCE VARIABLE 
2. STATIC VARIABLE 
3. LOCAL VARIABLE 
'''

'''
METHOD
1. INSTANCE METHOD 
2. CLASS METHOD 
3. STATIC METHOD 
'''


#class Student:
#    def __init__(self,name , rollno , marks) :  # constructor
#        self.name = name
#        self.rollno = rollno
#        self.marks = marks
#        print('object id inside class is',id(self))
#    def talk(self):
#        print('HELLO , MY NAME IS', self.name) 
#        print('MY ROLLNO IS', self.rollno) 
#        print('MY MARKS ARE', self.marks ) 
#
#ziyad = Student('Ziyad',10 ,98) 
#print('ziyad object id ' , id(ziyad))
#apurva = Student('Apurva',12,97) 
#print('Apurva object id ' , id(apurva))
#print(ziyad.marks)
#print(apurva.name)
#
#ziyad.talk() 
#apurva.talk() 
#
'''
object id inside class is 2632143305744
ziyad object id  2632143305744

'''

class Test :
    def __init__(self) :
        print('constructor') 

    def m1(self , x):
        print('x value',x) 

t = Test()  #constructor
t.m1(10)  # t 10    m1(t , 10)
Test.m1(t , 10) 

class bn:
    def __init__(sunny):
        sunny.name = 'Arijit'
        print(sunny.name)

s1 = bn() 

'''
create a class Cat 
assign values like cat name , cat age 
and print the value 
'''
class Cat:
    def __init__(self , name , age):
        self.name=name
        self.age=age
    def talk(self):
        print('My cat name is',self.name)
        print('My cat age is',self.age)
c=Cat('Manjar', 2)
c.talk()
print(c.name)
print(c.age) 

c1 = Cat('billi', 7) 
c1.talk()
print(c1.name)
print(c1.age) 




