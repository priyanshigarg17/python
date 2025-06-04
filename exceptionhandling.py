# try:
#     print("hey")
#     "abc"+10
#     print("hello")
# except:
#     print("error is being handled")



# try:
#     print("hey")
#     "abc"+10
#     print("hello")
# except Exception as e:
#     print("error is being handled", e)

'''hey
error is being handled can only concatenate str (not "int") to str'''

# try:
#     print("hey")
#     print("hello")
#     print(x)
# except NameError as e:
#     print("error is being handled", e)
# except ZeroDivisionError as e:
#     print("error is being handled", e)

"""output:hey
hello
error is being handled name 'x' is not defined"""

# try:
#     print("hey")
#     print("hello")
#     print(x)
# except (NameError,ZeroDivisionError) as e:
#     print("error is being handled", e)


"nested loop"
# try:
#     print("hey")
#     try:
#         10/0
#     except:
#         print("divided by zero error handled")
#     print("hello")
# except(NameError, ZeroDivisionError) as e:
#     print("error is beign handles", e)

"""hey
divided by zero error handled
hello"""


'try-except-else'
# try:
#     print("hey")
#     print("hello")
# except:
#     print("error is being handled")
# else:
#     print("else block")

"""hey
hello
else block"""

'try-except-finally'

# try:
#     print("hey")
#     print("hello")
# except:
#     print("error is being handled")
# finally:
#     print("finally block")


"#generate error "
# age=17
# if(age<18):
#     raise NameError

"#handle the generated error"
# try:
#    age=17
#    if(age<18):
#         raise NameError

# except ValueError:
#     print("value error due to age")

"assert keyword"
# x=10
# assert x!=10, "hey"


f= open("vij.txt", "r")
x=f.read()
raise FileNotFoundError
