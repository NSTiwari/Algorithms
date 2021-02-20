from pymongo import MongoClient
import json

def main():
	ip = '127.0.0.1'
	port = 27017

	dbName = input("Enter database name: ")
	print("Switched to database "+dbName+".", '\n')  
	collectionName = input("Enter collection name: ")
	print("Switched to collection "+collectionName+".", '\n')

	client = MongoClient(ip, port)
	db = client[dbName]

	while True:
		print()
		print("1. Insert")
		print("2. Update")
		print("3. Read")
		print("4. Delete")
		print("5. Find")
		print("6. Save Collection")
		print("7. Import Collection")
		print("8. Aggregation", '\n')

		option = int(input("Select one of the option: "))
		print()

		if(option==1):
			dictionary = {}
			n = int(input("Enter the no. of fields in record: "))
			data(dictionary, n)

			db[collectionName].insert_one(dictionary)
			print("Record inserted successfully.")

		if(option==2):
			update(db, collectionName)
			
			
		if(option==3):
		   read(db, collectionName)

		if(option==4):
			delete(db, collectionName)

		if(option==5):
			find(db, collectionName)

		if(option==6):
			save_collection(db, collectionName)

		if(option==7):
			import_collection(db, collectionName)

		if(option==8):
			aggregation(db, collectionName)


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


# Update records.
def update(db, collectionName):
	condition_dict = {}
	updated_dict = {}

	condition_field = input("Find record by: ")
	condition_value = input("Enter the "+condition_field+": ")
	print()
	condition_dict[condition_field] = condition_value

	n = int(input("Enter the no. of fields to be updated: "))
	for i in range(n):
		field_to_be_updated = input("Enter field"+str(i+1)+" to be updated: ")
		value_to_be_updated = input("Enter value"+str(i+1)+" to be updated: ")
		print()
		updated_dict[field_to_be_updated] = value_to_be_updated


	db[collectionName].update_one(
	condition_dict,
	{
	"$set": updated_dict
	})

	print("Record updated successfully.") 


# Delete records.
def delete(db, collectionName):
	condition_dict = {}
	condition_field = input("Delete record by: ")
	condition_value = input("Enter the "+condition_field+" to delete record(s)): ")
	condition_dict[condition_field] = condition_value
	db[collectionName].delete_many(condition_dict)
	print("Record(s) deleted successfully.")

# Find records.
def find(db, collectionName):
	condition_dict = {}
	condition_field = input("Find record by: ")
	condition_value = input("Enter the "+condition_field+" to find record(s): ")
	condition_dict[condition_field] = condition_value
	result = db[collectionName].find(condition_dict)
	for i in result:
		print(i)

# Save collection on disk.
def save_collection(db, collectionName):
	records = []
	collection_to_save = input("Enter the collection to be saved: ")
	result = db[collection_to_save].find({})
	for record in result:
		records.append(record)

	with open(collection_to_save+'.json', 'w') as fp:
		json.dump(records, fp)
		
	print("Collection "+collection_to_save+" is saved on disk.")


# Import collection in database from disk.
def import_collection(db, collectionName):

	# Load the collections.json file from local machine.
	collection_to_load = input("Enter the collection JSON file to be loaded into database: ")
	with open(collection_to_load+'.json') as fp:
		data = json.load(fp)

	new_collection = input("Enter the name of new collection: ")

	for i in range(len(data)):
		db[new_collection].insert_one(data[i])

	print("The collection "+new_collection+" is imported in database.")


# Compute Aggregation.
def aggregation(db, collectionName):
	aggregation_on = input("Enter the field to apply aggregation: ")
	result = db[collectionName].aggregate(
		[
			{ 
    			"$group": { 
      					   "_id": None, 
        					"total": {"$sum": {"$toInt": "$age"}},
        					"average": {"$avg":{"toInt": "$age"}},
        					"maximum": {"$max": {"toInt": "$age"}},
        					"minimum": {"$min": {"toInt": "$age"}}  
    					} 

			} 
		] 
	)
			

	for i in result:
		print(i)


if __name__=="__main__":
	main()

