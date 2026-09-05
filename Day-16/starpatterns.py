# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n-i):
#         print("*", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(1, n+1):
#     print("  " * (n-i) + "* " * (i))

# n = int(input("Enter the size: "))
# for i in range(n):
#     print("  " * (i) + "* " * (n-i))

# n = int(input("Enter the size: "))
# for i in range(n):
#     if i == 0 or i == n-1:
#         print('* ' * n)
#     else:
#         print("* " + "  " * (n-2) + "* ")

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or j == n-1 or i == n-1):
#             print('*', end=" ")
#         elif j == (n//2) or i == (n//2):
#             print('*', end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == j or i+j == n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input('Enter the size: '))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or j == n-1 or i == (n//2)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or i == n-1 or j == n-1 or i == n//2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or i == n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or i == n-1 or j == n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or i == n-1 or i == n//2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or i == n//2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = int(input("Enter the size: "))
# mid = n//2
# for i in range(n):
#     for j in range(n):
#         if (i == 0 or j == 0 or (i == n-1 and j <= mid) or (j == mid and i >= mid) or (i == mid and j >= mid) or (j == n-1 and i >= mid)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# n = int(input('Enter the size: '))
# for i in range(1, n+1):
#     print('* ' + "  " * (n-i) + "*")
# for i in range(1, n):
#     print("* " + "  " * (i) + "*")

