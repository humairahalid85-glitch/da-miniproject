import pandas as pd

# Load dataset
df = pd.read_csv('data/survey.csv')

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show basic info
print("\nData Info:")
print(df.info())
# --- Data Cleaning ---

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Remove missing values (if any)
df.dropna(inplace=True)

# --- Basic Statistics ---
print("\nBasic Statistics:")
print(df.describe())
import matplotlib.pyplot as plt
import seaborn as sns

# --- Graph 1: Satisfaction Distribution ---
plt.figure()
sns.histplot(df['Satisfaction'], kde=True)
plt.title("Customer Satisfaction Distribution")
plt.xlabel("Satisfaction")
plt.ylabel("Count")
plt.savefig("plots/satisfaction.png")
plt.show()

# --- Graph 2: Service Quality vs Satisfaction ---
plt.figure()
sns.boxplot(x='ServiceQuality', y='Satisfaction', data=df)
plt.title("Service Quality vs Satisfaction")
plt.savefig("plots/service_vs_satisfaction.png")
plt.show()
from scipy.stats import f_oneway

# Group data by Service Quality
groups = [group['Satisfaction'].values for name, group in df.groupby('ServiceQuality')]

# Perform ANOVA test
stat, p = f_oneway(*groups)

print("\nHypothesis Test Result:")
print("P-value:", p)

# Decision
if p < 0.05:
    print("Reject Null Hypothesis → Service Quality affects Satisfaction")
else:
    print("Fail to Reject Null → No significant effect")

print("\n--- FINAL INSIGHTS ---")

# Average satisfaction
avg = df['Satisfaction'].mean()
print(f"Average Satisfaction: {avg:.2f}")

# Best factor (simple check)
print("Higher Service Quality leads to higher Satisfaction (observed from graphs)")

print("Hypothesis Test Conclusion:")
if p < 0.05:
    print("Service Quality significantly affects Customer Satisfaction")
else:
    print("Service Quality does NOT significantly affect Customer Satisfaction")