Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
datatypes = ['int', 'float', 'complex', 'string', 'list', 'tuple', 'set', 'dict', 'boolean']
dataypes
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    dataypes
NameError: name 'dataypes' is not defined. Did you mean: 'datatypes'?
datatypes
['int', 'float', 'complex', 'string', 'list', 'tuple', 'set', 'dict', 'boolean']
a = 7
a
7
float(a)
7.0
complex(a)
(7+0j)
str(a)
'7'
list(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
f = 7.5
f
7.5
int(f)
7
complex(f)
(7.5+0j)
str(f)
'7.5'
list(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True
complex = 7 + 5j
complex
(7+5j)
int(complex)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(complex)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
c = 7 + 5j
c
(7+5j)
int(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(7+5j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
name = 'Vasudeva'
name
'Vasudeva'
int(name)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(name)
ValueError: invalid literal for int() with base 10: 'Vasudeva'
float(name)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(name)
ValueError: could not convert string to float: 'Vasudeva'
complex(name)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex(name)
TypeError: 'complex' object is not callable
list(name)
['V', 'a', 's', 'u', 'd', 'e', 'v', 'a']
tuple(name)
('V', 'a', 's', 'u', 'd', 'e', 'v', 'a')
set(name)
{'u', 'V', 'v', 'e', 'a', 'd', 's'}
dict(name)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    dict(name)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(name)
True
l = [7, 7.5, 'Vasudeva', True]
l
[7, 7.5, 'Vasudeva', True]
int(l)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    complex(l)
TypeError: 'complex' object is not callable
str(l)
"[7, 7.5, 'Vasudeva', True]"
tuple(l)
(7, 7.5, 'Vasudeva', True)
set(l)
{True, 7.5, 'Vasudeva', 7}
dict(l)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t = (7, 5.7, 'Krishna', False)
t
(7, 5.7, 'Krishna', False)
int(t)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    complex(t)
TypeError: 'complex' object is not callable
str(t)
"(7, 5.7, 'Krishna', False)"
list(t)
[7, 5.7, 'Krishna', False]
set(t)
{'Krishna', False, 5.7, 7}
dict(t)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s = {7, 3.4, 'Jaganadh', True}
s
{'Jaganadh', True, 3.4, 7}
int(s)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    complex(s)
TypeError: 'complex' object is not callable
str(s)
"{'Jaganadh', True, 3.4, 7}"
list(s)
['Jaganadh', True, 3.4, 7]
tuple(s)
('Jaganadh', True, 3.4, 7)
dict(s)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 8; 2 is required
bool(s)
True
d = {'name': 'Krish', 'age': 100000, 'location': 'universe'}
d
{'name': 'Krish', 'age': 100000, 'location': 'universe'}
int(d)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    complex(d)
TypeError: 'complex' object is not callable
str(d)
"{'name': 'Krish', 'age': 100000, 'location': 'universe'}"
list(d)
['name', 'age', 'location']
tuple(d)
('name', 'age', 'location')
>>> set(d)
{'name', 'location', 'age'}
>>> bool(d)
True
>>> b = True
>>> b
True
>>> int(b)
1
>>> float(b)
1.0
>>> complex(b)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    complex(b)
TypeError: 'complex' object is not callable
>>> str(b)
'True'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    list(b)
TypeError: 'bool' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    tuple(b)
TypeError: 'bool' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    set(b)
TypeError: 'bool' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    dict(b)
TypeError: 'bool' object is not iterable
