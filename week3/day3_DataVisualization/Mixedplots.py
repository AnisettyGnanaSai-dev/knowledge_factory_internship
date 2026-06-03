import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15,5)
)

axes[0].hist(
    df["petal_length"],
    bins=20
)

axes[0].set_title("Histogram")

sns.boxplot(
    y=df["petal_length"],
    ax=axes[1]
)

axes[1].set_title("Boxplot")

sns.violinplot(
    y=df["petal_length"],
    ax=axes[2]
)

axes[2].set_title("Violin Plot")

plt.tight_layout()

plt.savefig(
    "distribution_comparison.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()