import matplotlib.pyplot as plt
import seaborn as sns

x = [1,2,3,4,5]
y = [6,7,8,9,10]

sns.lineplot(x=x, y=y,legend=True,label="sales")
plt.title("Plot with seaborn")
sns.lineplot(x=x, y=y)

plt.show()

# types of plots in seaborn
# scatterplot()
# lineplot()
# barplot()
# histplot()
# countplot()
# boxplot()
# violinplot()
# heatmap()
# pairplot()
# jointplot()