import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("iris")

pair = sns.pairplot(
    df,
    hue = "species"
)

pair.fig.suptitle(
    "iris pair plot",
    y = 1.02
)

pair.savefig(
    "parplot.png"
)

plt.show()