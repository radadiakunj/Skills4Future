"""
Date: 09-07-2026
Topic: Greenskilling / Sustainability data analysis

Dataset: Our World in Data (OWID) CO2 & Greenhouse Gas Emissions
File: data/owid-co2-data.csv
Source: https://github.com/owid/co2-data

Why this dataset?
- Directly related to sustainability, climate action, and green transition.
- Useful for greenskilling context: countries with high fossil CO2 often need
  more green jobs, renewable energy skills, and low-carbon workforce training.
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------------
# 1) IMPORT DATASET
# ---------------------------------------------------------------------------
df = pd.read_csv("data/owid-co2-data.csv")

print("=" * 70)
print("GREEN / SUSTAINABILITY DATASET ANALYSIS - 10-07-2026")
print("=" * 70)
print("\n1) Dataset loaded successfully")
print("Shape (rows, columns):", df.shape)
print("Column names:")
print(df.columns.tolist())

# ---------------------------------------------------------------------------
# 2) GENERALISATIONS ABOUT THE DATASET
# ---------------------------------------------------------------------------
"""
GENERALISATIONS (overall understanding of the dataset):

1. This is a country-year panel dataset: each row = one country in one year.
2. Time coverage is very long (from ~1750 to recent years). Early years have
   many missing values because modern emission tracking did not exist then.
3. Columns cover:
   - Identity: country, year, iso_code
   - Scale: population, gdp
   - Emissions: co2, coal_co2, oil_co2, gas_co2, cement_co2, flaring_co2
   - Intensity: co2_per_capita, co2_per_gdp, co2_per_unit_energy
   - Energy: primary_energy_consumption, energy_per_capita, energy_per_gdp
   - Climate impact: temperature_change_from_co2 / ghg
   - Shares: share of global emissions
4. Many nulls are EXPECTED, not data-entry mistakes:
   - Old years lack GDP / energy / consumption data
   - Some countries never had flaring / other industry emissions recorded
   - Aggregates like "World", "Asia" may not have iso_code
5. For greenskilling / sustainability analysis, recent years matter most
   (e.g. 2000 onwards), because green jobs and climate policy are modern topics.
"""

print("\n2) Basic overview")
print("Year range:", df["year"].min(), "to", df["year"].max())
print("Number of countries/entities:", df["country"].nunique())
print("\nFirst 5 rows:")
print(df.head())
print("\nInfo:")
df.info()
print("\nDescribe (numeric summary):")
print(df.describe())

# ---------------------------------------------------------------------------
# 3) FEATURE / COLUMN RELATIONSHIPS
# ---------------------------------------------------------------------------
"""
RELATIONS BETWEEN FEATURES / COLUMNS:

A) Identity columns
- country  <-> iso_code : same place identity (name vs code). Aggregates may
  have country name but missing iso_code.
- country, year : together uniquely identify most rows (panel key).

B) Scale / economy / people
- population <-> co2 : larger population often means higher total CO2,
  but not always (depends on development and energy mix).
- gdp <-> co2 : richer economies historically emit more total CO2
  (industrial activity), but efficiency can break this link.
- gdp <-> co2_per_gdp : higher GDP with cleaner tech can lower CO2 per GDP.
- population <-> co2_per_capita : total CO2 / population = intensity per person.

C) Emission source breakdown (parts of total CO2)
- coal_co2 + oil_co2 + gas_co2 + cement_co2 + flaring_co2 (+ other)
  roughly relate to total co2.
- coal_co2 high => more fossil-heavy energy mix => stronger need for
  greenskilling (renewables, energy efficiency, just transition).
- oil_co2 / gas_co2 relate to transport and power sector fuel use.

D) Intensity indicators (quality of emissions, not just quantity)
- co2_per_capita : lifestyle / development intensity.
- co2_per_gdp : carbon intensity of the economy (important for green growth).
- co2_per_unit_energy : how dirty the energy system is.
- energy_per_capita <-> co2_per_capita : more energy use often means more
  emissions unless energy is clean/renewable.

E) Growth and cumulative impact
- co2_growth_abs / co2_growth_prct : year-to-year change (policy progress?).
- cumulative_co2 : historical responsibility for climate change.
- temperature_change_from_co2 / ghg : climate outcome linked to emissions.

