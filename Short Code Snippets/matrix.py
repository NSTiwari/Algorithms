r = int(input("Enter the no. of rows: "))
c = int(input("Enter the no. of columns: "))
matrix = []
for i in range(r):
	a = []
	for j in range(c):
		a.append(int(input("Enter element: ")))
	matrix.append(a)

for i in range(r):
	for j in range(c):
		print(matrix[i][j], end=' ')
	print()
