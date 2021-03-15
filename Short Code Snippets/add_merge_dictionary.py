from collections import Counter

d1 = Counter({'a':10, 'b':15, 'c':16})
d2 = Counter({'a': 20, 'b': 10, 'd': 999})
d = dict(d1+d2)
print(d)