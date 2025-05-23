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

f=open("count.txt", "r+")
print(f.read())  #read
f.write("regex")
f.close()