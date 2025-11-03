import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/cleaned/cookie_pairs_cleaned.csv")

# Boxplot for spread ratio
sns.boxplot(
    data=df,
    x="randomization_order",
    y="spread_ratio",
    hue="randomization_order",
    palette="pastel",
    legend=False
)
plt.title("Spread Ratio by Baking Method")
plt.xlabel("Baking Method")
plt.ylabel("Spread Ratio")
plt.show()

# Boxplot for weight loss %
sns.boxplot(
    data=df,
    x="randomization_order",
    y="weight_loss_pct",
    hue="randomization_order",
    palette="pastel",
    legend=False
)
plt.title("Weight Loss % by Baking Method")
plt.xlabel("Baking Method")
plt.ylabel("Weight Loss %")
plt.show()