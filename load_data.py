#Loading dataset
import pandas as pd
import logging

logging.basicConfig(
    filename='project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_dataset():
    """
    Loads the diabetics dataset from a CSV file into a pandas DataFrame.
    Logs success or failure of the loading process.
    """
    try:
        df = pd.read_csv("diabetic_data.csv")
        df = df.reset_index(drop=True)
        logging.info("csv loaded successfully")
        print("CSV file loaded successfully")

    except Exception as e:
        logging.error(f"csv loading error: {e}")
