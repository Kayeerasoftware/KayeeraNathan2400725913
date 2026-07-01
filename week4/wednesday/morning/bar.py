import matplotlib.pyplot as plt

# w = ['John', 'Peter', 'Ruth', 'Simon']
# z = [20,30,40,50]

# plt.bar(w,z)
# plt.title("simple Bar Graph")
# plt.xlabel("Names of students")
# plt.ylabel("Age of students")
# plt.show()



marks = [40, 60, 75, 90, 50, 78, 83, 77, 92, 87, 43, 67, 37]

# plt.hist(marks, bins=5)

# plt.title("Histogram of BSSE Student Marks")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")





fig, ax = plt.subplots(figsize=(10, 6))

ax.hist( marks, bins=6, edgecolor="black", linewidth=1.2, alpha=0.8)

average = sum(marks) / len(marks)
ax.axvline(average, color="red", linestyle="--", linewidth=2, label=f"Average = {average:.1f}")

ax.set_title("Distribution of BSSE Student Marks", fontsize=16, fontweight="bold")
ax.set_xlabel("Marks", fontsize=12)
ax.set_ylabel("Number of Students", fontsize=12)
ax.grid(axis="y", linestyle="--", alpha=0.6)

ax.legend()
plt.tight_layout()
plt.show()