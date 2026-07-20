import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('lung cancer.csv') 
# ==========================================
# Task 5 -> To analyse Multimorbidity
# among the patients
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assigning aliases

mpl = plt
sea = sns
a = df

# List of diseases considered

diseases = [
    'hypertension',
    'asthma',
    'cirrhosis',
    'other_cancer'
]

# Counting the number of diseases present
# ('yes' or 1 are treated as positive cases)

a['illness_count'] = a[diseases].apply(
    lambda x: (x == 'yes') | (x == 1)
).sum(axis=1)

# Setting up the graph screen

mpl.figure(figsize=(10, 6))

sea.countplot(
    x='illness_count',
    hue='illness_count',
    data=a,
    palette='viridis',
    legend=False
)

# Displaying disease names on the graph

mpl.text(
    1.05,
    0.6,
    "Diseases:\n- Hypertension\n- Asthma\n- Cirrhosis\n- Other Cancer",
    transform=mpl.gca().transAxes,
    bbox=dict(
        boxstyle='square',
        facecolor='white'
    )
)

# Graph title and labels

mpl.title('Multimorbidity Count (0–4)')

mpl.xlabel('Number of Additional Diseases')

mpl.ylabel('Patient Count')

# Display graph

mpl.show()

# ==========================================
# Summary of Results
# ==========================================

print("=" * 40)

print("--- SUMMARY OF RESULTS ---")

print("=" * 40)

print("Patient count by number of diseases:")

result = a['illness_count'].value_counts().sort_index()

print(result)

print("\nTotal Patients:", len(a))

print("=" * 40)

print(
    "0 means No Other Disease",
    "\n1 means One Other Disease",
    "\n2 means Two Other Diseases",
    "\n3 means Three Other Diseases",
    "\n4 means Four Other Diseases"
)
print("=" * 40)