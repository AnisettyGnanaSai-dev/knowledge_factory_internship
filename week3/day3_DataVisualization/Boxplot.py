import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

fig, ax = plt.subplots(
    figsize=(8,5)
)

sns.boxplot(
    data=df,
    x="species",
    y="petal_length",
    ax=ax
)

ax.set_title(
    "Petal Length by Species"
)

ax.set_xlabel(
    "Species"
)

ax.set_ylabel(
    "Petal Length"
)

plt.tight_layout()

plt.savefig(
    "species_boxplot1.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()