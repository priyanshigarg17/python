#sorting dictionary
# d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
# mykeys = list(d.keys())
# mykeys.sort()
# print(mykeys)

# sd={i:d[i] for i in mykeys}
# print(sd)


#next question
# d = {2: 56, 1: 2, 5: 12, 4: 24}
# mylist=[i for i in d]
# for i in range(len(mylist)):
#     for j in range(0, len(mylist)-i-1):
#         if mylist[j]>mylist[j+1]:
#             mylist[j], mylist[j+1]=mylist[j+1], mylist[j]

# print(mylist)
# for i in mylist:
#     print(i, end=" ")

# d = {'a': 100, 'b': 200, 'c': 300}
# sum=0
# for i in d.values():
#     sum+=i
#     print(sum)


#sort even number values    
# d = {'a': 1, 'b': 4, 'c': 5, 'd': 2}
# mydict={}
# # Output: {'b': 4, 'd': 2}
# for i, j in d.items():
#     if j%2==0:
#        mydict[i]=j
# print(mydict)


# marks = {'Ram': 45, 'Shyam': 78, 'Aman': 52}
# # Output: {'Shyam': 78, 'Aman': 52}
# mydict={}
# # Output: {'b': 4, 'd': 2}
# for i, j in marks.items():
#     if j>=50:
#        mydict[i]=j
# print(mydict)

'''or'''

# marks = {'Ram': 45, 'Shyam': 78, 'Aman': 52}
# mydict={}
# for i in marks:
#     if marks[i]>50:
#         mydict[i]=marks[i]
# print(mydict)

# items = {'pen': 5, 'pencil': 12, 'eraser': 8}
# new={}
# # Output: {'pen': 0, 'pencil': 12, 'eraser': 0}
# for i in items:
#     if items[i]<10:
#         new[i]=0
#     else:
#         new[i]=items[i]
# print(new)

'''this is a test this is only a test'''
# sentence = "this is a test this is only a test"
# mydict = {}

# Split sentence into words
# words = sentence.split()

# for word in words:
#     if word in mydict:
#         mydict[word] += 1
#     else:
#         mydict[word] = 1

# print(mydict)


# d1 = {'a': 2, 'b': 4}
# d2 = {'b': 3, 'c': 5}

# # Make a copy of d1 to avoid modifying original
# merged = d1.copy()

# # Loop through d2 and update merged dictionary
# for key in d2:
#     if key in merged:
#         merged[key] += d2[key]
#     else:
#         merged[key] = d2[key]

# print(merged)


# sales = {'A': 120, 'B': 305, 'C': 150}

# min_key = None
# min_value = None

# for key in sales:
#     if min_value is None or sales[key] < min_value:
#         min_value = sales[key]
#         min_key = key

# print("Minimum sale is by:", min_key, "with value:", min_value)

points = {'p1': 10, 'p2': -5, 'p3': 0, 'p4': -1}
# Output: {'p1': 10, 'p3': 0}
new={}
for i, j in points.items():
    if j>=0:
        print(i)
        new[i]=j
print(new)
    
    


