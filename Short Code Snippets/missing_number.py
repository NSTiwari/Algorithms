l = [1, 3, 4, 8, 12]
missing = [x for x in range(l[0], l[-1]+1) if x not in l]
print(missing)