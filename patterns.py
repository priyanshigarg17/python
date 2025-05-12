# for i in range(1, 6):
#   for j in range(1, 6-i):
#     print("*", end=' ')
#   print("")

 #output=
''' 
* * * * 
* * * 
* * 
* 
'''
# for i in range(1, 5):
#     for j in range(1, i):
#         print(" ", end="")
#     for j in range(1, 5):
#         print("*", end="")
#     print()

'''
****
 ****
  ****
   ****
'''

# for i in range(1, 5):
#   for j in range(i, 6): 
#    print(" ", end="")  # Two spaces per indent
#   for j in range(1, i + 1):
#     print("*", end=" ")
#   print("")  # New line

'''
     *
    * *
   * * *
  * * * *
'''

# for i in range(1, 6):
#   for j in range(i, 6): 
#    print(" ", end="")  # Two spaces per indent
#   for j in range(1, i + 1):
#     print("*", end=" ")
#   print("")  # New line
'''
     *
    * *
   * * *
  * * * *
 * * * * *
''' 

# for i in range(1, 6):
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print("")
'''
          *
        * *
      * * *
    * * * *
  * * * * *
'''  

# for i in range(1, 6):
#     x=1
#     for j in range(i, 6):
#         print(" ", end=" ")
#     for j in range(1, i + 1):
#         print(x, end=" ")
#         x+=1
#     print("")

'''
          1
        1 2
      1 2 3
    1 2 3 4
  1 2 3 4 5
'''    
# for i in range(1, 6):
#   for j in range(1, 5):
#       if i == 1 or i == 5 or j == 1 or j == 4:
#         print("*", end="")
#       else:
#         print(" ", end="")
#   print("")
'''
****
*  *
*  *
*  *
****
'''


# for i in range(5, 0, -1):
#     # Print leading spaces
#     for j in range(5 - i):
#         print("  ", end="")  # Two spaces for alignment
    
#     # Print stars
#     for j in range(1, i+1):
#         print("* ", end="")
    
#     print()

'''
 * * * * *
   * * * *
     * * *
       * *
         *   
'''       
# for i in range(5, 0, -1):
#     # Print leading spaces
#     for j in range(5 - i):
#         print("  ", end="")  # Two spaces for alignment
    
#     # Print stars
#     for j in range(1, i+1):
#         print(j, end=" ")
    
#     print()

'''
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 
'''

# # Patterns
# for i in range(1, 6):
#     x = 70- i  # Starting character code (E, D, C, B, A)
#     for j in range(i):
#         print(chr(x + j), end=" ")
#     print() 

'''
E 
D E 
C D E 
B C D E 
A B C D E 
'''    
# for i in range(1, 5):
#     for j in range(1, 6-i):
#         print(" ", end="")
#     for j in range(1, 5):
#         print("*", end="")
#     print()

'''
    ****
   ****
  ****
 ****
'''

# for i in range(1, 6):
#     x=1
#     for j in range(1, 6-i):
#         print(" ", end="")
#     for j in range(1, 6):
#         print(x, end="")
#         x+=1
#     print()

'''
    12345
   12345
  12345
 12345
12345
'''
# for i in range(1, 6):
#     x=65
#     for j in range(1, 6-i):
#         print(" ", end="")
#     for j in range(1, 6):
#         print(chr(x), end="")
#         x+=1
#     print()

'''    
    ABCDE
   ABCDE
  ABCDE
 ABCDE
ABCDE

'''
'''
for i in range (1, 5):
  for j in range(1, 5-i):
    print(" ", end='')
  for k in range(1, 2*i):
    print("*", end='')
  print()

   *
  ***
 *****
*******
'''

# for i in range (1, 5):
#   for j in range(1, i):
#     print(" ", end='')
#   for k in range(9, 2*i, -1):
#     print("*", end='')
#   print()

'''
*******
 *****
  ***
   *
'''

# for i in range(1, 5):
#   for j in range(1, i+1):
#     print("*", end='')
#   print()
# for i in range(1, 4):
#   for j in range(1, 5-i):
#     print("*", end="")
#   print()

'''
*
**
***
****
***
**
*
'''

# for i in range(1, 5):
#   for j in range(i, 4):
#     print(" ", end=" ")
#   for j in range(1, i+1):
#     print("*", end=" ")
#   print()
# for i in range(1, 4):
#   for j in range(1, i+1):
#     print(" ", end=" ")
#   for j in range(1, 5-i):
#     print("*", end=" ")
#   print()

'''
      * 
    * *
  * * *
* * * *
  * * *
    * *
      *

'''


# for i in range (1, 5):
#   for j in range(1, 5-i):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print("*", end='')
#   print()
# for i in range (1, 5):
#   for j in range(1, i):
#     print(" ", end='')
#   for k in range(9, 2*i, -1):
#     print("*", end='')
#   print()

