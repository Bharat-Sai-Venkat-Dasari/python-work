Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=7
>>> b=14
>>> c=21
>>> a
7
>>> b
14
>>> c
21
>>> a=b=c=7
>>> a
7
>>> b
7
>>> c
7
>>> a,b,c = 7,14,21
>>> a
7
>>> b
14
>>> c
21
>>> a,b = b,a
>>> a
14
>>> b
7
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
