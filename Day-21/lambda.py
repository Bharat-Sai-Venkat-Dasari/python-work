# greater = lambda a,b: a if a > b else b
# print(greater(6, 2))

# wish = lambda name: f'Welcome to the course {name}!'
# print(wish('Krishna'))

# iseven = lambda n: 'Even' if n % 2 == 0 else 'Odd'
# print(iseven(10))

# avg = lambda a,b,c: (a+b+c)//3
# print(avg(1,2,3))


# domain = lambda mail: mail.split('@')[-1].split('.')[0]
# print(domain('bharat@gmail.com'))
# print(domain('bharat@yahoo.com'))
# print(domain('bharat@outlook.com'))


# domain = lambda mail: mail.rstrip('.com').split('@')[-1]
# print(domain('bharat@gmail.com'))
# print(domain('bharat@yahoo.com'))
# print(domain('bharat@outlook.com'))


# gst = lambda price: price + price * 0.18
# print(gst(1000))
# print(gst(5000))
# print(gst(8000))


# prices = [5678, 3456, 67357, 4566, 4566, 3467]
# res = list(map(lambda price: price + price * 0.18, prices))
# print(res)


# names = ['krishna', 'madhava', 'kesava']
# res = list(map(lambda names: names.title(), names))
# print(res)


# prices = [5678, 3456, 67357, 4566, 4566, 3467]
# res = list(map(lambda price: price - price * 0.30, prices))
# print(res)


# prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(filter(lambda price: price % 2 == 0, prices))
# print(res)

# names = ['krishna', 'madhava', 'Hari', 'kesava', 'sai']
# res = list(filter(lambda lenght: len(lenght) > 5, names))
# print(res)

from functools import reduce
# l = [3, 4, 5, 67, 234]
# res = reduce(lambda sum, i: sum+i, l)
# print(res)


# names = ['krishna', 'madhava', 'Hari', 'kesava', 'sai']
# res = reduce(lambda res, i: res+" "+i, names)
# print(res)


products = {'sugar': 60, 'salt': 50, 'eggs': 90, 'cooking oil': 120, 'bread': 45}
print(dict(sorted(products.items(), key = lambda i:i[1])))
print(dict(sorted(products.items(), key = lambda i:i[1], reverse=True)))