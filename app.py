import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Title
st.title("📰 AI Fake News Detection System")

st.write("Enter a news article below to check if it's Fake or Real.")

# Input
input_text = st.text_area("News Text")

# Button
if st.button("Analyze"):
    if input_text.strip() != "":
        # Convert text to vector
        vectorized = vectorizer.transform([input_text])
        
        # Predict
        prediction = model.predict(vectorized)

        # Output
        if prediction[0] == "FAKE":
            st.error("🚨 This news is FAKE")
        else:
            st.success("✅ This news is REAL")
    else:
        st.warning("Please enter some text")