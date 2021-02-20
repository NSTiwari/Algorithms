from pymongo import MongoClient

def main():
	ip = '127.0.0.1'
	port = 27017

	dbName = input("Enter database name: ")
	print("Switched to database "+dbName+".", '\n')  
	collectionName = input("Enter collection name: ")
	print("Switched to collection "+collectionName+".", '\n')

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
		data(dictionary, n)

		db[collectionName].insert_one(dictionary)
		print("Recorded inserted successfully.")
		
		
	if(option==3):
	   read(db, collectionName)



# Get input data from user.
def data(dictionary, n):
	id_num = input("Enter ID: ")
	print()
	dictionary['_id'] = id_num
	for i in range(n):
		keys = input("Enter field"+str(i+1)+": ")
		values=input("Enter value"+str(i+1)+": ")
		print()
		dictionary[keys] = values

# Read all data from the collection.
def read(db, collectionName):
	result = db[collectionName].find({})
	for i in result:
		print(i)



if __name__=="__main__":
	main()

