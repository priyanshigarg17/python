#find maximum number
# list_1=[6, 4, 2, 3, 5, 7, 8, 9, 0]
# max_num=list_1[0]
# for i in range(0, len(list_1)):
#     if list_1[i]>max_num:
#         max_num=list_1[i]
# print(max_num)

#find second highest

#find maximum word
# word=["jay", "abhishek", "priyanshi", "divya"]
# max_num=word[0]
# for i in range(0, len(word)):
#     if word[i]>max_num:
#         max_num=word[i]
# print(max_num)

#find maximum number
# list_1=[6, 4, 2, 3, 5, 7, 8, 9, 0]
# max_num=list_1[0]
# for i in range(0, len(list_1)):
#     if list_1[i]>max_num:
#         max_num=list_1[i]
# print(max_num)

# with open("python.py", "r") as new:
#     x=new.read()
#     print(x)

# l = [6,4,2,3,5,7,8,9,0]
# max = l[0]
# second_max = l[0]

# for i in range(len(l)):
#     if l[i] > max:
#         second_max = max
#         max = l[i]
    
#     elif l[i] > second_max and l[i]!=max:
#         second_max = l[i]

# print(second_max)

# l = ["jay", "abhishek", "priyanshi", "divya"]
# max = l[0]
# second_max = l[0]

# for i in range(len(l)):
#     if l[i] > max:
#         second_max = max
#         max = l[i]
    
#     elif l[i] > second_max and l[i]!=max:
#         second_max = l[i]

# print(second_max)

# def find_second_highest(scores):
#     unique_scores = list(set(scores))  
#     if len(unique_scores) < 2:
#         return None  
#     unique_scores.sort(reverse=True)
#     return unique_scores[1]  
# scores = [45, 87, 92, 66, 92, 73]
# result = find_second_highest(scores)
# if result is not None:
#     print("Second highest score:", result)
# else:
#     print("Second highest score not available.")


l = ["jay", "abhishek", "priyanshi", "divya"]
max=l[0]
for i in range(len(l)):
    print(i)
