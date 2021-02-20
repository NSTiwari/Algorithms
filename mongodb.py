from pymongo import MongoClient

ip = '127.0.0.1'
port = 27017

dbName = input("Enter database name: ")
print("Database "+dbName+" is created.", '\n')  
collectionName = input("Enter collection name: ")
print("Collection "+collectionName+" is created.", '\n')

client = MongoClient(ip, port)
db = client[dbName]

print("1. Insert")
print("2. Update")
print("3. Read")
print("4. Delete")
print("5. Search", '\n')

option = int(input("Select one of the option: "))
print()

if(option==1):

	dictionary = {}
	n = int(input("Enter the no. of fields in collection: "))
	
	id_num = input("Enter ID: ")
	print()
	dictionary['_id']=id_num
	for i in range(n):
		keys=input("Enter field"+str(i+1)+": ")
		values=input("Enter value"+str(i+1)+": ")
		#values=list(map(str,input("Enter value"+str(i+1)+": ").split()))
		print()
		dictionary[keys]=values

	#print(dictionary)
	db[collectionName].insert_one(dictionary)
	print("Recorded inserted successfully.")

	'''result = db[collectionName].fetch({})

	for i in result:
		print(i)'''

'''if(option==3):
	result = db[collectionName].fetch({})
	for i in result:
		print(i)'''
