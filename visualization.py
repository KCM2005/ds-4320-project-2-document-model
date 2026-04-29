#Visualization of <30 day readmission risk of top 10 diagnoses by gender 
import matplotlib.pyplot as plt
import logging

def visualize_readmission(df_top):
    """
    Creates a bar chart showing within 30-day readmission risk
    by diagnosis and gender using grouped aggregation.
    """

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

        logging.info("Visualization created")

    except Exception as e:
        logging.error(f"Visualization error: {e}")
