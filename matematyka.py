import math
import sys

print(sys.argv)  # ['C:\\Users\\cmkz\\PycharmProjects\\python_06-1011203\\matematyka.py']
# po uruchomieniu programu parametry mamy wypisany ten parametr


pi = math.pi
print(pi)  # 3.141592653589793

print(math.sqrt(625))  # 25.0
print(math.cos(90))

print(dir())
print([x for x in dir() if not x.startswith('_')])
# ['math', 'pi', 'sys'] wypisał użyte zmienne w tym programie

