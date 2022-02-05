# TYPES OF METHODS 
# INSTANCE METHOD : deal with instance variable
# CLASS METHODS   : deal with static variables
# STATIC METHODS  : deal with local variables


#1. INSTANCE METHOD 

from numpy import test


class Student:
    schoolname = 'FCRIT'#static variables
                     #local  #local
    def __init__(self,name , rollno): #constructor
        self.name = name  #instance variables
        self.rollno = rollno #instance variables 

    def get_student_info (self):       #instance method
        print('student name:',self.name)
        print('student rollno:',self.rollno)


# 2. CLASS METHODS 

class Student:
    schoolname = 'FCRIT'#static variables
                     #local  #local
    def __init__(self,name , rollno): #constructor
        self.name = name  #instance variables
        self.rollno = rollno #instance variables 

    @classmethod
    def get_school_info(cls):                #Class method
        print('School name : ',cls.schoolname)

Student.schoolname
# proof that cls points to current class.
class Test:
    @classmethod
    def m1(cls): #CR
        print(id(cls)) #1958257646688

print(id(Test))  #1958257646688
Test.m1()


#3. STATIC METHODS  
class Student:
    schoolname = 'FCRIT'#static variables
                     #local  #local
    def __init__(self,name , rollno): #constructor
        self.name = name  #instance variables
        self.rollno = rollno #instance variables 


    @staticmethod
    #           local  local
    def getsum (num1 , num2):
        sum=num1 + num2  # local 
        return sum 

# SUMMARY 

class Student:
    schoolname = 'FCRIT'#static variables
                     #local  #local
    def __init__(self,name , rollno): #constructor
        self.name = name  #instance variables
        self.rollno = rollno #instance variables 

    def get_student_info (self):       #instance method
        print('student name:',self.name)
        print('student rollno:',self.rollno)

    @classmethod
    def get_school_info(cls):                #Class method
        print('School name : ',cls.schoolname)


    @staticmethod
    #           local  local
    def getsum (num1 , num2):                 # Static method
        sum=num1 + num2  # local 
        return sum 

#  VARIOUS PLACES TO DECLARE INSTANCE VARIABLES!!!

# 1. Inside Constructor by using self  
# 2. Inside Instance method by using self  
# 3. Outside class by using object reference 



class Test:
    def __init__(self) : #1
        self.a = 10
        self.b= 20 

    def m1(self):
        self.c = 30  #2

t = Test()     #a and b will be added
print(t.__dict__)                           #{'a': 10, 'b': 20}
t.m1()         # c will be added
print(t.__dict__)                           #{'a': 10, 'b': 20, 'c': 30}

t.d = 40       # d will be added
print(t.__dict__)                           #{'a': 10, 'b': 20, 'c': 30, 'd': 40} 4 instance variables


t2 = Test() 
t2.m1() 
print(t2.__dict__)  #{'a': 10, 'b': 20, 'c': 30} 3 instance variable

'''
In other languages like java , number of instance variables are always fixed,
cant change number of variable object to object.

In PYTHON we can have different number of instance variables for different objects
'''

# accessing instance variables
# 1.within class  
# 2.outside class



class Test:
    def __init__(self) : 
        self.a = 10
        self.b= 20 
    
    def display(self): #1
        print(self.a)
        print(self.b)
t = Test()
t.display() 
#2
print(t.a)
print(t.b)  

#deleting instance variables
# 1.within class  
# 2.outside class

class Test:
    def __init__(self) : 
        self.a = 10
        self.b= 20
        self.c = 30
        self.d= 40 
    
    def m1(self):  #1
        del self.c 

t1 = Test() 
print(t1.__dict__)      #{'a': 10, 'b': 20, 'c': 30, 'd': 40}                      

t1.m1()
print(t1.__dict__)     #{'a': 10, 'b': 20, 'd': 40}

del t1.a , t1.b   #2
print(t1.__dict__)     #{'d': 40}


t2 = Test()    #new object
del t2.b , t2.d
print(t2.__dict__) #{'a': 10, 'c': 30}

'''
Instance variables which are deleted from one object wont be deleted from other object
because for every object separate copy of variables is present 
'''

class Test:
    def __init__(self) : 
        self.a = 10
        self.b= 20

t1 = Test()
t1.a = 888
t1.b = 999 

t2 = Test() 
print(t1.a , t1.b) 
print(t2.a , t2.b)
