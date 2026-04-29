import pandas as pd
import logging

logging.basicConfig(
    filename='project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(path="diabetic_data.csv"):
    """
    Loads the raw diabetic dataset from a CSV file.

    Parameters:
        path (str): Path to the dataset file

    Returns:
        pd.DataFrame: Loaded dataset as a pandas DataFrame
    """
    try:
        # Load CSV file into DataFrame
        df = pd.read_csv(path)

        # Reset index for consistency
        df = df.reset_index(drop=True)

        logging.info("Dataset loaded successfully")
        return df

    except Exception as e:
        logging.error(f"Load error: {e}")
        return None
