import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('lung cancer.csv')            #Reading Data of Lung Cancer Patients from the uploaded file

print('Lung Cancer Patients Data\n',df.head())  #Printing Data of Patients to Check wether connection is established or not
'''=====================================================================================================================
                   This Shows that the program is working fine and the connection is established successfully
========================================================================================================================='''
# ==========================================
# Task 1: Age at Diagnosis vs Cancer Stage
# ==========================================
# Display column names (optional)

print("Columns in dataset:")
print(df.columns)
# ------------------------------------------------
# Calculate mean and median age for each stage
# ------------------------------------------------

age_statistics = df.groupby("cancer_stage")["age"].agg(
    Mean_Age="mean",
    Median_Age="median"
)

print("\nMean and Median Age by Cancer Stage:\n")
print(age_statistics)

# ------------------------------------------------
# Boxplot for Age at Diagnosis vs Cancer Stage
# ------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(
    x="cancer_stage",
    y="age",
    data=df
)
plt.title("Age at Diagnosis vs Cancer Stage")
plt.xlabel("Cancer Stage")
plt.ylabel("Age")
plt.show()
# ------------------------------------------------
# Violin Plot
# ------------------------------------------------
plt.figure(figsize=(8, 5))
sns.violinplot(
    x="cancer_stage",
    y="age",
    data=df
)
plt.title("Age Distribution Across Cancer Stages")
plt.xlabel("Cancer Stage")
plt.ylabel("Age")
plt.show()