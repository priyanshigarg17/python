# file handling is a mechanism to
# read or store the file permanently
# so that we can use it consistently
# process 3 steps
#- open file
#-read and write file
#-store

# f=open("count.txt", "r")
# print(f.read())  #read
# f.close()


# f=open("count.txt", "w")
# f.write("ujjawal")  #write
# f.close()


# f=open("count.txt", "r+") #to read and write
# print(f.read())  #read or x= f.read() and then print(x)
# f.write("regex")
# f.close()
# # f or fileobject



# fileobj=open("count.txt", "r+")
# fileobj.write("$$")
# x=fileobj.read()
# fileobj.close()
# print("file=>", x)



# w+ clears all the data

# fileobj=open("count.txt", "w+")
# print("cur1:", fileobj.tell() ) #tell apki current position print krta hai
# fileobj.write("rajasthan")
# print("cur2:", fileobj.tell() ) 
# fileobj.seek(4)  #Set the stream position, and return the new stream position.
# x=fileobj.read()
# print("cur3:", fileobj.tell() ) 
# fileobj.close()
# print("file=>", x)

"""fileobj=open("count.txt", "w+")
print("cur1:", fileobj.tell() ) #tell apki current position print krta hai
fileobj.write("rajasthan")
print("cur2:", fileobj.tell() ) 
fileobj.seek(4)  #Set the stream position, and return the new stream position.
x=fileobj.read()
print("cur3:", fileobj.tell() ) 
fileobj.close()
print("file=>", x)"""


# #new synatx with with
# with open("count.txt", "r") as fileobj:
#     x=fileobj.read()


# with open("count.txt", "r") as fileobj:
#     x=fileobj.readline()


# with open("count.txt", "r") as fileobj:
#     x=fileobj.readlines()


# with open("count.txt", "r") as fileobj:
#     for line in fileobj:
#         print(line.strip()) #strip remove unusefull charcters like /n

# with open("count.txt", "r") as fileobj:
#     x=fileobj.read()
#     print(x)

# with open("count.txt", "r") as fileobj:
#     for line in fileobj:
#        line=line.strip()
#        print(line.split(","))



#using csv


# import csv
# with open('count.txt', 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     print("Header:", header)
#     for row in reader:
#         print("Row:", row)

import os

def create_desktop_file(option):
    if option==1:
        os.mkdir("my_new_folder")
        print("my_new_folder")

create_desktop_file(1)
    
