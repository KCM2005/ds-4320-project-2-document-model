import pandas as pd
import logging

logging.basicConfig(
    filename='project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data():
    """
    Loads the raw diabetic dataset from a CSV file into a pandas DataFrame.
    Logs success or failure of the loading process.
    """

    #Loading dataset
    try:
        df = pd.read_csv("diabetic_data.csv")
        df = df.reset_index(drop=True)
        logging.info("csv loaded successfully")
        print("CSV file loaded successfully")
        return df

    except Exception as e:
        logging.error(f"csv loading error: {e}")
        return None
