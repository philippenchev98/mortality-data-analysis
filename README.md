# mortality-data-analysis
Python project calculating Net Single Premium for Term Life Insurance using demographic mortality tables from HMD

# Actuarial Life Insurance Pricing Model
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philippenchev98/mortality-data-analysis/blob/main/Actuarial_Model.ipynb)

📊 **View the business presentation [here](Actuarial_Presentation.pdf)**

## Project Overview
This project calculates the **Net Single Premium (NSP)** for a Term Life Insurance policy. It demonstrates the application of actuarial science, demographic data analysis, and the time value of money (discounting) to determine the exact mathematical cost of life insurance risk.

## Key Findings

**Example calculation:** 10-year Term Life policy, 30-year-old male,
€100,000 sum assured, technical interest rate i = 3%, HMD 2021 mortality tables:

- **Net Single Premium (NSP): €1,826.19** — the pure mathematical cost of the
  mortality risk, i.e. ≈ **1.83% of the sum assured** for the full 10-year coverage.
- The discounted risk contribution is **not flat across the term**: it rises from
  €134 at age 30 to €274 at age 39 — the final year carries ~2x the risk cost of
  the first, reflecting the exponential growth of q_x with age.
- Discounting materially shapes the premium: a death benefit paid in year 10 is
  worth only ~74 cents on the euro today (v¹⁰ ≈ 0.744 at i = 3%).

**Data caveat:** the 2021 tables still reflect elevated COVID-19 mortality —
premiums computed on them are conservative relative to pre-pandemic (2019) tables.

## Data Source
The model uses 1x1 mortality tables (single-year age intervals and single calendar year data) for 2021.
* **$l_x$**: Number of survivors at exact age x.
* **$d_x$**: Number of deaths between age x and x+1.

## Mathematical Standard: Principle of Equivalence
In actuarial science, the pricing is based on the **Principle of Equivalence**: the expected present value of the benefits paid by the insurer must equal the expected present value of the premiums paid by the insured.

To calculate the cost for an n-year Term Life policy for a person aged x, we discount the expected payout for each year t using the technical interest rate i:

$$
NSP = \sum_{t=0}^{n-1} S \times \left( \frac{d_{x+t}}{l_x} \right) \times v^{t+1}
$$

Where:
* **S** = Sum Assured (e.g., €100,000)
* **v** = Discount factor 1 / (1 + i)

## Visualizations

### 1. Life Expectancy ($e_x$)
As expected, female life expectancy is structurally higher than male life expectancy across all ages.
![Life Expectancy](myplot4.png)

### 2. Mortality Rate ($q_x$) - Log Scale
The logarithmic scale reveals the "accident hump" for males in their early 20s and the exponential growth of mortality risk after age 40 (Gompertz-Makeham law).
![Mortality Rate](myplot3.png)

## Tech Stack


* **Python** (Core logic and mathematical modeling)
* **pandas** (Data extraction and wrangling)
