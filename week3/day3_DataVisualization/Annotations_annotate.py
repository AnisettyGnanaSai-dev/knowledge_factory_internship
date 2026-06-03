import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]

sales = [
    100,
    110,
    115,
    120,
    250
]

fig, ax = plt.subplots(
    figsize=(8,5)
)

ax.plot(
    months,
    sales,
    marker='o',
    label='Sales'
)

ax.annotate(
    "Marketing Campaign Launch",
    xy=("May",250),
    xytext=("Mar",220),
    arrowprops=dict(
        arrowstyle="->"
    )
)

ax.legend()

ax.set_title(
    "Sales Trend"
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "arrow_annotation.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()