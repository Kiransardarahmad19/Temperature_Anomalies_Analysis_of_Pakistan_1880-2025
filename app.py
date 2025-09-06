import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt

# Load dataset
ds = xr.open_dataset("dataset.nc")

st.title("🌍 Climate Change Dashboard: Pakistan, India & Global")

# Country selection
region = st.selectbox("Select Region", ["Pakistan", "India", "Global"])

if region == "Pakistan":
    data = ds['tempanomaly'].sel(lat=slice(24,37), lon=slice(60,77)).mean(dim=["lat","lon"])
elif region == "India":
    data = ds['tempanomaly'].sel(lat=slice(8,37), lon=slice(68,97)).mean(dim=["lat","lon"])
else:
    data = ds['tempanomaly'].mean(dim=["lat","lon"])

# Plot
fig, ax = plt.subplots(figsize=(10,5))
data.groupby('time.year').mean().plot(ax=ax)
ax.set_title(f"{region} Temperature Anomaly (1880–2025)")
st.pyplot(fig)
