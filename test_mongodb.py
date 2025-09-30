from pymongo import MongoClient

# Replace <db_password> with your actual password
uri = "mongodb+srv://ankityaduvansh1rao9818_db_user:Ankit98@cluster0.uj5am6l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
finally:
    # Close the client when done
    client.close()
