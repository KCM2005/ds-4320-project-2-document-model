# pip install pymongo


```python
!pip install pymongo
```

    Collecting pymongo
      Downloading pymongo-4.17.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (10 kB)
    Collecting dnspython<3.0.0,>=2.6.1 (from pymongo)
      Downloading dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
    Downloading pymongo-4.17.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.8 MB)
    [?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/1.8 MB[0m [31m?[0m eta [36m-:--:--[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.8/1.8 MB[0m [31m75.3 MB/s[0m eta [36m0:00:00[0m
    [?25hDownloading dnspython-2.8.0-py3-none-any.whl (331 kB)
    [?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/331.1 kB[0m [31m?[0m eta [36m-:--:--[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m331.1/331.1 kB[0m [31m31.7 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: dnspython, pymongo
    Successfully installed dnspython-2.8.0 pymongo-4.17.0


# 1. Loading dataset


```python
#Loading dataset
import pandas as pd
import logging

logging.basicConfig(
    filename='project.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    df = pd.read_csv("diabetic_data.csv")
    df = df.reset_index(drop=True)
    logging.info("csv loaded successfully")
    print("CSV file loaded successfully")
except Exception as e:
    logging.error(f"csv loading error: {e}")
```

    CSV file loaded successfully


# 2. Upload dataset to MongoDB


```python
from pymongo import MongoClient
from urllib.parse import quote_plus
```


```python
#Upload to MongoDB
data = df.to_dict("records")

try:
    username = quote_plus("diabetics-db")
    password = quote_plus("B7W_qKfZFPt3uWD")

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
```

    Data inserted into MongoDB


# 3. Load data from MongoDB into a dataframe


```python
#Load data from MongoDB into DataFrame
try:
    df = pd.DataFrame(list(collection.find()))
    df = df.reset_index(drop=True)
    logging.info("Data loaded from MongoDB")
except Exception as e:
    logging.error(f"Error loading from MongoDB: {e}")

df.head()
```





  <div id="df-a179e33c-49b7-407a-9e3c-7096cee3ee47" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>_id</th>
      <th>encounter_id</th>
      <th>patient_nbr</th>
      <th>race</th>
      <th>gender</th>
      <th>age</th>
      <th>weight</th>
      <th>admission_type_id</th>
      <th>discharge_disposition_id</th>
      <th>admission_source_id</th>
      <th>...</th>
      <th>citoglipton</th>
      <th>insulin</th>
      <th>glyburide-metformin</th>
      <th>glipizide-metformin</th>
      <th>glimepiride-pioglitazone</th>
      <th>metformin-rosiglitazone</th>
      <th>metformin-pioglitazone</th>
      <th>change</th>
      <th>diabetesMed</th>
      <th>readmitted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>69dc2dea1c0ad742273a74f7</td>
      <td>149190</td>
      <td>55629189</td>
      <td>Caucasian</td>
      <td>Female</td>
      <td>[10-20)</td>
      <td>?</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>...</td>
      <td>No</td>
      <td>Up</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ch</td>
      <td>Yes</td>
      <td>&gt;30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>69dc2dea1c0ad742273a7506</td>
      <td>77076</td>
      <td>92519352</td>
      <td>AfricanAmerican</td>
      <td>Male</td>
      <td>[50-60)</td>
      <td>?</td>
      <td>1</td>
      <td>1</td>
      <td>7</td>
      <td>...</td>
      <td>No</td>
      <td>Steady</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ch</td>
      <td>Yes</td>
      <td>&lt;30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>69dc2dea1c0ad742273a7512</td>
      <td>250872</td>
      <td>41606064</td>
      <td>Caucasian</td>
      <td>Male</td>
      <td>[20-30)</td>
      <td>?</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>No</td>
      <td>Down</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ch</td>
      <td>Yes</td>
      <td>&gt;30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>69dc2dea1c0ad742273a7513</td>
      <td>252822</td>
      <td>18196434</td>
      <td>Caucasian</td>
      <td>Female</td>
      <td>[80-90)</td>
      <td>?</td>
      <td>1</td>
      <td>2</td>
      <td>7</td>
      <td>...</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ch</td>
      <td>Yes</td>
      <td>&gt;30</td>
    </tr>
    <tr>
      <th>4</th>
      <td>69dc2dea1c0ad742273a7518</td>
      <td>293118</td>
      <td>3327282</td>
      <td>Caucasian</td>
      <td>Female</td>
      <td>[70-80)</td>
      <td>?</td>
      <td>2</td>
      <td>11</td>
      <td>2</td>
      <td>...</td>
      <td>No</td>
      <td>Down</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>No</td>
      <td>Ch</td>
      <td>Yes</td>
      <td>NO</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-a179e33c-49b7-407a-9e3c-7096cee3ee47')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-a179e33c-49b7-407a-9e3c-7096cee3ee47 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-a179e33c-49b7-407a-9e3c-7096cee3ee47');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    </div>
  </div>




# 4. Data Cleaning


```python
#Data Cleaning
keep_cols = [
    'encounter_id',
    'patient_nbr',
    'age',
    'gender',
    'race',
    'diag_1',
    'diag_2',
    'diag_3',
    'time_in_hospital',
    'num_medications',
    'number_emergency',
    'number_inpatient',
    'number_diagnoses',
    'insulin',
    'diabetesMed',
    'readmitted'
]

df = df[keep_cols]

df.to_csv("cleaned_diabetic_data.csv", index=False)

#Calculate completeness
percentages = (df != "").sum() / len(df) * 100
types = df.dtypes

for field, pct in percentages.items():
    print(f"{field} ({types[field]}): {pct:.2f}%")
```

    encounter_id (int64): 100.00%
    patient_nbr (int64): 100.00%
    age (object): 100.00%
    gender (object): 100.00%
    race (object): 100.00%
    diag_1 (object): 100.00%
    diag_2 (object): 100.00%
    diag_3 (object): 100.00%
    time_in_hospital (int64): 100.00%
    num_medications (int64): 100.00%
    number_emergency (int64): 100.00%
    number_inpatient (int64): 100.00%
    number_diagnoses (int64): 100.00%
    insulin (object): 100.00%
    diabetesMed (object): 100.00%
    readmitted (object): 100.00%


# 5. Feature Engineering


```python
#Top 10 primary diagnoses
top_10_diag_codes = df['diag_1'].value_counts().head(10).index.tolist()
print(top_10_diag_codes)
```

    ['428', '414', '786', '410', '486', '427', '491', '715', '682', '434']



```python
#Feature Engineering
try:
    df['readmit_30'] = df['readmitted'] == '<30'

    def icd_to_disease(x):
        x = str(x)
        if x.startswith('410'): return "Heart Attack"
        elif x.startswith('414'): return "Ischemic Heart Disease"
        elif x.startswith('427'): return "Cardiac Dysrhythmias"
        elif x.startswith('428'): return "Heart Failure"
        elif x.startswith('434'): return "Stroke"
        elif x.startswith('486'): return "Pneumonia"
        elif x.startswith('491'): return "Chronic Bronchitis (COPD)"
        elif x.startswith('682'): return "Skin Infection"
        elif x.startswith('715'): return "Osteoarthritis"
        elif x.startswith('786'): return "Respiratory Symptoms"
        else: return x

    df['diag_name'] = df['diag_1'].apply(icd_to_disease)

    logging.info("Feature engineering complete")
    print("Feature engineering complete")

except Exception as e:
    logging.error(f"Feature engineering error: {e}")
```

    Feature engineering complete


# 6. Filter top 10 primary diagnoses


```python
#Filter top 10 diagnoses
try:
    top_diags = df['diag_name'].value_counts().head(10).index

    df_top = df[df['diag_name'].isin(top_diags)].copy()
    df_top = df_top[df_top['gender'] != 'Unknown/Invalid']

    logging.info("Filtered top 10 diagnoses")
    print("Filtered top 10 diagnoses")

except Exception as e:
    logging.error(f"Filtering error: {e}")
```

    Filtered top 10 diagnoses


# 7. Visualization


```python
#Visualization of <30 day readmission risk of top 10 diagnoses by gender
import matplotlib.pyplot as plt

try:
    rate_by_diag_gender = (
        df_top.groupby(['diag_name', 'gender'])['readmit_30']
        .mean()
        .unstack()
    )

    ax = rate_by_diag_gender.plot(
        kind='bar',
        figsize=(12, 7),
        color={'Female': 'pink', 'Male': 'blue'}
    )

    plt.title("Within 30-Day Readmission Risk by Diagnosis and Gender")
    plt.ylabel("Readmission Risk")
    plt.xlabel("Primary Diagnosis")
    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Gender")

    for container in ax.containers:
        labels = [f'{v*100:.1f}%' if v == v else '' for v in container.datavalues]
        ax.bar_label(container, labels=labels, padding=3, fontsize=8)

    plt.tight_layout()
    plt.show()

    logging.info("Bar chart created")

except Exception as e:
    logging.error(f"Visualization error: {e}")
```


    
![png](Pipeline_files/Pipeline_17_0.png)
    


# 8. Prepare data for model implementation


```python
#Preparing data for model implementation
import numpy as np

try:
    df_top["readmitted_binary"] = df_top["readmitted"].astype(str).str.strip()

    df_top["readmitted_binary"] = df_top["readmitted_binary"].apply(
        lambda x: 1 if x.startswith("<30") else 0 if x in [">30", "NO"] else np.nan
    )

    df_top = df_top.dropna(subset=["readmitted_binary"])

    X = df_top.drop(["readmitted", "readmitted_binary"], axis=1)
    y = df_top["readmitted_binary"]

    logging.info("Data prepared for modeling")
    print("Data prepared for modeling")

except Exception as e:
    logging.error(f"Model preparation error: {e}")
```

    Data prepared for modeling


# 9. Encoding and Train-Test split


```python
#Encoding and Train-Test split
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

try:
    categorical_cols = X.select_dtypes(include="object").columns
    le = LabelEncoder()

    for col in categorical_cols:
        X[col] = le.fit_transform(X[col].astype(str))

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    logging.info("Encoding and train-test split complete")
    print("Encoding and train-test split complete")

except Exception as e:
    logging.error(f"Error during encoding and train-test split: {e}")
```

    Encoding and train-test split complete


# 10. Fit logistic regression model


```python
#Implementing and fitting a logistic regression model to training data
from sklearn.linear_model import LogisticRegression

try:
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train, y_train)

    logging.info("Model trained successfully")
    print("Model trained successfully")

except Exception as e:
    logging.error(f"Training error: {e}")
```

    Model trained successfully


# 11. Evaluation


```python
#Evaluation
from sklearn.metrics import accuracy_score, mean_squared_error

#Generate predictions
try:
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    #Compute metrics (accuracy, MSE, and RMSE)
    accuracy = accuracy_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)

    print("Accuracy:", accuracy)
    print("MSE:", mse)
    print("RMSE:", rmse)

    logging.info(f"Model evaluation complete")

except Exception as e:
    logging.error(f"Evaluation error: {e}")
```

    Accuracy: 0.41112191772984724
    MSE: 0.5888780822701527
    RMSE: 0.7673839210396272


# 12. Visualization of model evaluation results


```python
#Line plot showing model evaluation results
import matplotlib.pyplot as plt

try:
    results = X_test.copy()
    results["predicted_prob"] = y_prob

    results["diag_name"] = df_top.loc[X_test.index, "diag_name"]
    results["gender"] = df_top.loc[X_test.index, "gender"]

    #Group data results
    line_df = results.groupby(
        ["diag_name", "gender"]
    )["predicted_prob"].mean().reset_index()

    plt.figure(figsize=(12, 6))

    #Plot separately for each gender
    for gender in line_df["gender"].unique():
        subset = line_df[line_df["gender"] == gender]

        plt.plot(
            subset["diag_name"],
            subset["predicted_prob"],
            marker='o',
            label=gender,
            color="blue" if gender == "Male" else "red"
        )

    plt.title(f"Within 30-Day readmission risk of primary diagnosis by gender (Model Accuracy: {accuracy:.2f})")
    plt.xlabel("Primary Diagnosis")
    plt.ylabel("Mean Predicted Readmission Risk (<30 days)")

    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Gender")

    plt.tight_layout()
    plt.show()

    logging.info("Visualization successfully created")

except Exception as e:
    logging.error(f"Error generating visualization: {e}")
```


    
![png](Pipeline_files/Pipeline_27_0.png)
    


## Analysis rationale

Logistic regression was chosen due to its suitability for binary classification tasks and its interpretability in estimating the probability of 30-day hospital readmission (yes/no outcome). The original primary diagnosis variables, encoded using ICD-9 codes, were transformed into clinically meaningful disease categories to improve interpretability and reduce sparsity in the feature space. This transformation allowed clearer communication of how the top 10 most frequent primary diagnoses influence readmission risk among diabetic patients. Specifically, the top diagnoses include Cardiac Dysrhythmias (427), Chronic Bronchitis/COPD (491), Heart Attack (410), Heart Failure (428), Ischemic Heart Disease (414), Osteoarthritis (715), Pneumonia (486), Respiratory Symptoms (786), Skin Infection (682), and Stroke (434). Gender was included as an additional covariate to assess potential disparities in readmission risk across demographic groups. The logistic regression model estimates how these features collectively influence the likelihood of readmission within 30 days. Model performance was evaluated using accuracy and predicted probabilities were used to compare risk across diagnosis and gender groups. This approach supports both predictive performance and interpretability, enabling identification of high-risk patient groups for targeted intervention.


## Visualization rationale

I chose to use bar graphs comparing the top 10 primary diagnoses by gender for three reasons: (a) To visualize trends in the within 30-day readmission rates across primary diagnosis categories. In this case, “primary diagnosis” is treated as a categorical variable ordered by overall observed readmission risk. By plotting actual readmission rates along the y-axis and the top 10 diagnoses along the x-axis, I am able to clearly see which diagnosis categories are associated with higher or lower observed readmission risk for each gender. (b) To compare gender differences within each diagnosis based on observed outcomes, allowing direct comparison of readmission rates between male and female patients for the same diagnosis, such as whether males with circulatory diagnoses show higher readmission rates than females with the same condition. (c) To identify specific diagnosis categories where gender differences in observed readmission rates are largest, highlighting potential disparities that may warrant further investigation. Additionally, I also implemented a line plot during model evaluation to visualize predicted within 30-day readmission probabilities generated by the logistic regression model. This allowed for effective comparison of model-estimated risk across the same top 10 diagnoses among males and females, helping assess how predicted risk patterns align with observed trends.

