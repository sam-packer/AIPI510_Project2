import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import ttest_rel

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

# Q-Q plots for weight loss % and spread ratio
sr_pairs = df.pivot(index="pair_id", columns="randomization_order", values="spread_ratio")
wlp_pairs = df.pivot(index="pair_id", columns="randomization_order", values="weight_loss_pct")
result = ttest_rel(sr_pairs["toaster"], sr_pairs["oven"])

sr_diffs = sr_pairs["toaster"] - sr_pairs["oven"]
wlp_diffs = wlp_pairs["toaster"] - wlp_pairs["oven"]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

stats.probplot(sr_diffs, dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot: Spread Ratio Differences")

stats.probplot(wlp_diffs, dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot: Weight Loss % Differences")

plt.tight_layout()
plt.show()