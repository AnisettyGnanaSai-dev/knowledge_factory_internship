import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = ['RohitSharma', 'ViratKohli', 'KL Rahul', 'ShikharDhawan', 'ShreyasIyer']
y = [100, 120, 80, 90, 110]

fig, ax = plt.subplots(figsize=(8, 6))

ax.set_title('Bar Chart Example')
ax.set_xlabel('Batsmen')
ax.set_ylabel('Runs Scored')
ax.legend(['Runs'], loc='upper left')
ax.bar(x, y, color='blue', alpha=0.7)
plt.tight_layout()
plt.savefig(
    "bar_chart.png",
    dpi=150,
    bbox_inches="tight"
)
plt.legend()
plt.show()

