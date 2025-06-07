import streamlit as st

# Title
st.title("🧠 Mood Predictor")
st.write("Type something and let me guess your mood!")

# Text input
user_input = st.text_area("How are you feeling today?", "")

# Simple mood prediction (just using keywords)
def predict_mood(text):
    text = text.lower()
    if any(word in text for word in ["happy", "great", "joy", "awesome", "fun"]):
        return "😊 Happy"
    elif any(word in text for word in ["sad", "down", "unhappy", "cry"]):
        return "😢 Sad"
    elif any(word in text for word in ["angry", "mad", "furious", "rage"]):
        return "😠 Angry"
    elif any(word in text for word in ["ok", "fine", "normal", "neutral"]):
        return "😐 Neutral"
    else:
        return "🤔 Couldn’t guess! Try using emotional words."

# Predict button
if st.button("Predict Mood"):
    if user_input.strip():
        mood = predict_mood(user_input)
        st.subheader(f"Predicted Mood: {mood}")
    else:
        st.warning("Please enter some text first.")
