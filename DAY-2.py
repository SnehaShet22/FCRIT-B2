'''
class Dog :
    attr1 = 'dog'
    def __init__(self,name): # Construvtor
        self.name =  name  

    def speak(self):
        print('my name is {}'.format(self.name))

dog1 = Dog('Tommy') 
dog2 = Dog ('Bunny')
dog1.name   # access instance variable
dog1.speak() # access instance method

print(dog1.attr1) # access Static variable  #dog
dog1.attr1 = 'Penguin' 
print(dog1.attr1) #Penguin
print(dog2.attr1) # dog 

Dog.attr1 = 'Parrot' 
print(dog1.attr1)
print(dog2.attr1) 




class Student :
    institute = 'Campus Credential'

    def __init__(self,name , roll_no) :
        self.name = name
        self.roll_number = roll_no

    def speak(self):
        print('my name is',self.name,'roll no is',self.roll_number,'and i go to',self.institute)


s1 = Student('Vivek',1) 
s1.speak() 
s1.institute = 'FCRIT'  #changing static variable for one object
print(s1.institute) #FCRIT

s2 = Student('Akash',2 ) 
s2.speak() 
print(s2.institute)  # CC 


#change static variable for all object use class name
Student.institute = 'CC'
s1.speak() 
s2.speak() 



from numpy import test


class Movie:
    def __init__(self,title , actor , actress):
        self.title = title
        self.actor = actor
        self.actress = actress 
        
    def info(self):
        print('Movie Name',self.title)
        print('Actor Name',self.actor)
        print('Actress Name',self.actress)        

list_of_movies = []     # []

while True:
    title=input('Enter Movie name')
    Actor =input('Enter Actor name')
    Actress =input('Enter Actress name') 

    m = Movie(title , Actor , Actress) # Create an object 
    list_of_movies.append(m)
    print('movie added successfully') 

    option = input('Do you want to add one more movie? [YES/NO]')
    if option.lower()=='no':
        break 

print('ALL MOVIES INFORMATION..')
for movie in list_of_movies:
    movie.info()
    print()



class Test :
    def __init__(self) :
        print('constructor') 

t1 = Test() 
t2 = Test()
t3 = Test() 



# constructor is optional in python
# if you dont create a constructor , python will create it (default constructor)
class Test:
    def m1 (self):
        print('method execution...') 

t1 = Test() 
t1.m1() 

class Test:
    def __init__(self):
        print('Constructor Executed')

t = Test()  # Will create only one object
t.__init__()
t.__init__()
t.__init__() 



class Test:
    def __init__(self):
        print('no arg constructor')
    def __init__(self , x):
        print('one arg constructor')

    def m1 (self , x , y):
        print(x,y) 

    def m1 (self , x ):
        print(x)

#t1 = Test() # error python does not support method overloading 
# Constructor is a method too
t2 = Test(10)

t2.m1(5)

''' 
class movie :
    def __init__(self , a , b , c ):
        self.title = a 
        self.actor = b 
        self.actress = c 

# good practice to use proper local variable names insted of a,b,c 
# our program becomes more readable or understandable