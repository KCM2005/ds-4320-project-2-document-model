# DS 4320 Project 2: Predicting Hospital Readmission Risks

# Executive Summary
This project analyzed hospital readmission risk (within 30 days) among diabetic patients by primary diagnosis and gender using descriptive analysis, feature engineering, and logistic regression modeling. Descriptive analysis of observed outcomes identified the most common primary diagnoses associated with readmission, including conditions such as heart failure, stroke, and chronic bronchitis, with small variations in readmission rates between male and female patients across diagnosis groups. To further investigate risk patterns, ICD-9 diagnosis codes were transformed into clinically meaningful disease categories, and a logistic regression model was trained to predict the probability of 30-day readmission. The model generated predicted risk estimates based on patient features, allowing comparison of estimated readmission likelihood across the top 10 diagnoses and between genders. A bar chart was used to visualize observed (empirical) readmission rates across diagnoses and genders, enabling interpretation of the dataset's real outcome distributions. In addition, a line plot was used during model evaluation to visualize predicted readmission probabilities, highlighting how estimated risk varies across diagnoses and between male and female patients. The results show that readmission risk varies across both diagnosis categories and gender groups. The combination of descriptive analysis and predictive modeling demonstrates that while observed outcomes highlight common high-volume conditions, the logistic regression model provides additional insight into how risk is distributed across patient groups, supporting more targeted clinical understanding of readmission patterns.
 

# Name
Kalenga Mumba

# NetID
kew6jk

