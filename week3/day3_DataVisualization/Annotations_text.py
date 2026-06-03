import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,30,20,40]

fig, ax = plt.subplots()

ax.plot(
    x,
    y,
    marker='o'
)

ax.text(
    5,
    40,
    "Highest Point"
)

ax.set_title(
    "Simple Annotation"
)

ax.set_xlabel("Month")
ax.set_ylabel("Sales")

plt.savefig(
    "text_annotation.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()