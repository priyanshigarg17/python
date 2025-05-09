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

# print("", end='')
# for i in range(4, 0, -1):
#   for j in range(1, i+1):
#     print("*", end='')
  
#   for j in range(1, (6 - i) * 2):
#     print(" ", end="")

#   # Right triangle
#   for j in range(1, i+1):
#     print('*', end="")
  
#   print()

for i in range(1, 5):
    for j in range(1, 5-i):
        print("-", end=" ")
    for j in range(1, i+1):
        if j == 1 or i == 4 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()