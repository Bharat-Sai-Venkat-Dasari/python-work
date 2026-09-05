Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> datatypes = ['int', 'float', 'complex', 'string', 'list', 'tuple', 'set', 'dict', 'boolean', 'None', 'frozenset']
>>> datatypes
['int', 'float', 'complex', 'string', 'list', 'tuple', 'set', 'dict', 'boolean', 'None', 'frozenset']
>>> a = 1
>>> a
1
>>> type(a)
<class 'int'>
>>> price = 79.99
>>> price
79.99
>>> type(price)
<class 'float'>
>>> c = 5 + 7J
>>> c
(5+7j)
>>> type(c)
<class 'complex'>
>>> name = 'Krishna'
>>> name
'Krishna'
>>> type(name)
<class 'str'>
>>> cart = ['Eggs', 'bread', 70, 7.9, [1, 2, 3], (1, 2, 3)]
>>> cart
['Eggs', 'bread', 70, 7.9, [1, 2, 3], (1, 2, 3)]
>>> type(cart)
<class 'list'>
>>> t = ('Eggs', 'bread', 'milk', 7, 7.3)
>>> t
('Eggs', 'bread', 'milk', 7, 7.3)
>>> type(t)
<class 'tuple'>
>>> s = {'Eggs', 7, 7.6, 'butter'}
>>> s
{7, 'butter', 'Eggs', 7.6}
type(s)
<class 'set'>
student_details = {'name': 'Madhava', 'age': 100000, 'location': 'universe}
                   
SyntaxError: unterminated string literal (detected at line 1)
student_details = {'name': 'Madhava', 'age': 1000000, 'location': 'universe'}
                   
student_details
                   
{'name': 'Madhava', 'age': 1000000, 'location': 'universe'}
type(student_details)
                   
<class 'dict'>
b = True
                   
b
                   
True
type(b)
                   
<class 'bool'>
stack = None
                   
stack
                   
type(stack)
                   
<class 'NoneType'>
f = frozenset({1, 2, 3, 4, 5, 1, 2, 3, 4, 5})
                   
f
                   
frozenset({1, 2, 3, 4, 5})
type(f)
                   
<class 'frozenset'>
