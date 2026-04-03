import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('sleep_model.pkl')

# Title
st.title("SleepLens")
st.subheader("Find out if your lifestyle is affecting your sleep")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 18, 60, 25)
occupation = st.selectbox("Occupation", ["Software Engineer", "Doctor", "Teacher", "Nurse", "Engineer", "Accountant", "Scientist", "Lawyer", "Salesperson", "Manager"])
sleep_duration = st.slider("Sleep Duration (hours)", 4.0, 10.0, 7.0)
quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10, 5)
physical_activity = st.slider("Physical Activity Level (mins/day)", 0, 90, 30)
stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
bmi_category = st.selectbox("BMI Category", ["Normal", "Normal Weight", "Overweight", "Obese"])
heart_rate = st.slider("Heart Rate (bpm)", 60, 100, 70)
daily_steps = st.slider("Daily Steps", 1000, 20000, 5000)

# Encode inputs manually
gender_enc = 1 if gender == "Male" else 0
occupation_map = {"Accountant":0,"Doctor":1,"Engineer":2,"Lawyer":3,"Manager":4,"Nurse":5,"Salesperson":6,"Scientist":7,"Software Engineer":8,"Teacher":9,"Sales Representative":10}
bmi_map = {"Normal":0, "Normal Weight":1, "Obese":2, "Overweight":3}
blood_pressure_enc = 11

occupation_enc = occupation_map[occupation]
bmi_enc = bmi_map[bmi_category]

# Predict button
if st.button("Analyze My Sleep"):
    input_data = np.array([[gender_enc, age, occupation_enc, sleep_duration,
                            quality_of_sleep, physical_activity, stress_level,
                            bmi_enc, blood_pressure_enc, heart_rate, daily_steps]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 0:
        st.error("Detected: Insomnia")
        st.write("**What this means:** Difficulty falling or staying asleep")
        st.write("**Advice:**")
        st.write("- Avoid screens 1 hour before bed")
        st.write("- Maintain a consistent sleep schedule")
        st.write("- Limit caffeine after 2pm")

    elif prediction == 1:
        st.success("No Sleep Disorder Detected")
        st.write("**Your lifestyle looks healthy!**")
        st.write("**Keep it up:**")
        st.write("- Maintain your current activity level")
        st.write("- Keep stress in check")
        st.write("- Stay consistent with sleep timing")

    else:
        st.warning("Detected: Sleep Apnea")
        st.write("**What this means:** Breathing interruptions during sleep")
        st.write("**Advice:**")
        st.write("- Maintain a healthy BMI")
        st.write("- Sleep on your side instead of your back")
        st.write("- Consult a doctor if symptoms persist")