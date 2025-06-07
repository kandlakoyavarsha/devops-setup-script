import streamlit as st
import requests
import pandas as pd

st.title("🦠 Live COVID-19 Tracker")
st.write("Get real-time COVID-19 stats by country")

# Input: Country Name
country = st.text_input("Enter a country (e.g., India, USA, Brazil)")

# Fetch data from API
def get_covid_data(country_name):
    url = f"https://disease.sh/v3/covid-19/countries/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Show data on button click
if st.button("Get Stats"):
    if country:
        data = get_covid_data(country.strip())
        if data:
            st.success(f"COVID-19 Stats for {data['country']}")
            st.write(f"🌍 Population: {data['population']:,}")
            st.write(f"🦠 Total Cases: {data['cases']:,}")
            st.write(f"✅ Recovered: {data['recovered']:,}")
            st.write(f"💀 Deaths: {data['deaths']:,}")
            st.write(f"📆 Updated: {pd.to_datetime(data['updated'], unit='ms')}")
        else:
            st.error("Invalid country or data not available.")
    else:
        st.warning("Please enter a country name.")
