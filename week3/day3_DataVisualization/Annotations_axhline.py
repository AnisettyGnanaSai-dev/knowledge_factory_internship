import numpy as np
import matplotlib.pyplot as plt

sales = [100,120,150,110,170]

mean_sales = np.mean(
    sales
)

fig, ax = plt.subplots()

ax.plot(
    sales,
    marker='o'
)

ax.axhline(
    mean_sales,
    color='red',
    linestyle='--',
    label='Average'
)

ax.legend()

ax.set_title(
    "Sales vs Average"
)

plt.savefig(
    "mean_line.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()