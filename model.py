import numpy as np
import logging

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, mean_squared_error

def train_model(df):
    """
    Implements logistic regression model to predict 30-day readmission.
    Handles encoding, splitting, training, and evaluation.
    """

    try:
        #Target variable
        df["readmitted_binary"] = df["readmitted"].astype(str).str.strip()

        df["readmitted_binary"] = df["readmitted_binary"].apply(
            lambda x: 1 if x.startswith("<30") else 0 if x in [">30", "NO"] else np.nan
        )

        #Features and target
        X = df.drop(["readmitted", "readmitted_binary"], axis=1, errors="ignore")
        y = df["readmitted_binary"]

        #Encode categorical variables
        categorical_cols = X.select_dtypes(include="object").columns
        le = LabelEncoder()

        for col in categorical_cols:
            X[col] = le.fit_transform(X[col].astype(str))

        #Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        #Logistic Regression Model
        model = LogisticRegression(max_iter=1000, class_weight="balanced")
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        #Evaluation Metrics
        accuracy = accuracy_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)

        logging.info(f"Model trained. Accuracy: {accuracy}")

        return X_test, y_test, y_pred, accuracy

    except Exception as e:
        logging.error(f"Model error: {e}")
