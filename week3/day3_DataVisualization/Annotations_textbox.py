import numpy as np
import matplotlib.pyplot as plt

scores = [
    50,
    60,
    80,
    70,
    90
]

fig, ax = plt.subplots()

ax.plot(
    scores,
    marker='o'
)

ax.text(
    2,
    85,
    f"Mean = {np.mean(scores):.1f}",
    bbox=dict(
        boxstyle='round'
    )
)

ax.set_title(
    "Scores Analysis"
)

plt.savefig(
    "text_box.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()