# DOI
[DOI](https://doi.org/10.5281/zenodo.19906831)

# Press release
[Press release](https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/Press_release.md)

# Pipeline
[Pipeline](https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/Pipeline.ipynb)

# License
MIT License: [https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/LICENSE](https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/LICENSE)

## Initial general problem
Predicting hospital readmission risk

## Refined specific problem
Analyzing within 30-day readmission risk for diabetes-related primary diagnoses in American diabetic patients by gender

## Motivation
Diabetic patients frequently present with multiple comorbidities (which are additional medical conditions/diseases that occur simultaneously with a primary condition or disease in an individual). For example, research shows that patients with  diabetes (primary condition) also tend to have hypertension and kidney disease (comorbidities) (Swamy et al, 2023). These co-occurring conditions can impact the treatment, management, and outcome of the primary condition. Therefore, identifying the primary diabetes-related diagnoses is crucial for understanding hospital readmission drivers. Therefore, analysing the primary comorbidities that lead to a within 30-day readmission risk enables targeted interventions, ultimately reducing healthcare costs and improving patient outcomes by mitigating readmissions (Rubin et al, 2021). 

References:
Swamy, Sowmya et al. “Cardiovascular Disease in Diabetes and Chronic Kidney Disease.” Journal of clinical medicine vol. 12,22 6984. 8 Nov. 2023, doi:10.3390/jcm12226984

Rubin, Daniel J, and Arnav A Shah. “Predicting and Preventing Acute Care Re-Utilization by Patients with Diabetes.” Current diabetes reports vol. 21,9 34. 4 Sep. 2021, doi:10.1007/s11892-021-01402-7


## Rationale
Focusing on primary comorbidities is crucial because diabetic patients often present with multiple co-occurring conditions that significantly impact treatment, management, and outcomes. By identifying and analyzing these comorbidities, the data scientists can uncover key drivers of within 30-day readmissions and develop targeted interventions to mitigate risks, reduce healthcare costs, and improve patient outcomes. This approach enables data-driven care optimization and personalized treatment strategies.

## Headline and link to press release
Headline: Targeting the within 30-day hospital readmissions: Top 10 key diabetes-related primary diagnoses by gender unveiled

Link: https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/Press_release.md

## Terminology
| Term / KPI        | Description                                                | Relevance to Domain                                                 |
| ----------------- | ---------------------------------------------------------- | ------------------------------------------------------------------- |
| readmitted        | Indicates whether a patient was readmitted after discharge | Primary outcome variable for 30-day readmission risk analysis       |
| diag_1            | Primary diagnosis code at admission                        | Core predictor representing main disease condition                  |
| gender            | Patient gender                                             | Key demographic variable for subgroup analysis                      |
| age               | Patient age group                                          | Important confounder affecting health outcomes and readmission risk |
| race              | Patient race                                               | Demographic factor for population-level disparity analysis          |
| time_in_hospital  | Number of days spent in hospital                           | Proxy for illness severity and treatment complexity                 |
| num_medications   | Number of medications prescribed                           | Indicates treatment intensity and patient condition severity        |
| number_inpatient  | Number of previous inpatient visits                        | Strong predictor of future readmission risk                         |
| number_emergency  | Number of emergency visits                                 | Reflects acute health instability and prior complications           |
| number_outpatient | Number of outpatient visits                                | Captures ongoing disease management outside hospital                |
| A1Cresult         | HbA1c test result                                          | Measures long-term glucose control and diabetes severity            |
| diabetesMed       | Whether diabetes medication was prescribed                 | Indicates treatment status influencing outcomes                     |

## Domain explanation
This project lives in the domain of healthcare analytics, specifically analyzing readmission risk for diabetic patients. It leverages Electronic Health Record (EHR) data and machine learning to analyze the within 30-day hospital readmission across diabetes-related primary diagnoses (comorbidities) by gender. By identifying patterns in these data, the project aims to predict 30-day readmission risk, enabling targeted interventions to improve patient outcomes.

## Background Reading
https://github.com/KCM2005/ds-4320-project-2-document-model/tree/main/Background%20readings

## Summary of readings table
| Title                                                                                                            | Brief Description                                                                                                                                                                                                                                                                                                                 | Link                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hospital Readmission Risk and Risk Factors of People with a Primary or Secondary Discharge Diagnosis of Diabetes | Rubin et al (2023) found that patients with a primary diagnosis of diabetes have a higher 30-day readmission rate (22.2%) compared to those with a secondary diagnosis (16.2%). The study suggests inpatient diabetes consultation may be more effective in reducing readmissions for patients with a primary diabetes diagnosis. | [https://pmc.ncbi.nlm.nih.gov/articles/PMC9961750/pdf/jcm-12-01274.pdf](https://pmc.ncbi.nlm.nih.gov/articles/PMC9961750/pdf/jcm-12-01274.pdf)                                                                                                                                                 |
| Diabetes Mellitus and Prevalence of Other Comorbid Conditions: A Systematic Review                               | Bodke et al (2023) reveals common comorbidities including UTIs, tuberculosis, sepsis, and hypertension. Risk varies by age, genetics, and lifestyle factors.                                                                                                                                                                      | [https://pmc.ncbi.nlm.nih.gov/articles/PMC10749406/pdf/cureus-0015-00000049374.pdf](https://pmc.ncbi.nlm.nih.gov/articles/PMC10749406/pdf/cureus-0015-00000049374.pdf)                                                                                                                         |
| Cardiovascular Disease in Diabetes and Chronic Kidney Disease                                                    | Swamy et al (2023) highlights that CKD occurs in about 40% of diabetes cases and significantly increases cardiovascular disease risk.                                                                                                                                                                                             | [https://pmc.ncbi.nlm.nih.gov/articles/PMC10672715/pdf/jcm-12-06984.pdf](https://pmc.ncbi.nlm.nih.gov/articles/PMC10672715/pdf/jcm-12-06984.pdf)                                                                                                                                               |
| Identification and Predictors for Cardiovascular Disease Risk Equivalents among Adults With Diabetes Mellitus    | Zhao et al (2021) found that about one-fifth of CVD-free adults with diabetes have risk equivalent to those with established CVD. Predictors include high HbA1c, long duration, and medication use.                                                                                                                               | [https://diabetesjournals.org/care/article-abstract/44/10/2411/138552/Identification-and-Predictors-for-Cardiovascular?redirectedFrom=fulltext](https://diabetesjournals.org/care/article-abstract/44/10/2411/138552/Identification-and-Predictors-for-Cardiovascular?redirectedFrom=fulltext) |
| The Mental Health Comorbidities of Diabetes                                                                      | Ducat et al (2014) highlights increased risk of depression, anxiety, and eating disorders in diabetes patients, impacting treatment adherence and quality of life.                                                                                                                                                                | [https://pmc.ncbi.nlm.nih.gov/articles/PMC4439400/pdf/nihms684855.pdf](https://pmc.ncbi.nlm.nih.gov/articles/PMC4439400/pdf/nihms684855.pdf)                                                                                                                                                   |

## Raw Data Acquisition
The dataset originated from the University of California at Irvine (UCI) Machine Learning Repository website (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008), which contains de-identified data from 130 U.S. hospitals (1999-2008) on diabetic patients, including demographics, diagnoses, medications, and 30-day readmission outcomes. The dataset was formatted into a CSV file, comprising 101, 766 patient encounters.

My refined specific problem for Project 2 is: Analyzing the within 30-day risk of primary diagnoses readmission in American diabetic patients by gender. As such, the raw data acquisition process (provenance) involved the following steps. First, I went to the UCI Machine Learning Repository website (https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008). Second, I searched for “diabetes” in the search box, and selected “Diabetes130-US Hospitals for Years 1999-2008”. Third, I clicked on the “download” button, and downloaded the dataset consisting of 101,766 records (rows) in CSV format. Lastly, I loaded the dataset into MongoDB via mongoimport.

## Code Table
| File / Step        | Description                                                                                                              | Link / Source                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| diabetic_data.csv  | Raw dataset from UCI containing diabetic patient encounters used as input data                                           | [https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) |
| load_dataset.py    | Loads the diabetics dataset into a pandas DataFrame for initial exploration                                              | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/load_data.py                                                                                                                                                       |
| clean_data.py      | Performs core data cleaning (handling missing values, correcting data types, removing duplicates, basic normalization)   | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/clean_data.py                                                                                                                                      |
| mongo_upload.py    | Uploads the cleaned dataset into MongoDB for persistent storage and querying                                             | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/mongo_upload.py                                                                                                 |
| mongo_retrieve.py  | Retrieves dataset from MongoDB and converts it back into a pandas DataFrame for downstream analysis                      | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/mongo_retrieve.py                                                                                                                                                       |
| data_processing.py | Handles advanced transformations and feature engineering (e.g., 30-day readmission flag, diagnosis categorization)       | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/data_processing.py                                                                                                                                                       |
| visualization.py   | Performs analysis (e.g., readmission risk by diagnosis and gender) and generates visualizations such as charts and plots | https://github.com/KCM2005/ds-4320-project-2-document-model/blob/main/visualization.py                                                                                                                                                       |

## Bias Identification
- Selection bias: Data only includes hospitalized diabetic patients (1999-2008), excluding outpatient cases or those not seeking care.

- Geographic bias: Data is from 130 U.S. hospitals, and may not represent global diabetes patient demographics.

- Time period bias: Data is outdated (from 1999-2008), which may not reflect current diabetes treatment/management practices or patient demographics.

- Measurement bias: Variations in hospital data collection/recording practices across the 130 hospitals may affect data consistency.

- Socioeconomic bias: Limited representation of uninsured or underinsured patients may skew results.

- Data Quality Bias: Missing values and potential errors in data extraction (e.g., during the de-identification process may have removed relevant information) may both impact analysis.

## Bias Mitigation
Selection Bias:

- Weighting: Apply weights to match national diabetes prevalence rates.

Geographic Bias:

- Stratification: Given the 130 hospitals, could be analyzed by location of hospitals or hospital type or hospital size.

Time Period Bias:

- Data Augmentation: Incorporate more recent data.

Measurement Bias:

- Data Harmonization: Standardize variables across the 130 hospitals if possible.
- Stratification: Analyze by hospital or data collection practices.

Socioeconomic Bias:

- Weighting: Adjust for insurance status.
- Stratification: Analyze subgroups by socioeconomic factors.

Data Quality Bias:

- Data Validation: Check for inconsistencies and outliers.
- Imputation: Handle missing values appropriately (e.g., multiple imputation).
- Sensitivity Analysis: Assess impact of missing/de-identified data.

## Rationale of critical decisions
Data Inclusion Criteria:

- Decision: Include all diabetic patients (1999-2008) from all U.S. hospitals.
- Uncertainty: Excluding some patients (e.g., non-hospitalized) may introduce bias.
- Mitigation: Apply weighting or data augmentation.

Variable Selection:

- Decision: Focus on demographics, insulin usage, time in hospital, and readmission risk.
- Uncertainty: Omitting relevant variables (e.g., socioeconomic status, insurance) may introduce bias.
- Mitigation: Include relevant variables if available.

Modeling Approach:

- Decision: Choose a model (e.g., logistic regression, random forest).
- Uncertainty: Model choice can impact results.
- Mitigation: Compare multiple models and use ensemble methods.

Handling Missing Data:

- Decision: Impute missing values.
- Uncertainty: Imputation methods can introduce uncertainty.
- Mitigation: Use multiple imputation methods and compare results.

## Implicit Schema
| Top-level field  | Data type | How to interpret (with examples)                                        |
| ---------------- | --------- | ----------------------------------------------------------------------- |
| _id              | string    | Unique MongoDB document ID                                              |
| encounter_id     | integer   | Hospital visit ID (e.g. 149190)                                         |
| patient_nbr      | integer   | Patient ID (same patient may appear multiple times)                     |
| age              | string    | Age ranges such as [0-10), [20-30), [70-80)                             |
| gender           | string    | Male or Female                                                          |
| race             | string    | Race category (e.g. Caucasian, African American, Asian, Hispanic, Other) |
| diag_1           | string    | Primary diagnosis ICD-9 code (e.g. 414 = heart disease)                 |
| diag_2           | string    | Secondary diagnosis ICD-9 code (e.g. 250 = diabetes)                    |
| diag_3           | string    | Tertiary diagnosis ICD-9 code                                           |
| time_in_hospital | integer   | Number of days in hospital (e.g. 3 = 3 days)                            |
| num_medications  | integer   | Number of medications prescribed (e.g. 5 = 5 drugs)                     |
| number_emergency | integer   | Number of emergency visits (e.g. 1 = one visit)                         |
| number_inpatient | integer   | Number of prior inpatient admissions (e.g. 2 = two admissions)          |
| number_diagnoses | integer   | Total number of diagnoses recorded (e.g. 9 = nine diagnoses)            |
| insulin          | string    | No, Steady, Up, Down (insulin change status)                            |
| diabetesMed      | string    | Yes or No (whether diabetes medication was prescribed)                  |
| readmitted       | string    | <30 = within 30 days, >30 = after 30 days, No = not readmitted          |

## Data Summary Table
| Metric                   | Value                                                      |
| ------------------------ | ---------------------------------------------------------- |
| Number of records        | 101,766                                                    |
| Number of fields         | 17                                                         |
| Missing values handling  | Not allowed / replaced or removed (based on preprocessing) |
| Categorical fields       | 8                                                          |
| Numerical fields         | 9                                                          |
| Outcome variable         | readmitted                                                 |
| Outcome classes          | <30, >30, No                                         |
| Unit of analysis         | One hospital encounter per row                             |
| Patient-level uniqueness | patient_nbr (patient can repeat across rows)               |


## Data Dictionary 
| Name             | Data type | Description                      | Example                  |
| ---------------- | --------- | -------------------------------- | ------------------------ |
| _id              | String    | Unique document ID               | 507f1f77bcf86cd799439011 |
| encounter_id     | Integer   | Hospital visit ID                | 149190                   |
| patient_nbr      | Integer   | Patient ID                       | 8222157                  |
| age              | String    | Age group of patient             | [50-60)                  |
| gender           | String    | Patient gender                   | Female                   |
| race             | String    | Patient race                     | Caucasian                |
| diag_1           | String    | Primary diagnosis code           | 250.83                   |
| diag_2           | String    | Secondary diagnosis code         | 276                      |
| diag_3           | String    | Tertiary diagnosis code          | 401                      |
| time_in_hospital | Integer   | Number of hospital days          | 4                        |
| num_medications  | Integer   | Number of medications prescribed | 13                       |
| number_emergency | Integer   | Number of emergency visits       | 0                        |
| number_inpatient | Integer   | Number of inpatient visits       | 1                        |
| number_diagnoses | Integer   | Total diagnoses recorded         | 9                        |
| insulin          | String    | Insulin change status            | Steady                   |
| diabetesMed      | String    | Diabetes medication prescribed   | Yes                      |
| readmitted       | String    | Readmission status               | <30                      |

## Data Dictionary - Numerical Features
| Feature            | Data Type | Source of Uncertainty                                   | Quantification / Characterization of Uncertainty                                        |
| ------------------ | --------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| encounter_id       | Integer   | System-generated identifier                             | N/A (unique ID, no statistical uncertainty)                                             |
| patient_nbr        | Integer   | Repeated patient tracking across visits                 | N/A (identifier; variation reflects visit frequency, not measurement error)             |
| time_in_hospital   | Integer   | Differences in patient severity and discharge practices | Bounded (1–14 days); moderate variability due to clinical condition and hospital policy |
| num_lab_procedures | Integer   | Differences in testing intensity across hospitals       | Moderate variability; depends on patient condition and hospital protocols               |
| num_procedures     | Integer   | Variation in treatment decisions and coding practices   | Low-to-moderate variability; many zero values indicating no procedures                  |
| num_medications    | Integer   | Prescribing behavior and patient complexity             | Wide range (0–80+); right-skewed distribution indicating complex cases                  |
| number_outpatient  | Integer   | Inconsistent recording of outpatient visits             | Highly zero-inflated; many patients have no recorded outpatient visits                  |
| number_emergency   | Integer   | Rare emergency events and underreporting                | Extremely zero-inflated; few patients account for most values                           |
| number_inpatient   | Integer   | Prior admission history and incomplete records          | Strongly zero-inflated; most patients have no prior inpatient stays                     |
| number_diagnoses   | Integer   | Variation in clinical coding and comorbidities          | Moderate variability; higher values indicate more complex cases                         |
