import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

fig, ax = plt.subplots(figsize=(8, 5))

ax.hist(
    df["petal_length"],
    bins=10,
    edgecolor='black',
    color='skyblue',
    alpha=0.7,
    label='Petal Length'
)

ax.set_title('Histogram Example: Iris Dataset')
ax.set_xlabel(
    "Petal Length"
)

ax.set_ylabel(
    "Frequency"
)

ax.legend()

plt.tight_layout()

plt.savefig(
    "histogram.png",
    dpi=150,
    bbox_inches='tight'
)

plt.show()