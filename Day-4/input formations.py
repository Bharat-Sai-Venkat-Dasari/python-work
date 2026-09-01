Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Input Formations:')
Input Formations:
#int float str list tuple set dict
    
name = input('Enter your name: ')
Enter your name: Madhava
name
'Madhava'
age = int(input('Enter the age: '))
Enter the age: 21
age
21
price = float(input('Enter the price: '))
Enter the price: 79.99
price
79.99
cart = input('Enter the items: ').split()
Enter the items: Eggs Bread Butter Milk
cart
['Eggs', 'Bread', 'Butter', 'Milk']
prices = list(map(int, input('Enter the prices: ').split()))
Enter the prices: 30 45 40 10
prices
[30, 45, 40, 10]
discount = list(float(float, input('Enter the discount: ').split()))
Enter the discount: 5.0 5.0 20.0 0.0
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    discount = list(float(float, input('Enter the discount: ').split()))
TypeError: float expected at most 1 argument, got 2
discount = list(map(float, input('Enter the discount: ').split()))
Enter the discount: 5.0 5.0 20.0 0.0
discount
[5.0, 5.0, 20.0, 0.0]
t = tuple(input().split())
1 2 3 4 5
t
('1', '2', '3', '4', '5')
t = tuple(map(int, input().split()))
1 2 3 4 5
t
(1, 2, 3, 4, 5)
t = tuple(map(float, input().split()))
1 2 3
t
(1.0, 2.0, 3.0)
s = set(input().split())
1 2 3 4 5 1
s
{'5', '1', '2', '3', '4'}
s = set(map(int, input().split()))
1 2 3 4 2 1 5
s
{1, 2, 3, 4, 5}
s = set(map(float, input().split()))
1 2 3 4 5 1 2
s
{1.0, 2.0, 3.0, 4.0, 5.0}
a, b = [1, 2]
a
1
b
2
email, password = input('Enter the email and password: ').split()
Enter the email and password: bharat@gmail.com 12345
email
'bharat@gmail.com'
password
'12345'
a,b,c = list(map(int, input().split()))
1 2 3
a
1
b
2
c
3
name, marks = input('Enter the name and marks:').split()
Enter the name and marks:krishna 100
name
'krishna'
marks
'100'
>>> int(marks)
100
>>> e = eval(input())
7
>>> e
7
>>> e = eval(input())
7.8
>>> e
7.8
>>> e = eval(input())
Hello
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> e
7.8
>>> e = eval(input())
True
>>> e
True
>>> e = eval(input())
[1, 2, 3]
>>> e
[1, 2, 3]
>>> e = eval(input())
(1, 2, 3)
>>> e
(1, 2, 3)
>>> e = eval(input())
{1, 2, 1, 3, 2}
>>> e
{1, 2, 3}
>>> e = eval(input())
{name: 'Bharat'}
>>> e
{'krishna': 'Bharat'}
