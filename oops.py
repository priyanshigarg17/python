# class HouseDesign:
#     color="yellow"

# #object=class()
# h1=HouseDesign()
# print(h1.color)

"output= yellow"



# class HouseDesign:
#     color="yellow"

# #object=class()
# h1=HouseDesign()
# h1.color="green" #to change the color
# print(h1.color)

# h2=HouseDesign()
# print(h2.color)
'''output=
green
yellow'''


#function constructor => used to initialize memory for an object
# class HouseDesign:
#     def __init__(self):   #memory address of current object
#         print("called constructor")

# h1=HouseDesign()    #h1 object access the memmory from class
# print(h1)

'''
called constructor
<__main__.HouseDesign object at 0x00000297E64D9BB0>

'''

'''#class ke naam ke aage bracket use krne se consturcrot call hoga jiska address ek variable store hoga'''

# class HouseDesign:
#     def __init__(self):   
#         self.color="green"
        
# house1=HouseDesign()    



# class HouseDesign:
#     def __init__(self, x):      #x is parameter
#         self.color=x
        
# house1=HouseDesign("green")   
# house2=HouseDesign("red") 
# print(house2.color, house1.color)

'''
output:
red green
'''
#multiple variable

# class HouseDesign:
#     def __init__(self, x, y):      #x is parameter
#         self.color=x
#         self.room=y
        
# house1=HouseDesign("green", 5)   
# house2=HouseDesign("red", 6) 
# print(house2.color, house1.room)

'''
output:
red 5
'''
#class=employee
#employee has three variables, employeeID, employeename and employeeemail

# class Employee:
#   def __init__(self, x,y):
#     self.id=x
#     self.name=y

#   def info(self):
#     print("data is", self.id, self.name)

# e1=Employee(10,"tushar")
# e1.info()



'class variables- 05-05-2025'
# class employee:
#     company = "regex"          #class variable
#                                 # intialized once and can access by both class name and object 
#     def __init__(self):
#         self.salary = 100
# e1 = employee()
# print(employee.company , e1.company)
# print(e1.salary)            # instance variable only access by object

'''
output:
regex regex
100
'''

# class employee:
#     count = 0
#     def __init__(self):
#         self.count+=1
#         print("constructor called",self.count)

# e1 = employee()
# e2 = employee()

'''
output:
constructor called 1
constructor called 1
'''

# class employee:
#     count = 0
#     def __init__(self):
#         employee.count+=1
#         print("constructor called",self.count)

# e1 = employee()
# e2 = employee()

'''
output:
constructor called 1
constructor called 1
'''



'''(Interitance)'''

# class parent:
#     amount = 500000
#     def hello(self):
#         print("hello from parent")

# class child(parent):
#     salary = 0

# c1 = child()
# c1.hello()
# print(c1.salary,c1.amount)

'''
hello from parent
0 500000
'''

# class parent:
#     amount = 500000
#     def hello(self):
#         print("hello from parent")

# class child(parent):
#     salary = parent.amount

# c1 = child()
# c1.hello()
# print(c1.salary)

'''
hello from parent
500000
'''

# class Driver:

#     def __init__(self,x,y,z):
#         self.driver_id = x
#         self.driver_name = y
#         self.driver_email = z

#     def show(self):
#         print("data is => ",self.driver_id,self.driver_name,self.driver_email)


# d1 = Driver(10,"ramesh","ramesh@gmail.com")
# d1.show()

'''
data is =>  10 ramesh ramesh@gmail.com
'''


# class A():
#     salary=100

# a1=A()
# print(a1.salary)

# class B(A):    #B is child, A is parent
#     amount=1000

# b1=B()
# print(b1.salary)

'''
100
100
'''

# class A():
#     salary=100
#     def info(self): 
#         print("this is class 1")
#         print("this is class 2")
#         print("this is class 3")

# class B(A):
#     amount=10000
#     def info2(self):
#       print("this is  class B ", self.amount, self.salary)
#       super().info()  
#     #self.info()   #<== calling function from parent class

# b1=B()
# b1.info2()
''''
this is  class B  10000 100
this is class 1
this is class 2
this is class 3

'''
# class A():
#     salary=100
#     def info(self): 
#         print("this is class 1")

# class B(A):
#     amount=10000

#     def info(self):
#         print("this is by self")
#     def info2(self):
#       print("this is  class B ", self.amount, self.salary)
#       super().info()    #output  this is  class B  10000 100, this is class 1

#     #self.info()   #<== calling function from parent class

# b1=B()
# b1.info2()


# class Driver:
#     def __init__(self, x, y, z):
#         self.id=x
#         self.name=y
#         self.email=z
   
#     def info(self):
#         print("data is -", self.id, self.name, self.email)

# d1=Driver(1008, "aman", "aman@gmail.com")
# d1.info()

# '''
# output-data is - 1008 aman aman@gmail.com
# '''

# class Customer(Driver):
#     def __init__(self, x, y, z):
#         super().__init__(x, y, z)

# c1=Customer(9009, "pri", "pri@gmail.com")
# c1.info()


# class Driver:
#     def __init__(self, x, y, z):
#         self.id=x
#         self.name=y
#         self.email=z
   
#     def info(self):
#         print("data is -", self.id, self.name, self.email)

# d1=Driver(1008, "aman", "aman@gmail.com")
# d1.info()

