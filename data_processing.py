import logging

def process_data(df):
    """
    Performs data cleaning, feature selection, completeness calculation,
    and ICD-9 diagnosis mapping for analysis.
    """

    #Keep necessary columns
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

    # Calculate completeness
    percentages = (df != "").sum() / len(df) * 100
    types = df.dtypes

    for field, pct in percentages.items():
        print(f"{field} ({types[field]}): {pct:.2f}%")

    #Create 30-day readmission threshold
    df['readmit_30'] = df['readmitted'] == '<30'

    #Convert ICD-9 codes to disease groups
    def icd_to_disease(x):
        x = str(x)

        if x.startswith('410'):
            return "Heart Attack"
        elif x.startswith('414'):
            return "Ischemic Heart Disease"
        elif x.startswith('427'):
            return "Cardiac Dysrhythmias"
        elif x.startswith('428'):
            return "Heart Failure"
        elif x.startswith('434'):
            return "Stroke"
        elif x.startswith('486'):
            return "Pneumonia"
        elif x.startswith('491'):
            return "Chronic Bronchitis (COPD)"
        elif x.startswith('682'):
            return "Skin Infection"
        elif x.startswith('715'):
            return "Osteoarthritis"
        elif x.startswith('786'):
            return "Respiratory Symptoms"
        else:
            return x

    try:
        df['diag_name'] = df['diag_1'].apply(icd_to_disease)
        logging.info("ICD mapping complete")

    except Exception as e:
        logging.error(f"ICD mapping error: {e}")
