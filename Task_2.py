import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv('lung cancer.csv')   
# ==========================================
# Task 2: Country-wise Cancer Stage Distribution
# ==========================================

# Creating a percentage distribution table of cancer stages
# for each country

pcountry = pd.crosstab(
    df['country'],
    df['cancer_stage'],
    normalize='index'
) * 100

# Randomly selecting 5 countries

rcountries = pcountry.sample(8)

# Plotting the graph

rcountries.plot(
    kind='bar',
    stacked=False,
    figsize=(12, 6),
    color=["#4EABE9", '#48C9B0', '#F4D03F', '#EB984E']
)

# Adding graph title and labels

plt.title(
    'Percentage Distribution of Cancer Stages by Selected Countries',
    fontsize=20
)

plt.xlabel(
    'Country Name',
    fontsize=12
)

plt.ylabel(
    'Stage Percentage (%)',
    fontsize=20
)

plt.legend(
    title='Stage',
    bbox_to_anchor=(1, 1)
)

# Rotating country names

plt.xticks(rotation=90)

# Displaying the graph

plt.show()
print("=" * 60)
print("Percentage Distribution of Cancer Stages by Country")
print("=" * 60)

print(rcountries.round(2))

print("=" * 60)

print("Highest percentage stage in each country:")
print("=" * 60)

for country in rcountries.index:
    max_stage = rcountries.loc[country].idxmax()
    max_percent = rcountries.loc[country].max()

    print(
        f"{country}: {max_stage} "
        f"({max_percent:.2f}%)"
    )