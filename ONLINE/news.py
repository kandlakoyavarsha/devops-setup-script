import streamlit as st
import requests

st.title("📰 Live News Tracker")

API_KEY = "c44f77860f984fb2a828f682e645325c"

country = st.selectbox("Choose a country", ["in", "us", "gb", "au", "ca"])
category = st.selectbox("Choose a category", ["general", "technology", "business", "health", "science", "sports"])


url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

st.write("API response:", data)

if data.get("status") == "ok" and "articles" in data:
    for article in data["articles"][:5]:
        st.subheader(article["title"])
        st.write(article.get("description", "No description"))
        st.markdown(f"[Read more]({article['url']})")
else:
    st.error("Something went wrong: " + data.get("message", "Unknown error"))
