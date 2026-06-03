import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

corr = df.drop(
    columns="species"
).corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="viridis",
    fmt=".2f"
)

plt.title(
    "Iris Correlation Heatmap"
)

plt.savefig(
    "heatmap2.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()