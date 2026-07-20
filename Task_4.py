import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('lung cancer.csv')  
# ==========================================
# Task 4 -> Comparing age distributions
# across smoking categories using boxplots
# and summary statistics
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assigning aliases

mpl = plt
sea = sns
a = df

# Setting up graph screen

mpl.figure(figsize=(10, 6))

# 'Set2' palette is used here for the colour scheme

sea.boxplot(
    x='smoking_status',
    y='age',
    data=a,
    palette='Set2',
    hue='smoking_status',
    legend=False
)

# Adding labels and title

mpl.title(
    'Comparison: Impact of Smoking on Different Age Groups',
    fontsize=22
)

mpl.xlabel(
    'Smoking Status',
    fontsize=20
)

mpl.ylabel(
    'Age at Diagnosis',
    fontsize=20
)

# Displaying graph

mpl.show()

# ==========================================
# Summary Statistics
# ==========================================

print("~/" * 60)

print("Average Age of Diagnosis by Smoking Category:")

print(
    a.groupby('smoking_status')['age'].mean()
)

print("~/" * 60)

# Optional: Mean, Median and Standard Deviation

print("\nDetailed Summary Statistics:\n")

print(
    a.groupby('smoking_status')['age'].agg(
        Mean='mean',
        Median='median',
        Std_Deviation='std'
    )
)