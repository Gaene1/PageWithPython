import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set_theme()  # set default seaborn theme

# Scatterplot with grouping
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
group = np.random.choice(['A', 'B', 'C'], 100)

sns.scatterplot(x=x, y=y, hue=group, palette='viridis')
plt.title('Seaborn Scatter Plot')
plt.show()
plt.savefig("figures/sns_basics.png")
plt.close()

# Violinplot
data = np.random.normal(0, 1, 100)
groups = np.random.choice(['A', 'B'], 100)

sns.violinplot(x=data, y=groups)
plt.title("Seaborn Violinplot")
plt.savefig("figures/sns_violinplot.png")
plt.close()

# Color palettes
x = np.random.normal(0, 1, 200)
y = np.random.normal(0, 1, 200)
groups = np.random.choice(['A', 'B', 'C', 'D'], 200)

sns.scatterplot(x=x, y=y, hue=groups, palette='rocket')
plt.savefig("figures/sns_color_palette.png")
plt.close()
