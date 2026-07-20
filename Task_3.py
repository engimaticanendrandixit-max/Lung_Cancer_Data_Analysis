import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('lung cancer.csv')  
# ==========================================
# Task 3 -> Selecting treatment type on the basis of cancer stage
# ==========================================

# Assigning alias

mpl = plt
a = df

# Setting up graph screen

mpl.figure(figsize=(12, 7))

# "hue" helps us group patients from different stages
# to determine the treatment type through the graph.
# 'Set2' palette is used for the colour scheme.

sns.countplot(
    x='cancer_stage',
    hue='treatment_type',
    data=a,
    order=['Stage I', 'Stage II', 'Stage III', 'Stage IV'],
    palette='Set2'
)

# Labelling and title block for the graph

mpl.title(
    'Distribution of Treatment Types by Cancer Stage',
    fontsize=14
)

mpl.xlabel(
    'Cancer Stage',
    fontsize=12
)

mpl.ylabel(
    'Number of Patients',
    fontsize=12
)

mpl.legend(
    title='Treatment Type',
    bbox_to_anchor=(1.05, 1),
    loc='upper left'
)

# Display graph

mpl.show()

print("=" * 60)

# Distribution of patients under each treatment type and cancer stage

print("Exact counts for each treatment per stage:")

print("=" * 60)

print(
    pd.crosstab(
        a['cancer_stage'],
        a['treatment_type']
    )
)