# os.getcwd() Returns the current working directory
# os.chdir(path) Changes the current working directory
# os.listdir(path) Returns a list of files and folders in a directory
# os.mkdir(name) Creates a new directory
# os.remove(file) Deletes a specified file
# os.rmdir(dir) Removes an empty directory
# os.path.exists(path) Checks if a path exists

# import os
# # os.mkdir('demo')
# # os.rmdir('demo')
# # print(os.getcwd())
#-----------------------------------------------------------------------------------
# sys.argv List of command-line arguments
# sys.exit() Exits the program
# sys.path List of paths for module search
# sys.version Returns the Python version

# import sys
# print(sys.version)
# print(sys.argv)
# print(sys.path)
# print(sys.exit)
#-----------------------------------------------------------------------------------
# platform.system() Returns OS name (e.g., Windows, Linux)
# platform.release() OS release version
# platform.processor() Returns processor type

# import platform
# print(platform.system())
# print(platform.release())
# print(platform.processor())
#-----------------------------------------------------------------------------------
# math.pi π = 3.14159...
# math.e Euler’s number ≈ 2.718
# math.sqrt(x) Returns the square root of x
# math.pow(x, y) x raised to the power y (x^y)
# math.ceil(x) Smallest integer ≥ x
# math.floor(x) Largest integer ≤ x
# math.fabs(x) Absolute value of x
# math.factorial(x) Factorial of x (x!)
# math.gcd(x, y) Greatest common divisor
# math.log(x, base) Logarithm of x to the given base
# math.sin(x) Sine of x (x in radians)
# math.cos(x) Cosine of x
# math.tan(x) Tangent of x
# math.degrees(x) Convert radians to degrees
# math.radians(x) Convert degrees to radians

# import math
# print(math.pi)
# print(math.e)
# print(math.sqrt(36))
# print(math.pow(2,3))
# print(math.ceil(12.00001))
# print(math.floor(12.9999))
# print(math.fabs(-12))
# print(math.factorial(5))
# print(math.gcd(8,24))
# print(math.log(10,10))
# print(math.sin(30))
# print(math.cos(30))
# print(math.tan(30))
# print(math.degrees(1))
# print(math.radians(1))
#-----------------------------------------------------------------------------------
# random.random() Returns a float in the range [0.0, 1.0)
# random.randint(a, b) Returns random integer between a and b (inclusive)
# random.uniform(a, b) Returns a float between a and b
# random.choice(seq) Returns a random element from a non-empty sequence
# random.choices(seq,k=n) Returns a list of k random elements from seq
# random.shuffle(list) Shuffles the list in place
# random.seed(n) Sets the seed for reproducibility

# import random
# print(random.random())
# print(random.randint(20,30))
# print(random.randint(10000, 999999))
# print(random.uniform(2,3))
# print(random.choice(['Bharat', 'Avinash', 'Lokesh', 'Ganesh', 'Narasimha', 'Vikas', 'Anil']))
# print(random.choices(['Bharat', 'Avinash', 'Lokesh', 'Ganesh', 'Narasimha', 'Vikas', 'Anil'], k=4))
# print(random.shuffle(['Bharat', 'Avinash', 'Lokesh', 'Ganesh', 'Narasimha', 'Vikas', 'Anil']))
# print(random.seed(34))
#-----------------------------------------------------------------------------------
# Counter Counts frequency of elements
# defaultdict Dictionary with default values
# deque Double-ended queue for fast appends/pops

# from collections import Counter, defaultdict, deque

# s = 'Python Programming'
# m = 'this is that that is this is is this that'.split()
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 123, 234, 43, 123, 12, 41, 789]
# # print(Counter(s))
# # print(Counter(l))
# # print(Counter(m))

# # d = {}
# # for i in s:
# #     d[i] = d.get(i, 0) + 1
# # print(d)

# # d = defaultdict(int)
# # for i in s:
# #     d[i] += 1
# # print(d)

# l = deque([])
# l.append(10)
# l.append(20)
# l.append(30)
# l.popleft()
# l.popleft()
# l.append(50)
# l.append(70)
# l.popleft()
# l.appendleft(40)
# print(l)
#-----------------------------------------------------------------------------------
# combinations(iter, r) r-length tuples, combinations without replacement
# permutations(iter, r) r-length tuples, all possible orderings

from itertools import combinations, permutations

res1 = list(combinations('abc', 2))
res2 = list(permutations('abc', 2))

# print(res1)
# print(res2)

print(["".join(x) for x in res2])
print(["".join(x) for x in res1])