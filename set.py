#datatype to store all values 
#all values are unique
#not orders as not indexed
#mutable

'''
myset={1, 2, 3, 1, 1, 1, "def", 555, 7}
print(myset)

output=
{1, 2, 3, 7, 555, 'def'}
'''


'''
#to insert element and delete
myset={1, 2, 3, 1, 1, 1, "def", 555, 7}
myset.add(80)
myset.discard(77)
print(myset)

output=
{80, 1, 2, 3, 'def', 7, 555}
'''

'''
#to combine 2 sets
myset={10, 20, 30}
myset2={40, 50}
print(myset.union(myset2))
output={50, 20, 40, 10, 30}
'''

'''
#to find common
myset={10, 20, 30}
myset2={40, 50, 30}
myset.intersection(myset2)
'''


'''
#to check superset
myset={10, 20, 30, 40, 50}
myset2={40, 50, 30, "abc"}
print(myset.issuperset(myset2))
output=False'''

#set symmetric difference- by yourself
# set difference

#set comprehension
x={i for i in range(1, 10) if i%2==0}
print(x)