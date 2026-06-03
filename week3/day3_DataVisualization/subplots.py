import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

fig, axes = plt.subplots(
    2,
    2,
    figsize=(12,10)
)

axes[0,0].hist(
    df["petal_length"],
    bins = 20
)

axes[0,0].set_title("Petal length Disturbation")

sns.boxplot(
    data=df,
    x="species",
    y="petal_length",
    ax=axes[0,1]
)

axes[0,1].set_title(
    "Boxplot by Species"
)

# Scatter
sns.scatterplot(
    data=df,
    x="petal_length",
    y="petal_width",
    hue="species",
    ax=axes[1,0]
)

axes[1,0].set_title(
    "Scatter Plot"
)

# Heatmap
sns.heatmap(
    df.corr(
        numeric_only=True
    ),
    annot=True,
    cmap="coolwarm",
    ax=axes[1,1]
)

axes[1,1].set_title(
    "Correlation Heatmap"
)

plt.suptitle(
    "Iris EDA Dashboard",
    fontsize=16
)

plt.tight_layout()

plt.savefig(
    "dashboard.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()