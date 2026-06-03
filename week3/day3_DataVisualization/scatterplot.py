import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

fig, ax = plt.subplots(figsize=(8, 6))

species = {
    'setosa': 'red',
    'versicolor': 'green',
    'virginica': 'blue'
}

for sp,color in species.items():
    subset = df[df['species'] == sp]
    ax.scatter(
        subset['sepal_length'],
        subset['sepal_width'],
        color=color,
        label=sp,
        alpha=0.7,
        edgecolor='black'
    )

ax.set_title('Scatter Plot Example: Iris Dataset')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Sepal Width (cm)')
ax.legend(title='Species')
ax.grid(True)
plt.tight_layout()
plt.savefig(
    "scatter_plot.png",
    dpi=150,
    bbox_inches="tight"
)
plt.show()