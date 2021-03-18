from itertools import combinations
l = [1,2,3,4]

# Method 1: Using list comprehension.
t = [(a,b) for idx, a in enumerate(l) for b in l[idx+1:]]
print(t)

# Method 2: Using combinations package.
u = list(combinations(l,2))
print(u)