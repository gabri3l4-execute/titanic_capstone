# User Guide

This guide explains how to use the Titanic Survival Prediction web application.

---

## Table of Contents

1. Accessing the Application
2. Making a Prediction
3. Viewing History
4. Understanding Results

---

## 1. Accessing the Application

- Open web browser
- Navigate to: `http://127.0.0.1:8000/` (for local setup)
- Or visit: [production URL if deployed]
- The home page provides navigation links: **Home**, **Predict**, **History**.

---

## 2. Making a Prediction

1. Click **Predict** in navigation bar.
2. Fill in passenger information form:
   - Name (enter name with title)
   - Sex (Choose male or female)
   - Age (enter number)
   - PassengerClass (Select 1st, 2nd, or 3rd class.)
   - Siblings/Spouses Aboard (Number of siblings or spouses.)
   - Parent/Children Aboard (Number of parent or children travel with.)
   - Fare (Ticket fare (e.g., 25.35))
   - Port of embarkation (Port of embarkation (Cherbourg, Queenstown, Southampton))
3. Click **Predict Survival** button.
4. The prediction result will appear below the form:
   - ✅ **Survived** (with probability)
   - ❌ **Did Not Survive** (with probability)
5. The prediction is automatically saved to your history.


---

## 3. Viewing Prediction History

- Click **History** in navigation bar.
- You will see a table listing all previous predictions with:
  - Date and time
  - Passenger details
  - Survival outcome

---

## 4. Understanding Results

- **Survived**: Model predicts passenger survived
- **Did Not Survive**: Model predicts passenger died
- **Probability**: Confidence level (0-100%)

---

## Notes

- All fields are required unless marked optional.
- The model is a pre-trained classifier; predictions are for educational purposes.
