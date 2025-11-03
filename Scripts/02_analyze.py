import pandas as pd
from scipy.stats import ttest_rel

df = pd.read_csv("../data/cleaned/cookie_pairs_cleaned.csv")
sr_pairs = df.pivot(index="pair_id", columns="randomization_order", values="spread_ratio")

result = ttest_rel(sr_pairs["toaster"], sr_pairs["oven"])
t_stat = result.statistic
p_val = result.pvalue
df_len = len(sr_pairs) - 1

print("Paired t-test for Spread Ratio (Toaster vs. Oven)")
print(f"t({df_len}) = {t_stat:.3f},  p = {p_val:.3f}")

wlp_pairs = df.pivot(index="pair_id", columns="randomization_order", values="weight_loss_pct")

result = ttest_rel(wlp_pairs["toaster"], wlp_pairs["oven"])
t_stat = result.statistic
p_val = result.pvalue
df_len = len(wlp_pairs) - 1

print("Paired t-test for Weight Loss % (Toaster vs. Oven)")
print(f"t({df_len}) = {t_stat:.3f},  p = {p_val:.3f}")

sr_diffs = sr_pairs["toaster"] - sr_pairs["oven"]
sr_dz = sr_diffs.mean() / sr_diffs.std(ddof=1)
print(f"Cohen's d_z for Spread Ratio: {sr_dz:.3f}")

# --- Weight loss % effect size ---
wlp_diffs = wlp_pairs["toaster"] - wlp_pairs["oven"]
wlp_dz = wlp_diffs.mean() / wlp_diffs.std(ddof=1)
print(f"Cohen's d_z for Weight Loss %: {wlp_dz:.3f}")