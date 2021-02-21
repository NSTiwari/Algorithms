dictionary = {}
n = int(input("Enter the no. of key-value pairs: "))
print()
for i in range(n):
	key = input("Enter key"+str(i+1)+": ")
	value = input("Enter value"+str(i+1)+": ")
	print()
	dictionary[key] = value

print(dictionary)