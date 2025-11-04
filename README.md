# AIPI510 Project 2: Toaster vs. Regular Oven: Cookie Science 🍪

This repo contains a small-scale, reproducible experiment comparing cookies baked in a **toaster oven** vs. a **regular
oven**.  
We analyze two objective metrics:

- **Weight Loss % (primary DV)** — proxy for moisture loss → relates to “crunchiness”
- **Spread Ratio (secondary DV)** — `diameter_avg / thickness`

We designed a **paired** experiment (one toaster + one regular per pair), controlled temperature/time/weight, and used *
*pilot-based power analysis** to plan the sample size.

---

## Research Summary

**Research question.** Do cookies from a regular oven differ from those baked in a toaster oven in objective, measurable
ways?

**Hypotheses.**

- **H₀:** No difference between ovens in weight loss % or spread ratio.
- **H₁:** There is a difference in at least one metric.

**Design highlights.**

- **IV:** Oven type (`toaster` vs `oven`)
- **DVs:** `weight_loss_pct` (primary), `spread_ratio` (secondary)
- **Controls:** same dough batch, ~30g per cookie, 375°F, 8 min bake, 3 min cool, same rack; no mid-bake rotation
- **Randomization:** dough pieces randomly assigned across two trays; bake order alternated between ovens
- **Paired analysis:** each `pair_id` contains two rows (toaster/oven)

**Power analysis (software & assumptions).**

- Initial: assumed **Cohen’s d = 0.5**, paired t-test, α=0.05, power=0.80 → ~**34 pairs** (≈68 cookies)
- Pilot: collected **7 pairs**, observed **dₙ ≈ 0.97 (weight loss %)**, **dₙ ≈ 0.87 (spread)** → required **13–15 pairs
  ** (26–30 cookies)
- Final: baked **28 pairs** (56 cookies total), exceeding power needs
- Software: **Python `statsmodels.stats.power.TTestPower`**

---

## Repo Structure

```
AIPI510_Project2/
├── data/
│   ├── raw/
│   │   ├── cookie_pairs_raw.csv       # raw paired data (toaster/oven)
│   │   └── cookie_pairs_pilot.csv     # 7-pair pilot used for power estimation
│   └── cleaned/
│       └── cookie_pairs_cleaned.csv   # produced by 01_clean.py
├── notebooks/
│   ├── 00_powerAnalysis.ipynb         # d=0.5 baseline power analysis (readable narrative)
│   └── 01_powerAnalysisPilot.ipynb    # pilot-based power analysis
├── Scripts/
│   ├── 00_power_analysis.py           # CLI version for power analysis (baseline + pilot)
│   ├── 01_clean.py                    # reads raw → validates/standardizes → writes cleaned
│   ├── 02_analyze.py                  # paired t-tests + Cohen’s d_z (two DVs)
│   └── 03_visualize.py                # boxplots for both metrics
├── requirements.txt
├── .gitignore
└── README.md
```

> Per assignment: **analysis code is provided as scripts** under `Scripts/`.  
> Notebooks are for explanation and are not required to reproduce results.

---

## Environment Setup

```bash
# Clone
git clone https://github.com/sam-packer/AIPI510_Project2.git
cd AIPI510_Project2

# Create environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate

# Install deps
pip install -r requirements.txt
```

## AI Citation

For our project, ChatGPT was used to generate the README with human modification afterward. ChatGPT was used on November
3, 2025, to assist with the generation of the README file.

ChatGPT was also used to help with the analysis on November 2, 2025. We used it to help choose the best statistical
evaluation methods for our data. ChatGPT gave us the syntax for our analysis, however the code was written out manually
to deepen our understanding of how to use the `statsmodels` package.

ChatGPT was also used on November 2, 2025, for minimal consultation on the best way to plot the graphical data, and to
give an understanding of how to read a box plot. ChatGPT helped revise the boxplot code as the initial, human written
version, had errors.

Claude 4.1 Opus was used on November 3, 2025, to help strengthen the analysis by explaining confidence intervals and
assisting writing the code to calculate them. Claude 4.1 Opus was used as well to explain the requirement for a normal
distribution with a paired t-test and showed how to plot a Q-Q plot to prove a normal distribution in our data.