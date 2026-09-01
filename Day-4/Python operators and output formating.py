Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Arthimetic operators:')
Arthimetic operators:
a = 20
b = 10
a + b
30
a - b
10
a * b
200
a / b
2.0
a // b
2
a ** b
10240000000000
a % b
0
print('Comparison opertors:')
Comparison opertors:
a = 20
b = 10
a > b
True
a < b
False
a >= b
True
a <= b
False
a == b
False
a != b
True
print('Assignment operators:')
Assignment operators:
c = 10
c += 10
c
20
c -= 10
c
10
c *= 10
c
100
c /= 10
c
10.0
c //= 10
c
1.0
c **= 10
c
1.0
c %= 10
c
1.0
c &= 10
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c &= 10
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
c = 10
c &= 10
c
10
c = 10
c |= 10
c
10
c = 10
c ^= 10
c
0
c = 10
c >>= 2
c
2
c = 10
c <<= 2
c
40
c := 10
SyntaxError: invalid syntax
print(c := 10)
10
print('Relational (or) Logical operators:')
Relational (or) Logical operators:
a = 10
a > 5 and a < 15
True
a > 5 and a < 10
False
a > 10 and a < 7
False
a > 5 or a < 15
True
a > 5 or a < 8
True
a > 15 or a < 5
False
a > 5
True
not a > 5
False
print('Membership operators:')
Membership operators:
collection_of_elements = ['str', 'list', 'tuple', 'set', 'dict']
collection_of_elements
['str', 'list', 'tuple', 'set', 'dict']
s = 'Madhava'
'a' in s
True
'b' in s
False
'b' not in s
True
'M' not in s
False
l = [1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
2 in l
True
6 in l
False
8 not in l
True
5 not in l
False
t = (1, 2, 3, 4, 5)
t
(1, 2, 3, 4, 5)
3 in t
True
6 in t
False
6 not in t
True
s = {1, 2, 3, 4, 5}
s
{1, 2, 3, 4, 5}
1 in s
True
6 in s
False
5 not in s
False
d = {'name': 'Krishna', age: 10000, 'location': 'universe'}
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d = {'name': 'Krishna', age: 10000, 'location': 'universe'}
NameError: name 'age' is not defined
d = {'name': 'Krishna', 'age': 100000, 'location':'universe'}
d
{'name': 'Krishna', 'age': 100000, 'location': 'universe'}
'name' in d
True
'location' in d
True
10000 in d
False
10000 not in d
True
'Krishna' not in d
True
print('Identity operators:')
Identity operators:
l = [1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
m = [1, 2, 3, 4, 5]
m
[1, 2, 3, 4, 5]
id(l)
2070653257984
id(m)
2070653259904
l is m
False
m is l
False
l is not m
True
m is not l
True
n = l
n
[1, 2, 3, 4, 5]
id(n)
2070653257984
l is n
True
l is not n
False
print('Bitwise operators:')
Bitwise operators:
9 & 10
8
9 | 10
11
9 ^ 10
3
>>> 8 << 2
32
>>> 8 >> 3
1
>>> ~8
-9
>>> ~69
-70
>>> print('Output formating:')
Output formating:
>>> a = 10
>>> b = 7.2
>>> c = 'Madhava'
>>> print(a, b, c)
10 7.2 Madhava
>>> print('a value:', a, 'b value:',b, 'c value:', c)
a value: 10 b value: 7.2 c value: Madhava
>>> print(a, b, c, sep=',')
10,7.2,Madhava
>>> print(a, b, c, sep='| ')
10| 7.2| Madhava
>>> print(a,b,c,sep='\n')
10
7.2
Madhava
>>> print(a,b,c,sep='\t')
10	7.2	Madhava
>>> print(a,b,c,end='$')
10 7.2 Madhava$
>>> print(a,b,c,sep='\t',end='\n\n')
10	7.2	Madhava

>>> print(f'a={a} | b={b} | c={c}')
a=10 | b=7.2 | c=Madhava
>>> print(f'a = {} | b = {b} | c = {c}'.format(a,b,c))
SyntaxError: f-string: empty expression not allowed
>>> print(f'a = %d | b = %f | c = %s'%(a,b,c))
a = 10 | b = 7.200000 | c = Madhava
>>> print(f'a = {} | b = {} | c = {}'.format(a,b,c))
SyntaxError: f-string: empty expression not allowed
>>> print('a = {} | b = {} | c = {}'.format(a,b,c))
a = 10 | b = 7.2 | c = Madhava
>>> print(f'a value is: {a} | b value is: {b} | c value is: {c}')
a value is: 10 | b value is: 7.2 | c value is: Madhava
