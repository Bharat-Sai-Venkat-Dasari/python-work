Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('***LIST***')
***LIST***
>>> print('List is a collection of elements which is enclosed between ([])sqaure brackets.')
List is a collection of elements which is enclosed between ([])sqaure brackets.
>>> print('List Properties:\n1.Ordered\n2.Mutable\n3.Allow duplicates\n4.Heterogenous\n5.Dynamic')
List Properties:
1.Ordered
2.Mutable
3.Allow duplicates
4.Heterogenous
5.Dynamic
>>> l = []
>>> l = list()
>>> l = [2, 2.3, 10+1j, 'Bharat', [1, 2, 3], (4, 5, 6), {1, 2, 3}]
>>> l
[2, 2.3, (10+1j), 'Bharat', [1, 2, 3], (4, 5, 6), {1, 2, 3}]
>>> l = [1, 2, 3]
>>> m = [4, 5, 6]
>>> l + m
[1, 2, 3, 4, 5, 6]
>>> l * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> l[-1]
3
>>> l[::-1]
[3, 2, 1]
>>> 3 in l
True
>>> 5 not in l
True
