#open bracket must be closed in the correct order
# s="[(]"
# x=[]
# a=0 #indicator
# for i in range(0, len(s)):
#   char=s[i]
#   if(char=='(' or char=="{" or char=="["):
#     x.append(char)
#   else:
#     if((char==")" and "("==x[-1]) or (char=="]" and "["==x[-1]) or (char=="}") and "{"==x[-1]):
#       a=1
#     else:
#       a=0
#       break
# if(a==1):
#   print("valid")
# else:
#   print("invalid")




# s="([]}"
# x=[]
# a=0 #indicator
# for i in range(0, len(s)):
#   char=s[i]
#   if(char=='(' or char=="{" or char=="["):
#     x.append(char)
#   else:
#     if((char==")" and "("==x[-1]) or (char=="]" and "["==x[-1]) or (char=="}") and "{"==x[-1]):
#       a=1
#       x.pop()
#     else:
#       a=0
#       break
# if(a==1):
#   print("valid")
# else:
#   print("invalid")




# s="{}"   
# x=[]      #x store open bracket
# a=0
# for i in range(0, len(s)):
#   char=s[i]
#   if(char=="(" or char=="{" or char=="["):
#     x.append(char)
#   elif(len(x) >0):
#     if( (char==")"  and "("==x[-1]) or ( char=="]"  and "["==x[-1])  or ( char=="}"  and "{"==x[-1]) ):
#       a=1
#       x.pop()
    
#     else:
#       a=0
#       break

# if(a==1):
#   print("valid")
# else:
#   print("invalid")

# numbers=[10, 20, 4, 45, 99]
# max=numbers[0]
# for i in range(0, len(numbers)):
#     if max<numbers[i]:
#         max=numbers[i]
# print("maximum number is ", max)

'''
output=maximum number is  99
'''

# x=[10, 20, 30, 40]
# sum=0
# for i in range(0, len(x)):
#     sum+=x[i]
# print(sum)

''''
output=100
'''
# nums=[1, 2, 3, 4, 5]
# x=[]
# list=len(nums)
# for i in range(list -1, -1, -1):
#     x.append(nums[i])
# print(x)

''''
output=[5, 4, 3, 2, 1]
'''
# num=[8, 9, 3, 2, 7]
# asclist=[]
# while num:
#     min=num[0]
#     for i in range(1, len(num)):
#         if min>num[i]:
#             min=num[i]
#     asclist.append(min)
#     num.remove(min)

# print("asc order is ", asclist)
'''
output: asc order is  [2, 3, 7, 8, 9]
'''
# num=[1, 2, 2, 3, 4, 4, 5]
# for i in range(0, len(num)):
#     for j in range(i+1, len(num)):
#         if num[j]==num[i]:
#             num.remove(num[j])
#             break
# print(num)
'''
output=[1, 2, 3, 4, 5]
'''
# num=[1, 2, 3, 4, 3, 5, 6]
# for i in range(0, len(num)):
#     for j in range(i+1, len(num)):
#         if(num[i]+num[j]==6):
#             print(num[i], num[j])

'''
1 5
2 4
3 3
'''
# numbers = [1, 2, 3, 4, 5]
# min=numbers[0]
# max=numbers[1]
# sum=0
# for i in range(1, len(numbers)):
#     if min>numbers[i]:
#         min=numbers[i]
# for j in range(2, len(numbers)):
#     if max<numbers[j]:
#         max=numbers[j]
# numbers.remove(min)
# numbers.remove(max)
# print(numbers)
# for k in range(0, len(numbers)):
#     sum+=numbers[k]
# print(sum)
'''
output:-[2, 3, 4]
9
'''

# nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
# Flattenedlist: []
# for i in range(0, len(nested_list)):
#     if nested_list 

#  checks if the list is a palindrome 
# num = [1, 2, 3, 2, 1]
# for i in range(0, len(num)):
#     if(num[i]==num[-(i+1)]):
#         continue
#     else:
#         print("false")
#         break
# else:
#     print("true")

'''
output: false
'''
num = [1, 2, 3, 2, 4, 5, 1, 6]
for i in range(0, len(num)):
    for j in range(i+1, len(num)):
        if(num[j]==num[i]):
            num.pop(num[j])
            break
print(num)

'''
[2, 3, 2, 4, 5, 1, 6]
'''

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Result= []
# for i in range(0, len(list1)):
#     for j in range(0, len(list2)):
#         if list1[i]==list2[j]:
#             Result.append(list2[j])
#             break
# print(Result)

'''
[3, 4, 5]
'''
# words = ["apple", "banana", "strawberry", "kiwi"]
# longest=words[0]
# for i in range(0, len(words)):
#     if longest<words[i]:
#         longest=words[i]
# print(longest)

'''
strawberry
'''

# n = [-1, 0, 1, 2, -1, -4]
# for i in range(0, len(n)):
#     for j in range(i+1, len(n)):
#         for k in range(i+2, len(n)):
#             if(n[i]+n[j]+n[k]==0):
#                 print(n[i], n[j], n[k])
#                 break

# mytuple=(10, 20, "abc", 10)
# mytuple.count(10)
# print(mytuple.count(10))

# mytuple=(10, 20, "abc", 10)
# print(mytuple.index("abc"))

# dictionary
# no index position
# time complexity for insert/access: O(1)
# mutuable datatype
# key is unique identifier
#value: are like the data
# element store in form of key and value pair

''''
mydictionary={10:"aman", 11:"aditya"}
mydictionary[12]='naina' #to insert the new
mydictionary[10]="ujjwal" #to updata the value
x=mydictionary.pop(11) #mydictionary.pop(11) #to delete
print(mydictionary)
print(x)

mydictionary={10:"aman", 11:"aditya"}
mydictionary.update({10:"naina", 11:"aditya"}) #to update using update fun
print(mydictionary)

mydictionary={10:"aman", 11:"aditya"}
print(mydictionary.keys())
print(mydictionary.values())
print(mydictionary.items())


mydictionary={10:"aman", 11:"aditya"}
for i in mydictionary:
    print(i, mydictionary[i])

mydictionary={10:"aman", 11:"aditya"}
for i in mydictionary.keys():
    print(i, mydictionary[i])

mydictionary={10:"aman", 11:"aditya"}
for i in mydictionary.items():
    print(i)

mydictionary={10:"aman", 11:"aditya"}
for i in mydictionary.values():
    print(i)
'''
# s='hello'
# mydictionary={}
# count=0
# for i in s:
#     count+=1
# mydictionary["total"]=count
# print(mydictionary)

# output:
# {'total': 5}

# s='hello'
# count=0
# mydictionary={"total":0}
# for i in s:
#     mydictionary["total"]=mydictionary["total"]+1
# print(mydictionary)
# {'total': 5}

'''
mydictionary={"salary:80"}
mydictionary["salary"]=mydictionary["salary"]+5
print(mydictionary)

output={'salary':85}

'''
# s="hleidfejr"
# mydictionary={"vowels":0}
# for i in s:
#     if i in "aeiou":
#         mydictionary["vowels"]=mydictionary["vowels"]+1
# print(mydictionary)

# s="heyvit"
# mydictionary={}
# for i in s:
#     mydictionary[i]=1
# print(mydictionary)

# {'h': 1, 'e': 1, 'y': 1, 'v': 1, 'i': 1, 't': 1}

