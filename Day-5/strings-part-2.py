Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c = 'strings.py'
>>> c.startswith('str')
True
>>> c.startswith('Python')
False
>>> s.endswith('.py')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.endswith('.py')
NameError: name 's' is not defined
>>> c.endswith('.py')
True
>>> c.islower()
True
>>> c.isupper()
False
>>> 'PYTHONV13'.isupper()
True
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> c.isspace()
False
>>> ' '.isspace()
True
>>> c.istitle()
False
>>> 'Python Is Easy To Learn'.istitle()
True
>>> 'Python is east to learn'.istitle()
False
>>> c.isidentifier()
False
>>> 'variable1'.isidentifier()
True
