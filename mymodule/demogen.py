import sys
wgl=[i**2 for i in range(1000000)]
g=(i**2 for i in range(1000000))
print(sys.getsizeof(wgl))
print(sys.getsizeof(g))