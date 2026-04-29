from pymongo import MongoClient
from urllib.parse import quote_plus
import logging

def upload_to_mongo(df):
    """
    Uploads the processed dataset into a MongoDB collection.
    Prevents duplicate inserts and logs connection status.
    """

    #Upload to MongoDB
    data = df.to_dict("records")

    try:
        username = quote_plus("MONGODB_USERNAME")
        password = quote_plus("MONGODB_PASSWORD")

        uri = f"mongodb+srv://{username}:{password}@diabetics.049ou64.mongodb.net/?appName=Diabetics"

        client = MongoClient(uri)

        db = client["diabetics-db"]
        collection = db["readmissions"]

        logging.info("Connected to MongoDB")

        #Avoid duplicate inserts on reruns
        if collection.count_documents({}) == 0:
            collection.insert_many(data)

        logging.info("Data inserted into MongoDB")
        print("Data inserted into MongoDB")

    except Exception as e:
        logging.error(f"MongoDB error: {e}")