'''
output-data is - 1008 aman aman@gmail.com
'''


# class Customer(Driver):
#     def _init_(self,a,b,c):
#         super()._init_(a,b,c)

#     def c_info(self):
#         super().info()

# c1=Customer(123,"naina","naina@gmail.com")
# c1.c_info()



# class A:
#     def __init__(self):
#         print("hello")

#     def __init__(self):
#         print("this is second constructor")

# a1= A()


"""
create a class with two parametere a and b then create two instance variable with the same name a and b
"""

# class B:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# b1 = B(10, 20)
# b2 = B(30, 40)

# print(b1.a)
# print(b1.b)


'''#__add__[dunder function]'''

# class B:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, x):
#       print(self)
# b1 = B(10, 20)
# b2 = B(30, 40)

# print(b1)
# # print(b1+b2)
# # b1.__add__
# # __add__ [dunder function]
# # output=hey
# # print(x)
# # print(b1)


# class B:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, x):
#         print("Inside __add__, self:", self)
#         print("Inside __add__, x:", x)

#         return "done"

# b1 = B(10, 20)
# b2 = B(30, 40)

# print("Outside, b1:", b1)
# print("Outside, b2:", b2)


# print(b1 + b2)


'''
operator overloading- below
'''

# class xyz:
#     amount=1000

#     def __repr__(self):  #to change the representation of object
#       return f"xyz class has{self.amount}"
#     #method => number of parameters
#     # overloading the gt method => gt is function for --> operator
    
#     def __gt__(self,x):
#         print("hey")
# x1=xyz()
# x2=xyz()
# x1>x2   #(gives error as operatprs do not work for object so we use dunder methods like here we use __gt__ method)
# print(x1)

# hey
# xyz class has1000


'''instance method'''
# class xyz:
#     amount =1000
#     def __init__(self, salary):
#         self.salary=salary
    
#     def func(self):
#         print("value is", self.salary)

# x1=xyz(10)
# x1.func()

# '''static method'''
# class xyz:
#     amount =1000
#     def __init__(self, salary):
#         self.salary=salary
    
#     @staticmethod
#     def func(x):
#         print("value is", x)

# x1=xyz(10)
# x1.func(20)

# # output=value is 20



'''question for class method'''
# class Dollar:
#     def __init__(self, amount):
#         self.amount=amount
    

#     @classmethod
#     def __repr__(cls): 
#       return f"Amount in {cls} class"

# c1= Dollar(10)
# print(c1)

# # output'''Amount is 10'''

# class IndianRupee(Dollar):
#     def __init__(self, amount):
#         super().__init__(amount)

# ind1 =IndianRupee(50)
# print(ind1)


# class A:
#     def info(self):
#         print("hey info from A class")

#     def info(self, x):
#         print("hey this is from second class")

# a1=A()
# a1.info()

'''encapsulation'''

#private and protected (only for showing things but there is nothing called as private and protected)
# class users:
#     _amount = 100 #protected
#     __salary = 2000 #private

#     #by writing _class name then we can access both at any where
# class employee(users):
#     id=10

# e1=employee()
# print(e1._users__salary)



#abstarction property---------------

# from abc import ABC, abstractmethod
# class RBIAccount(ABC):  #abstract base class
#     @abstractmethod
#     def interest(self):   #abstarct method = which is not implement
#         pass

#     def info(self):    #normal method as abstarct class can both abstract method and normal method
#         print("hey")

# class saving_HDFC(RBIAccount):
#     amount=5000
#     def interest(self):    #this implementation is necessary
#         print("interest rate is 8%")

# s1=saving_HDFC()
# print(s1.amount)

#decorators---------
# def outerFunc():
#     def inner_function():
#         print("this is inner functions")

    
#     return inner_function()       

# x=outerFunc()
# print(x)

''' output-this is inner functions
None'''

# def outerFunc():
#     def inner_function():
#         print("this is inner functions")

    
#     return inner_function          #return the memeory address of iner fucntion

# x=outerFunc()
# x()         #this will call inner function


#clouser -----------

# def outerFunc(num):
#     print("outside functions", num)
#     def inner_function():
#         print("this is inner functions", num)
    
#     return inner_function       #return the memeory address of iner fucntion

# x=outerFunc(10)
# print(x)
# x()         #this will call inner function


'''output - outside functions 10
<function outerFunc.<locals>.inner_function at 0x00000224BEEED300>
this is inner functions 10'''



# def outerFunc(num):
#     def inner_function():
#         print("this is inner functions", num)
#         out = num().upper()    #will give hey by calling the test function
#         print("inside out-", out)  
#     return inner_function       #return the memeory address of iner fucntion

# def test():
#     return ("hey")

# # x=outerFunc(test)     #will provide memoery address of test to fucntion for num
# # x()     

# test=outerFunc(test)      #inner_funtion memory return
# test()  #inner function  

'''output==this is inner functions <function test at 0x000002047290D300>
inside out- HEY'''



# def outerFunc(num):
#     def inner_function():
#         out = num().upper()   
#         print("inside out-", out)  
#     return inner_function      

# @outerFunc
# def test():
#     return ("hey")
   
# test()

'''output- inside out- HEY'''


# fiabonnaci series using generator
def func():
    a=0
    b=1
    while(True):
        yield a
        a, b=b, a+b

gen=func()
for i in range(1, 11):
    print(next(gen))