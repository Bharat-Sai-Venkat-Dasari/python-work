# def display(n):
#     n = n + 10
#     print('Inside: ', n)

# n = 10 #Global Variable
# display(n)
# print("Outside: ", n)

# def display():
#     print('Inside: ', n)

# n = 10 #Global Variable
# display()
# print("Outside: ", n)

# def display():
#     n = 10 #Local Variable
#     print('Inside: ', n)

# display()
# print("Outside: ", n)

# def display():
#     global n
#     n = n + 10
#     print('Inside: ', n)

# n = 10
# display()
# print("Outside: ", n)


# def display(n):
#     n = 'PFS'
#     print("Updated Course: ", n)

# n = 'JFS'
# display(n)
# print("Final Course: ", n)



# def display():
#     global n
#     n = 'PFS'
#     print("Updated Course: ", n)

# n = 'JFS'
# display()
# print("Final Course: ", n)


# def display():
#     n = 'JFS'
#     def update():
#         n='PFS'
#         print("Updated Course: ", n)
#     update()
#     print("Final Course: ", n)
# display()


def display():
    n = 'JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated Course: ", n)
    update()
    print("Final Course: ", n)
display()