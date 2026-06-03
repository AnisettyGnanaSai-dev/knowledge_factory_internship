import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df = sns.load_dataset("titanic")

print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

#age distrubution

fig, axes = plt.subplots(
    2,
    2,
    figsize=(14,10)
)
corr = df.select_dtypes(
    include="number"
).corr()
sns.histplot(
    data=df,
    x="age",
    kde=True,
    ax=axes[0,0]
)

sns.boxplot(
    data=df,
    x="survived",
    y="age",
    ax=axes[0,1]
)

sns.countplot(
    data=df,
    x="sex",
    hue="survived",
    ax=axes[1,0]
)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=axes[1,1]
)

plt.suptitle(
    "Titanic EDA Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    "Titanic_dashboard.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()