import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

rolls = np.random.randint(1, 7, size=1000)

print("First 10 rolls:", rolls[:10])

faces, counts = np.unique(rolls, return_counts=True)

print("\nFace\tCount\tEmpirical P\tTheoretical P")

for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    theoretical_probability = 1 / 6

    print(
        face,
        "\t",
        count,
        "\t",
        round(empirical_probability, 4),
        "\t\t",
        round(theoretical_probability, 4)
    )

plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), edgecolor="black")

plt.title("Die Roll Distribution")
plt.xlabel("Die Face")
plt.ylabel("Frequency")

plt.xticks(range(1, 7))

plt.savefig("die_rolls.png")
plt.show()

print("\nSaved die_rolls.png")