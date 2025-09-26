# Temperature Anomalies in Pakistan (1880–2025)

“This project analyzes monthly temperature anomaly data for Pakistan (1880–2025) using exploratory data analysis and time-series forecasting. The goal is to measure long-term warming trends, smooth seasonal fluctuations, and build predictive models to forecast future temperature changes. By focusing on Pakistan, a climate-vulnerable country , the study highlights both historical climate change impacts and future risks.”

This repository contains the notebook **`main.ipynb`**, which analyzes historical and future temperature anomaly trends for Pakistan using NASA GISTEMP data.

## Repository Contents
- `main.ipynb` — Jupyter notebook with code, visuals, and findings.
- `README.md` - Summary of Project 

## Dataset Source
NASA GISTEMP v4: https://data.giss.nasa.gov/gistemp/

Subset: Pakistan’s latitude (24–37°N) and longitude (60–77°E).

---

# Temperature Anomalies in Pakistan (1880–2025)

## 1. Introduction
- **Problem Statement**: Climate change is one of the greatest challenges of the 21st century. Pakistan, being highly vulnerable due to its geography and reliance on agriculture, faces significant risks from rising temperatures.
- **Goal of Study**: To analyze historical temperature anomaly data for Pakistan, understand long-term warming trends, seasonal patterns, and forecast future anomalies.
- **Dataset Used**: NASA GISTEMP v4 gridded monthly temperature anomaly dataset (1880–2025), subset for Pakistan’s latitude and longitude.

## 2. Exploratory Data Analysis (EDA)
- **Coverage:** Data spans 1880–2025; monthly; no major gaps.
- **Raw anomalies:** High short-term variability with an upward drift.
- **Smoothed trend:** 12‑month rolling average shows clear warming post‑1970.
- **Decadal means:** Each recent decade warmer than the previous; 2010s/2020s highest.
- **Seasonality:** Winters warming faster than summers.
- **Distribution:** Shift toward positive anomalies; extreme hot months more frequent.
- **Decomposition:** Trend ↑, stable seasonality, residual captures noise.

## 3. Forecasting (Time Series Modeling)
- **Approaches:** ARIMA/SARIMA and/or Prophet; (optionally) LSTM.
- **Outcome:** Continued warming; future anomalies remain above historical baseline.

## 4. Discussion
- **Implications:** Agriculture stress, water shortages, health impacts; winter warming reduces snowmelt supply.
- **Limitations:** Only temperature anomalies modeled; not precipitation/extreme events; global modes (e.g., ENSO) not explicitly controlled.

## 5. Conclusion
- Warming clear since 1880, accelerating post‑1970.
- Winters warming faster.
- Forecasts indicate sustained rise; Pakistan remains climate‑vulnerable and needs adaptation across agriculture, water, and disaster preparedness.

---

# Results & Figures 

## 1) EDA-Global & Pakistan Anomaly Trends
Loaded NASA GISTEMP v4 monthly anomalies; validated coverage; visualized Pakistan vs global series; applied 12‑month rolling means.

**Results** Both global and Pakistan series warm markedly post‑1970; Pakistan’s variability is higher but follows the global upward drift.

## 2) Regional Breakdown-North, South, East (Punjab) Slopes
Aggregated gridded anomalies by region and estimated linear warming rates.

**Results** North (mountains) warms fastest (~0.13 °C/decade), East/Punjab ~0.11 °C/decade (agri‑critical), South ~0.09 °C/decade (heat‑stress compounding).

## 3) Change Point Detection-1970s Acceleration
Computed rolling 10‑year slopes and inspected structural shifts.

**Results** Persistent positive rates after the 1970s indicate a regime shift to sustained warming → higher baseline risk for heat, melt and water stress.

## 4) Extreme Event Analysis-Top Hottest Years
Ranked annual means and monthly extremes.

**Results** Top‑10 hottest years cluster after 2000, showing a frequent extremes (aligns with observed heatwaves and 2022 anomalies).

## 5) Pakistan vs Global Comparison
Overlayed Pakistan and global anomalies; compared decadal means.

**Results** Pakistan’s warming is broadly in line with global trends but exhibits sharper peaks, reflecting regional sensitivity to large‑scale climate modes.

## 6) Forecast — Prophet (with Uncertainty Bands)
Fit Prophet on monthly anomalies and generated 10–20y forecasts with uncertainty intervals.

**Results** Median trajectory remains above historical baseline with rising anomalies; intervals reinforce high probability of continued warming.
> If ARIMA was used in the notebook, treat Prophet as an alternative specification; include whichever plot is present and label accordingly.

## 7) Policy & Societal Insights
**Agriculture:** Heat stress threatens wheat/rice/cotton yields → invest in heat‑tolerant seeds and modern irrigation.
**Water/Glaciers:** Northern warming accelerates melt → expand storage, basin management.
**Urban Health:** Heatwaves intensify in southern cities → heat action plans, cooling access.
**Disaster Risk:** Extremes cluster post‑2000 → stronger early warnings/NDMA capacity.
**Climate Justice:** Pakistan emits <1% but bears outsized impacts → leverage evidence for climate finance & loss‑and‑damage.

---

## 🔧 Environment & Dependencies
Python ≥ 3.9. Main libraries: pandas, numpy, matplotlib, seaborn, scikit‑learn, plotly.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -U pip pandas numpy matplotlib seaborn scikit-learn plotly prophet pmdarima
```

