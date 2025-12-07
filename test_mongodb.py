from pymongo import MongoClient

uri = "mongodb+srv://ankityaduvansh1rao9818_db_user:Ankit98@cluster0.uj5am6l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
finally:
    client.close()

# write in terminal python test_mongodb.py
