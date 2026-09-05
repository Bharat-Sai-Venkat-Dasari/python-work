Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("***DICT-2***")
***DICT-2***
>>> data = {'name': 'Madhava', 'batch': 7, 'course': 'PFS'}
>>> data
{'name': 'Madhava', 'batch': 7, 'course': 'PFS'}
>>> data['name']
'Madhava'
>>> data['bacth']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data['bacth']
KeyError: 'bacth'
>>> data['batch']
7
>>> data['course']
'PFS'
>>> 63 in data
False
>>> data.get('age', 'key is not present')
'key is not present'
>>> data.get('course', 'key is not present')
... 
'PFS'
data['batch'] = 5
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS'}
data['skills'] = ['Python', 'MySQL', 'flask']
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask']}
data['age'] = 21
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask'], 'age': 21}
data.update({'phone': 944-518235, 'email': 'bharatdasari777@gmail.com'})
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask'], 'age': 21, 'phone': -517291, 'email': 'bharatdasari777@gmail.com'}
data.pop('age')
21
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask'], 'phone': -517291, 'email': 'bharatdasari777@gmail.com'}
data.pop('phone')
-517291
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask'], 'email': 'bharatdasari777@gmail.com'}
del data['email']
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS', 'skills': ['Python', 'MySQL', 'flask']}
data.popitem()
('skills', ['Python', 'MySQL', 'flask'])
data
{'name': 'Madhava', 'batch': 5, 'course': 'PFS'}
data.clear()
data
{}
