# for i in range(1, 11):
#     print(i)

# s = 'Python Programming'
# for i in range(len(s)):
#     if s[i] in 'aeiouAEIOU':
#         print(s[i], i)

# l = (23, 45, 12, 34, 50, 24, 35, 68, 75, 34, 10)
# total = 0
# for i in range(len(l)):
#     if l[i] % 2 == 0:
#         total += i
#         print(i, l[i])
# print(total)

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)
# n = int(input('Enter the number: '))
# print(fact(n))

# n = int(input("Enter the number: "))
# prod = 1
# for i in range(1, n+1):
#     prod *= i
# print(f'Factorial of {n} is: {prod}')

# stu_details = eval(input("Enter the student details: "))

# for key, value in stu_details.items():
#     print(f'{key}: {value}')

# n = int(input("Enter the number of students: "))
# data = {}
# max_marks = 0
# min_marks = 0
# for i in range(n):
#     name = input("Enter the name: ")
#     marks = int(input("Enter the marks: "))
#     if max_marks < marks:
#         max_marks = marks
#     if max_marks > marks:
#         min_marks = marks
#     data[name] = marks
# print(f'Maximum marks: {max_marks}')
# print(f'Minimum marks: {min_marks}')

n = int(input("Enter the number of products: "))
total = 0
data = {}
for i in range(n):
    product_name = input("Enter the product name: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    data[product_name] = {
        'price: ': price,
        'quantity': quantity
    }
    print(data)
    total += price * quantity
print(f'Total price: {total}')