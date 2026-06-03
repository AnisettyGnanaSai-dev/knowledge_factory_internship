import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.arange(1, 11)
y = x ** 2

fig, ax = plt.subplots(figsize=(8, 6)
)

ax.plot(
    x,
    y,
    marker='o',
    linewidth=2,
    label = 'y = x^2'
)

ax.set_title('Line Plot Example')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True)
plt.tight_layout()
plt.savefig(
    "line_plot.png",
    dpi=150,
    bbox_inches="tight"
)
plt.show()