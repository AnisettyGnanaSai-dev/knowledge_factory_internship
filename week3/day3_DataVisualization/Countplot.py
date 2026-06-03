import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x="species"
)

plt.title(
    "Count of Iris Species"
)

plt.savefig(
    "countplot.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()