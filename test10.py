# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, i+1):
#         if(j==1 or j==i or i==5):
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

''''
output=
# # # # # 
  #     #
    #   #
      # #
        #
'''      

# for i in range(4, 0, -1):
#     for j in range(4, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if(j==1 or j==2*i-1 or i==4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

'''
output
* * * * * * * 
  *       *
    *   *
      *
'''
# for i in range(5, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end="")
#     for j in range(1, i+1):
#             print("*", end="")
#     print()
# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(" ", end="")
#     for j in range(1, i+1):
#             print("*", end="")
#     print()

'''
output
*****
 ****
  ***
   **
    *
    *
   **
  ***
 ****
*****

'''

# num=5
# factorial=1
# for i in range (1, num+1):
#     factorial=factorial*i
# print("factorial is ", factorial)

'''
output:
factorial is  120
'''

# list1 = [2, -7, 5, -64, -14]
# count=0
# count1=0
# for i in range(0, len(list1)):
#     if(list1[i]<0):
#         count+=1
#     if(list1[i]>0):
#         count1+=1
# print("pos", count1)
# print("negative", count)

'''
pos 2
negative 3
'''