F) Trade / consumption view
- consumption_co2 vs co2 (production): shows whether a country "imports"
  emissions through goods. Important for fair sustainability accounting.

G) Land use
- land_use_change_co2 / co2_including_luc : deforestation and land use also
  matter for sustainability, not only fossil fuels.

Greenskilling takeaway from relations:
- High co2 + high coal_co2 + high co2_per_gdp => priority regions for green
  skills training (renewables, grid, efficiency, green manufacturing).
- Falling co2_per_gdp with rising gdp => possible green growth signal.
"""

# Focus on a practical sustainability subset for clearer analysis
focus_cols = [
    "country",
    "year",
    "iso_code",
    "population",
    "gdp",
    "co2",
    "co2_per_capita",
    "co2_per_gdp",
    "coal_co2",
    "oil_co2",
    "gas_co2",
    "cement_co2",
    "primary_energy_consumption",
    "energy_per_capita",
    "share_global_co2",
    "temperature_change_from_co2",
]

# Keep recent years (more relevant to greenskilling / current sustainability)
df_focus = df.loc[df["year"] >= 2000, focus_cols].copy()

print("\n3) Focused sustainability subset (year >= 2000)")
print("Focused shape:", df_focus.shape)
print("Null % in focused columns:")
print((df_focus.isnull().mean() * 100).round(2).sort_values(ascending=False))

# Correlation among numeric sustainability features
numeric_cols = df_focus.select_dtypes(include=[np.number]).columns.tolist()
corr = df_focus[numeric_cols].corr()
print("\nCorrelation matrix (feature relationships, numeric):")
print(corr.round(2))

print("\nStrongest correlations with total CO2 (absolute value):")
if "co2" in corr.columns:
    print(corr["co2"].drop("co2").abs().sort_values(ascending=False).head(10).round(3))

# ---------------------------------------------------------------------------
# 4) HANDLE NULL VALUES (based on dataset understanding)
# ---------------------------------------------------------------------------
"""
NULL HANDLING STRATEGY (reasoned for THIS dataset):

1) iso_code
   - Missing mostly for regions/aggregates (World, continents, income groups).
   - Action: fill with 'UNKNOWN_OR_AGGREGATE' so rows stay usable for grouping.

2) Emission source columns (coal_co2, oil_co2, gas_co2, cement_co2)
   - Missing often means "not reported / not applicable for that year-country",
     especially historically. In recent years, for country-level analysis,
     treating truly absent reported sources as 0 can be reasonable when the
     country has a total co2 value (source not separately broken out).
   - Action: if co2 is present and source is null => fill source with 0.
     If co2 itself is null => leave source null (row is incomplete).

3) population, gdp, energy, intensity metrics
   - These are NOT safely fillable with 0 (0 GDP/population is unrealistic).
   - Action: keep nulls, then for modeling/summary use rows where key fields
     exist; optionally forward-fill within each country by year for short gaps.

4) Drop rows where core sustainability target 'co2' is missing
   - Without CO2, climate/sustainability analysis for that row is weak.

5) Do NOT blindly fill all nulls with mean/median across whole dataset
   - That would mix rich/poor countries and old/new years and distort truth.
