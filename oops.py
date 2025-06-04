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

class employee:
    def __init__(self, x, y):
        self.id=x
        self.name=y
        
    def info(self):
        print("data is", self.id, self.name)


e1=employee(10, "pri")
e1.info


