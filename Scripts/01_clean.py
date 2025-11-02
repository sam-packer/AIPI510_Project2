import pandas as pd
import numpy as np

df = pd.read_csv("../data/raw/cookie_pairs_pilot.csv")

df.columns = [c.strip().lower() for c in df.columns]

# rename t and r to toaster/oven
df["randomization_order"] = (
    df["randomization_order"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({"t": "toaster", "r": "oven"})
)

# ensure there's no other labels
valid_labels = {"toaster", "oven"}
bad_labels = set(df["randomization_order"]) - valid_labels
if bad_labels:
    print("Unexpected labels found:", bad_labels)

# check for any non pairs
pair_counts = df["pair_id"].value_counts()
invalid_pairs = pair_counts[pair_counts != 2]
if not invalid_pairs.empty:
    print("Invalid pair counts detected:")
    print(invalid_pairs)


# ensure nothing is outrageously out of bounds (i.e. typo detection)
def flag_out_of_bounds(series, low=None, high=None):
    return (series < low) | (series > high)


bounds = {
    "preheat_f": (200, 600),
    "bake_time_min": (1, 60),
    "cool_down_min": (0, 180),
    "init_weight_g": (5, 100),
    "post_weight_g": (0, 100),
    "d1_cm": (0, 25),
    "d2_cm": (0, 25),
    "d_avg": (0, 25),
    "thickness_cm": (0, 5),
    "spread_ratio": (0.5, 30),
    "weight_loss_pct": (0, 1),
}

for col, (low, high) in bounds.items():
    mask = flag_out_of_bounds(df[col], low, high)
    if mask.any():
        n_bad = mask.sum()
        print(f"{n_bad} values of '{col}' outside [{low}, {high}]")
        print(df.loc[mask, ["pair_id", "randomization_order", col]])

# reorder the columns
desired_order = [
    "pair_id",
    "batch_id",
    "randomization_order",
    "preheat_f",
    "bake_time_min",
    "cool_down_min",
    "init_weight_g",
    "post_weight_g",
    "d1_cm",
    "d2_cm",
    "d_avg",
    "thickness_cm",
    "spread_ratio",
    "weight_loss_pct",
]

df = df[desired_order]

print(f"Clean summary: {len(df)} rows, "
      f"{df['pair_id'].nunique()} unique pairs, "
      f"{(df['randomization_order'] == 'toaster').sum()} toaster / "
      f"{(df['randomization_order'] == 'oven').sum()} oven rows.")

df.to_csv("../data/cleaned/cookie_pairs_cleaned.csv", index=False)