''' 
   *
  ***
 *****
*******
*******
 *****
  ***
   *
'''
# for i in range (1, 6):
#   for j in range(1, 6-i):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print("*", end='')
#   print()
# for i in range (5, 0, -1):
#   for j in range(5, i,  -1):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print("*", end='')
#   print()

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
# for i in range (1, 6):
#   for j in range(1, 6-i):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print(k, end='')
#   print()
# for i in range (1, 5):
#   for j in range(1, i+1):
#     print(" ", end='')
#   for k in range(9, 2*i, -1):
#     print(k, end='')
#   print()

# for i in range(1, 6):
#   for j in range(1, i+1):
#     print(j, end=' ')
#   print()

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# for i in range(5, 0, -1):
#   for j in range(1, i+1):
#     print(j, end=' ')
#   print()

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

# for i in range (5, 0, -1):
#   for j in range(5, i, -1 ):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print(k, end='')
#   print()
# for i in range (2, 6):
#   for j in range(1, 6-i):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print(k, end='')
#   print()

'''
123456789
 1234567
  12345
   123
    1
   123
  12345
 1234567
123456789
'''


# for i in range (5, 0, -1):
#   x=65
#   for j in range(5, i, -1 ):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print(chr(x), end='')
#     x+=1
#   print()
# for i in range (2, 6):
#   x=65
#   for j in range(1, 6-i):
#     print(" ", end='')
#   for k in range(1, 2*i):
#     print(chr(x), end='')
#     x+=1
#   print()

'''

ABCDEFGHI
 ABCDEFG
  ABCDE
   ABC
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
'''

'''
for i in range(1, 6):
  # Left triangle
  for j in range(1, i+1):
    print('*', end="")

  # Spaces between the two triangles
  for j in range(1, (6 - i) * 2):
    print(" ", end="")

  # Right triangle (mirrored)
  for j in range(1, i+1):
    print('*', end="")

  print("")

print("", end='')
for i in range(4, 0, -1):
  for j in range(1, i+1):
    print("*", end='')
  
  for j in range(1, (6 - i) * 2):
    print(" ", end="")

  # Right triangle
  for j in range(1, i+1):
    print('*', end="")
  
  print()
'''
# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *


# for i in range(5, 0, -1):
#   for j in range(1, i+1):
#     print("*", end='')
  
#   for j in range(1, (6 - i) * 2):
#     print(" ", end="")

#   # Right triangle
#   for j in range(1, i+1):
#     print('*', end="")
  
#   print()
# for i in range(1, 6):
#   # Left triangle
#   for j in range(1, i+1):
#     print('*', end="")

#   # Spaces between the two triangles
#   for j in range(1, (6 - i) * 2):
#     print(" ", end="")

#   # Right triangle (mirrored)
#   for j in range(1, i+1):
#     print('*', end="")

#   print("")

'''
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
'''
# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         print(j, end=" ")
#     print()
# for i in range(4, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         print(j, end=" ")
#     print()

'''
        1 
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
'''


# for i in range(1, 6):
#     for j in range(1, 6):
#         if(j==1 or i==1 or j==5 or i==5):
#           print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

'''
1 2 3 4 5
1       5
1       5
1       5
1 2 3 4 5

'''

# for i in range(1, 6):
#     for j in range(1, 6-i):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if(j==1 or j==2*i-1):
#           print(j, end=" ")
#         else:
#            print(" ", end=" ")
#     print()
# for i in range(4, 0, -1):
#     for j in range(5, i, -1):
#         print(" ", end=" ")
#     for j in range(1, 2*i):
#         if(j==1 or j==2*i-1):
#           print(j, end=" ")
#         else:
#            print(" ", end=" ")
#     print()

''''
        1 
      1   3
    1       5
  1           7
1               9
  1           7
    1       5
      1   3
        1

'''

# for i in range(1, 6):
#   for j in range(1, i+1):
#     if(j==1 or j==i or i==5):
#       print(j, end=' ')
#     else:
#       print(" ", end=' ')
#   print()

'''
1 
1 2
1   3
1     4
1 2 3 4 5
'''

# for i in range(5, 0, -1):
#   for j in range(1, i+1):
#     if(j==1 or j==i or i==5):
#       print(j, end=' ')
#     else:
#       print(" ", end=' ')
#   print()

'''
1 2 3 4 5 
1     4
1   3
1 2
1

'''

for i in range(1, 5):
  for j in range(i, 4):
    print(" ", end=" ")
  for j in range(1, i+1):
    if(j==1 or j==i):
      print(j, end=' ')
    else:
      print(" ", end=' ')
  print()
for i in range(1, 4):
  for j in range(1, i+1):
    print(" ", end=" ")
  for j in range(1, 5-i):
    if(j==1 or j==i):
      print(j, end=' ')
    else:
      print(" ", end=' ')
  print()

