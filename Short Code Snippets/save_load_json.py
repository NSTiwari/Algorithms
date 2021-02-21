import json


# Create a dictionary.
dictionary_to_save = {}
n = int(input("Enter the no. of key-value pairs: "))
print()

for i in range(n):
	key = input("Enter key"+str(i+1)+": ")
	value = input("Enter value"+str(i+1)+": ")
	print()
	dictionary_to_save[key] = value


# Save dictionary as JSON.
save_dictionary_as = input("Save the dictionary as: ")
with open(save_dictionary_as+'.json', 'w') as fp:
		json.dump(dictionary_to_save, fp)
print("Dictionary is saved as "+save_dictionary_as+".json.")
print()


# Load JSON as dictionary.
load_json = input("Enter the JSON file to be loaded: ")
with open(load_json+'.json') as fp:
		data = json.load(fp)

print(data)