"""

print("\n4) Null handling")
before_nulls = df_focus.isnull().sum().sum()
print("Total null cells before cleaning:", before_nulls)

# 4a) iso_code: categorical placeholder for aggregates / unknown
df_focus["iso_code"] = df_focus["iso_code"].fillna("UNKNOWN_OR_AGGREGATE")

# 4b) emission sources: fill with 0 only when total co2 exists
source_cols = ["coal_co2", "oil_co2", "gas_co2", "cement_co2"]
for col in source_cols:
    mask = df_focus["co2"].notna() & df_focus[col].isna()
    df_focus.loc[mask, col] = 0

# 4c) within each country, forward-fill then back-fill short gaps for
#     population/gdp/energy (time-series continuity), without inventing zeros
ts_cols = [
    "population",
    "gdp",
    "primary_energy_consumption",
    "energy_per_capita",
    "co2_per_capita",
    "co2_per_gdp",
    "share_global_co2",
    "temperature_change_from_co2",
]
df_focus = df_focus.sort_values(["country", "year"])
df_focus[ts_cols] = df_focus.groupby("country", group_keys=False)[ts_cols].apply(
    lambda g: g.ffill().bfill()
)

# 4d) drop rows still missing the core emission indicator
df_clean = df_focus.dropna(subset=["co2"]).copy()

after_nulls = df_clean.isnull().sum().sum()
print("Rows after dropping missing co2:", len(df_clean))
print("Total null cells after cleaning:", after_nulls)
print("Remaining nulls by column:")
print(df_clean.isnull().sum().sort_values(ascending=False))

# ---------------------------------------------------------------------------
# 5) SIMPLE SUSTAINABILITY / GREEN ANALYSIS OUTPUTS
# ---------------------------------------------------------------------------
print("\n5) Quick sustainability insights (cleaned data)")

# Top emitters in latest available year
latest_year = int(df_clean["year"].max())
latest = df_clean[df_clean["year"] == latest_year].copy()

# Prefer actual countries (have real iso codes) for ranking
latest_countries = latest[latest["iso_code"] != "UNKNOWN_OR_AGGREGATE"]

print(f"\nTop 10 CO2 emitters in {latest_year} (countries only):")
print(
    latest_countries.nlargest(10, "co2")[
        ["country", "co2", "co2_per_capita", "coal_co2", "share_global_co2"]
    ]
)

print(f"\nTop 10 by CO2 per capita in {latest_year}:")
print(
    latest_countries.nlargest(10, "co2_per_capita")[
        ["country", "co2_per_capita", "co2", "energy_per_capita"]
    ]
)

# Coal share proxy: coal_co2 / co2 (greenskilling pressure indicator)
latest_countries = latest_countries.copy()
latest_countries["coal_share"] = np.where(
    latest_countries["co2"] > 0,
    latest_countries["coal_co2"] / latest_countries["co2"],
    np.nan,
)
print(f"\nTop 10 coal-heavy emitters (coal_co2 / co2) in {latest_year}:")
print(
    latest_countries.nlargest(10, "coal_share")[
        ["country", "coal_share", "coal_co2", "co2"]
    ]
)

# Save cleaned subset for reuse
output_path = "data/owid_co2_cleaned_2000plus_10-07-2026.csv"
df_clean.to_csv(output_path, index=False)
print("\nCleaned dataset saved to:", output_path)

# ---------------------------------------------------------------------------
# 6) SUMMARY OF WHAT WAS DONE
# ---------------------------------------------------------------------------
"""
======================== SUMMARY (END OF FILE) ========================

What I did on 10-07-2026:

1. Downloaded a sustainability-related dataset:
   - Our World in Data CO2 emissions dataset (owid-co2-data.csv)
   - Saved in: data/owid-co2-data.csv

2. Imported the dataset into this Python file using pandas.

3. Wrote generalisations about the dataset:
   - Country-year panel from 1750 to recent years
   - Mix of identity, emissions, energy, GDP, population, climate columns
   - Many nulls are structural (old years / unreported indicators)

4. Documented relationships between features:
   - population/gdp linked to total emissions scale
   - coal/oil/gas/cement as parts of total CO2
   - per-capita and per-GDP metrics as intensity / efficiency signals
   - energy use linked to emissions unless energy is clean
   - greenskilling relevance: high fossil/coal intensity => stronger need
     for green skills and just transition

5. Handled null values with dataset-aware logic:
   - iso_code missing => 'UNKNOWN_OR_AGGREGATE'
   - emission source nulls filled with 0 only when total co2 exists
   - population/gdp/energy gaps filled within country by time (ffill/bfill)
   - rows without co2 dropped
   - avoided blind global mean filling (would distort country differences)

6. Produced simple analysis:
   - correlation between numeric features
   - top emitters, top per-capita emitters, coal-heavy countries
   - saved cleaned recent-year subset CSV

7. Uploaded/saved this Python file with today's date in the name:
   - 10-07-2026_Green_Sustainability_Analysis.py

=======================================================================
"""

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(
    """
1) Downloaded OWID CO2 sustainability dataset into data/owid-co2-data.csv
2) Imported it with pandas and explored shape, columns, describe, nulls
3) Documented generalisations + feature relationships in comments
4) Handled nulls using dataset understanding (not blind fill)
5) Analysed recent years for sustainability / greenskilling signals
6) Saved cleaned CSV and named this script with today's date (10-07-2026)
"""
)
print("Done.")
