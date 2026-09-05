#From 1 to N
# def display(n):
#     if n > 10:
#       return
#     print(n)
#     display(n+1)
# display(1)


#From N to 1
# def display(n):
#     if n > 10:
#       return
#     display(n+1)
#     print(n)
# display(1)

#Sum of N numbers
# def display(n):
#    if n == 0:
#       return 0
#    return n + display(n-1)

# print(display(5))

#Product of N numbers
# def display(n):
#    if n == 0:
#       return 1
#    return n * display(n-1)

# print(display(3))

#Factorial of a Number
# def display(n):
#    if n == 0:
#       return 1
#    return n * display(n-1)

# print(display(5))

#Iterate the String
# def display(i):
#     if i == len(s):
#         return
#     print(s[i], end="")
#     display(i+1)

# s = 'Python Programming'
# display(0)

#Iterate the String in reverse order
# def display(i):
#     if i == len(s):
#         return
#     display(i+1)
#     print(s[i], end="")

# s = 'Python Programming'
# display(0)

# def display(i):
#     if i == len(s):
#         return
#     print(s[:i+1])
#     display(i+1)

# s = 'Python'
# display(0)


# def display(i, j):
#     if i > len(s)-j:
#         return
#     print(s[i:i+j])
#     display(i+1, j)

# s = 'Python'
# display(0, 3)


def display(n):
    if n == 0:
        return
    display(n//10)
    print(n%10)

display(98765)