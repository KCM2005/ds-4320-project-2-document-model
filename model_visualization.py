#Line plot showing model evaluation results
import matplotlib.pyplot as plt

def plot_model_evaluation(X_test, y_prob, df_top, accuracy):
    """
    Creates a line plot showing the predicted within 30-day readmission risk
    by primary diagnosis and gender using the logistic regression model outputs.
    """

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
