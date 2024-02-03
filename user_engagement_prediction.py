import streamlit as st
import pandas as pd

# Load your CSV data
# Assuming your CSV has columns 'Website Feature' and 'App Feature'
df = pd.read_csv('features.csv')

def predict_engagement(selected_features):
    # Dummy function for predicting engagement score
    engagement_score = len(selected_features)
    if engagement_score > 20:
        return st.success("Well done! It's user engaging.")
    else:
        return st.write("Not much engaging need to improve.")

st.title("Digital Marketing Engagement Predictor")

# User chooses between website and app features
platform = st.radio("Choose Platform:", ["Website", "App"])

# Display multi-select based on the chosen platform
if platform == "Website":
    features = st.multiselect("Select Website Features:", df['Website Feature'].unique())
else:
    features = st.multiselect("Select App Features:", df['App Feature'].unique())

# Calculate and display engagement prediction
if st.button("Predict Engagement"):
    engagement_score = predict_engagement(features)
    st.success(f"{engagement_score}")
