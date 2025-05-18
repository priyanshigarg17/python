# x=10
# a=x
# print(id(x), id(a))
# a=20
# print(id(x), id(a))

''' means a is immutaable datatype as it changes the memory address'''



# x=[10, 20]
# a=x
# print(id(x), id(a))
# a.append(100)
# print(id(x), id(a), x, a)

''' No change in memory address in List datatype'''


# def test():
#     print("hello")
# test()

'''output=hello'''


# def test():
#     y=10 #local scope or life scope
#     print("hello", y)
# test()

'''output=hello 10'''



# a=10  #global scope
# def test():
#     y=10 #local scope or life scope
#     print("hello", y)
# test()
# print(a)

''' hello 10
    10 '''



# a=90  
# def test():
#     y=10 
#     a=100
#     print("hello", y, a)
# test()
# print(a)

''' hello 10 100  
    90''' #(here global variable change only local)



# a=90  
# def test():
#     global a
#     y=10 
#     a=100
#     print("hello", y, a)
# test()
# print(a)

''' hello 10 100
    100'''    #(here we made the "a" global)


# def msg(username):
#     print("hello user", username)

# msg("tushar")
'''hello user tushar'''


# def msg(username):  #username is parameter
#     print("hello user", username)

# msg("tushar")   #tushar is argument
# msg("aman")

'''hello user tushar
hello user aman'''


# def msg(username, x):  #username is parameter
#     print("hello user", username, x)

# msg("tushar", 100)
'''hello user tushar 100'''

# def func(num):
#     total=0
#     for i in range(1, num+1):
#         total+=i
#     print("total of starting", num, "is", total)

# func(5)
# func(7)

'''
total of starting 5 is 15
total of starting 7 is 28
'''




'''number is armstrong or not'''

# def func(num):
#     original = num
#     count = len(str(num))
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit ** count
#         num //= 10
#     if total == original:
#         print("Armstrong number")
#     else:
#         print("Not an Armstrong number")

# func(153)



'''Roman to Integer'''
# def int_to_roman(num):
#     val = [
#         1000, 900, 500, 400,
#         100, 90, 50, 40,
#         10, 9, 5, 4, 1
#     ]
#     syms = [
#         "M", "CM", "D", "CD",
#         "C", "XC", "L", "XL",
#         "X", "IX", "V", "IV", "I"
#     ]
#     roman = ""
#     for i in range(len(val)):
#         count = num // val[i]
#         roman += syms[i] * count
#         num -= val[i] * count
#     return roman

# print(int_to_roman(668))




# def func(a, b):
#     print("A=>", a, "B=>", b)

# func(10, 20) #data passed based on position and requierement

# #if we want to fix the values of parameter than that is called keyword argument regardless to position

# func(b=20, a=10)




# def func(a, b):
#     print("A=>", a, "B=>", b)

# func(10) #will throw error



#to solve this we create a default value at the time of creating function that can be change in future whill will be override by new Value
# def func(a, b=30): #defalut should be right hand side
#     print("A=>", a, "B=>", b)

# func(10)


'''variable length argument that means length will be change according to my request'''
'''always return in tuple format'''
# def func(*data):
#     print(data, type(data))

# func(20, 30, 40, 50)
# output=(20, 30, 40, 50) <class 'tuple'>


'''keyword variable length argument'''
# def func(**data):  
#     print(data, type(data))  #type return dictionary

# func(age=10, salary=1000)
# func(name="abc", age=30)



'''what is the difference between args(*) and kwargs(**)'''


#return keyword
# def shadi(lifafa):
#     print(lifafa+50)

# shadi(100)

' output=150'


# then
# def shadi(lifafa):
#     print(lifafa+50)

# x=shadi(100)
# print("x=>", x)

'''150
x=> None'''

'''now to return the value we use return'''
# def shadi(lifafa):
#     return(lifafa+50)

# x=shadi(100)
# print("x=>", x)

'''x=> 150'''

# def func(num):
#     print(num+10)
#     return "hello" 

# out=func(5)  #function calling
# print(out)

'''15
hello'''

#in case of two return value the first will be used




'''first class and higher order functions'''
# def square(num):
#     print(num*num)

# def addno(a,b):
#     print(a, b)

# addno(10, square(5)) 

#output=
'''25
10 None'''


#for not printing none we use return instead of print
# def square(num):
#     return(num*num)

# def addno(a,b):
#     print(a, b)

# addno(10, square(5)) 

'''10, 25'''

#cube
# def square(num):
#     return(num*num)

# def cube(a,b):    
#     print(a* b(a))

# cube(10, square)       cube is a first class function as it passed as a argument to another function

'''1000'''



#list type
def func(x):
    print("x=>", id(x), id(mylist))
    x.append(90)
    print("x new=>", id(x))

mylist=[10, 20]
func(mylist)
print("new=>", mylist)