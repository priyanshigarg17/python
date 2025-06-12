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

# #count vowel
# s='regex software'
# regexsoftware={}
# for i in s:
#     if i in "aeiou":
#         regexsoftware[i]=regexsoftware.get(i, 0)+1
# print(regexsoftware)


'''second approach'''

# data="helloe"
# mydictionary={}

# for char in data:
#   if char in "aeiou":
#     if char in mydictionary:
#       mydictionary[char]+=1
#     else:
#       mydictionary[char]=1

#     print(char, mydictionary)

'''
e {'e': 1}
o {'e': 1, 'o': 1}
e {'e': 2, 'o': 1}
'''

# #dictionary comprehension
# x={i:1 for i in "hey"}
# print(x)

'''output={'h': 1, 'e': 1, 'y': 1}'''

#list comprehension
# x=[i+5 for i in [10, 20, 30]]
# print(x)

# '''output=[15, 25, 35]'''


dict={"a":2, "b":3}
dict2={"c":4, "d":5}
dict.update(dict2)
print(dict)
