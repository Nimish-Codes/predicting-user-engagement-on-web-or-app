import streamlit as st
import pandas as pd

# Load your CSV data
# Assuming your CSV has columns 'Website Feature' and 'App Feature'
df = pd.read_csv('features.csv')

def predict_engagement(selected_features):
    # Dummy function for predicting engagement score
    engagement_score = len(selected_features)
    if engagement_score > 20:
        return "Well done! It's user engaging."
    else:
        return "Not much engaging. Need to improve."

st.title("Digital Marketing Engagement Predictor")

# User chooses between website and app features
platform = st.radio("Choose Platform:", ["Website", "App"])

# Strip whitespaces from the column names
df.columns = df.columns.str.strip()

# Display multi-select based on the chosen platform
if platform == "Website":
    features = st.multiselect("Select Website Features:", df['Website Feature'].unique())
else:
    features = st.multiselect("Select App Features:", df['App Feature'].unique())

# Calculate and display engagement prediction
if st.button("Predict Engagement"):
    engagement_score = predict_engagement(features)
    st.success(engagement_score)
