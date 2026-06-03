import seaborn as sns
import matplotlib.pyplot as plt

anscombe = sns.load_dataset("anscombe")

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 8)
)

axes = axes.flatten()

datasets = anscombe["dataset"].unique()

for ax, dataset in zip(axes, datasets):

    subset = anscombe[
        anscombe["dataset"] == dataset
    ]

    ax.scatter(
        subset["x"],
        subset["y"],
        s=60
    )

    ax.set_title(
        f"Dataset {dataset.upper()}"
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    ax.grid(True)

plt.suptitle(
    "Anscombe's Quartet: Same Statistics, Different Stories",
    fontsize=14
)

plt.tight_layout()

plt.savefig(
    "anscombe_quartet.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()