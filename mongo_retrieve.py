from pymongo import MongoClient
from urllib.parse import quote_plus
import pandas as pd
import logging

def load_from_mongo():
    """
    Retrieves dataset from MongoDB and converts it into a pandas DataFrame.
    """

    #Load data from MongoDB into DataFrame
    try:
        username = quote_plus(MONGODB_USERNAME)
        password = quote_plus(MONGODB_PASSWORD)

        uri = f"mongodb+srv://{username}:{password}@diabetics.049ou64.mongodb.net/?appName=Diabetics"

        client = MongoClient(uri)

        db = client["diabetics-db"]
        collection = db["readmissions"]

        df = pd.DataFrame(list(collection.find()))
        df = df.reset_index(drop=True)

        logging.info("Data loaded from MongoDB")

    except Exception as e:
        logging.error(f"Error loading from MongoDB: {e}")
