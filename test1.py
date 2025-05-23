


# for i in range(1, 5):
#     for j in range(1, i+1):
#         if(j==1 or j==i):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")
# for i in range(3, 0, -1):
#     for j in range(1, i+1):
#         if(j==1 or j==i):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print("")


# str1="regexian"
# str2="tushar"
# count=0
# for i in str1:
#     # print(i, end=" ")
#     for j in str2:
#     # print(j, end=" ")
#         if i==j:
#             count+=1
#             print(count)


# str="hello hey computer science new"
# k=4
# for i in str:
#     if len(i)>k:
#         print(k, end="")
        

# s="ababa"
# mydict={}
# for i in range(0, 6):
#     data=""
#     for j in range(i, len(s)):
#         data=data+s[j]
#         print(data)
#         if data in mydict:
#             mydict[data]+=1
#         else:
#             mydict[data]=1
# print(mydict)

'''{'a': 3, 'ab': 2, 'aba': 2, 'abab': 1, 'ababa': 1, 'b': 2, 'ba': 2, 'bab': 1, 'baba': 1} '''

for i in range(1, 6):
    for j in range(1, 6-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        print(j, end=" ")
    print()





# str="huhii"
# total=0
# middle=0
# for i in str:
#     total+=1
#     middle=total//2
# print(total, i, middle)