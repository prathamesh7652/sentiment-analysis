import streamlit as st
from textblob import TextBlob

# Page config
st.set_page_config(page_title="Sentiment Analyzer", page_icon="💬", layout="centered")

# Title
st.title("💬 Sentiment Analysis App")
st.write("Enter any text and see its sentiment!")

# Input
user_input = st.text_area("Enter your text here:")

# Analyze button
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Determine sentiment
        if polarity > 0:
            sentiment = "Positive 😊"
            color = "green"
        elif polarity < 0:
            sentiment = "Negative 😡"
            color = "red"
        else:
            sentiment = "Neutral 😐"
            color = "gray"

        # Output
        st.markdown(f"### Sentiment: :{color}[{sentiment}]")
        st.write(f"Polarity Score: {polarity:.2f}")