string = input("Enter the text to encrypt: ")
n = int(input("Enter the value to be shifted: "))
encrypted = ''

for i in range(len(string)):
	letter = string[i]
	if(letter.islower()):
		encrypted += chr((ord(letter)-97 + n) % 26 + 97)
	else:
		encrypted += chr((ord(letter)-65 + n) %26 + 65)

print(encrypted)