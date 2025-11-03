# --- Method 1: Exact computation using statsmodels --------------------
import math

import numpy as np
import pandas as pd
from statsmodels.stats.power import TTestPower
from math import ceil

# Parameters
alpha = 0.05        # significance level (two-sided)
power = 0.80        # desired power (1 - β)
d = 0.5             # assumed medium effect size (Cohen's d)
tt = TTestPower()
PATH = "../data/raw/cookie_pairs_pilot.csv"
ALPHA = 0.05
TARGET_POWER = 0.80
BUFFER = 0.10  # 10% extra safety margin

# Compute required number of pairs (each pair = 2 cookies)
n_pairs_exact = tt.solve_power(effect_size=d, alpha=alpha, power=power, alternative='two-sided')
n_pairs_exact_ceiled = ceil(n_pairs_exact)

print("*" * 80)
print(f"Initial T-Test With No Pilot:")
print(f"Required pairs (raw):     {n_pairs_exact:.2f}")
print(f"Required pairs (rounded): {n_pairs_exact_ceiled}")
print(f"Total cookies (≈):        {n_pairs_exact_ceiled * 2}")
print("*" * 80)


print("T-Test with Pilot Data for Weight Loss %")
# 2) Read the pilot data
df = pd.read_csv(PATH, encoding="utf-8-sig")

# preview data
print(df.head())

# standardize column names
df.columns = [c.strip().lower() for c in df.columns]

# 3) Pivot into pairs (toaster vs regular)

# pivot so that each row = one pair
pairs_1 = df.pivot(index="pair_id", columns="randomization_order", values="weight_loss_pct")

print(pairs_1.head())

# 4) Compute paired differences (toaster − regular)
diffs = (pairs_1["t"].astype(float) - pairs_1["r"].astype(float)).values
n_pilot = len(diffs)
mean_diff = np.mean(diffs)
sd_diff = np.std(diffs, ddof=1)

print(f"[Pilot] n_pairs = {n_pilot}")
print(f"[Pilot] mean_diff = {mean_diff:.4f}  (toaster - regular)")
print(f"[Pilot] sd_diff   = {sd_diff:.4f}")

# 5) Compute effect size (Cohen’s d_z) and required sample size
dz = abs(mean_diff) / sd_diff
tt = TTestPower()
n_exact = tt.solve_power(effect_size=dz, alpha=ALPHA, power=TARGET_POWER, alternative="two-sided")
required_pairs = math.ceil(n_exact)
planning_pairs = math.ceil(required_pairs / (1 - BUFFER))

print(f"[Effect] Cohen's d_z = {dz:.3f}")
print(f"[Power] Required pairs @80% power = {required_pairs} (~{required_pairs*2} cookies)")
print(f"[Plan] With 10% buffer → {planning_pairs} pairs (~{planning_pairs*2} cookies)")

print("*" * 80)

print("T-Test with Pilot Data for Spread Ratio")
pairs_2 = df.pivot(index="pair_id", columns="randomization_order", values="spread_ratio")

print(pairs_2.head())

diffs = (pairs_2["t"].astype(float) - pairs_2["r"].astype(float)).values
n_pilot = len(diffs)
mean_diff = np.mean(diffs)
sd_diff = np.std(diffs, ddof=1)

print(f"[Pilot] n_pairs = {n_pilot}")
print(f"[Pilot] mean_diff = {mean_diff:.4f}  (toaster - regular)")
print(f"[Pilot] sd_diff   = {sd_diff:.4f}")

dz = abs(mean_diff) / sd_diff
tt = TTestPower()
n_exact = tt.solve_power(effect_size=dz, alpha=ALPHA, power=TARGET_POWER, alternative="two-sided")
required_pairs = math.ceil(n_exact)
planning_pairs = math.ceil(required_pairs / (1 - BUFFER))

print(f"[Effect] Cohen's d_z = {dz:.3f}")
print(f"[Power] Required pairs @80% power = {required_pairs} (~{required_pairs*2} cookies)")
print(f"[Plan] With 10% buffer → {planning_pairs} pairs (~{planning_pairs*2} cookies)")
print("*" * 80)