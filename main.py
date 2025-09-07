import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Define subject lines and preheader texts
subject_lines = ['Subject A', 'Subject B', 'Subject C']
preheader_texts = ['Preheader A', 'Preheader B', 'Preheader C']
# Generate synthetic data
num_emails = 1000
data = {
    'Subject': np.random.choice(subject_lines, size=num_emails),
    'Preheader': np.random.choice(preheader_texts, size=num_emails),
    'Opened': np.random.binomial(1, 0.2, size=num_emails) # 20% open rate on average
}
df = pd.DataFrame(data)
# --- 2. Data Analysis ---
# Calculate open rates for each subject/preheader combination
open_rates = df.groupby(['Subject', 'Preheader'])['Opened'].mean().unstack()
# Find the best performing combination
best_combination = open_rates.stack().idxmax()
best_open_rate = open_rates.stack().max()
print("Open Rates for each Subject/Preheader combination:\n", open_rates)
print(f"\nBest performing combination: {best_combination} with an open rate of {best_open_rate:.2%}")
# --- 3. Visualization ---
plt.figure(figsize=(10, 6))
sns.heatmap(open_rates, annot=True, fmt=".2%", cmap="YlGnBu", cbar_kws={'label': 'Open Rate'})
plt.title('Email Open Rates by Subject Line and Preheader Text')
plt.xlabel('Preheader Text')
plt.ylabel('Subject Line')
plt.tight_layout()
# Save the plot to a file
output_filename = 'open_rates_heatmap.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
#Further analysis (example - could be expanded)
# Chi-squared test for independence between Subject and Opened
from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df['Subject'], df['Opened'])
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-squared test for Subject and Opened:\nChi-squared statistic: {chi2:.2f}\nP-value: {p:.3f}")
#Similar analysis could be done for Preheader and Opened.