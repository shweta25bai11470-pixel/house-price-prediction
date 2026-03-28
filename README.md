#  House Price Prediction using Machine Learning

## Overview

This project predicts house prices using machine learning based on features such as square footage, number of bedrooms (BHK), construction status, and geographical location. It also includes an interactive system where users can input their own property details to get real-time price predictions.

---

## Problem Statement

The goal of this project is to build a model that can estimate house prices based on various property features. This helps in understanding how different factors influence pricing in the real estate market.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn

---

## Features Used

* Square feet area (`SQUARE_FT`)
* Number of bedrooms (`BHK_NO.`)
* Under construction status
* RERA approval
* Ready to move
* Resale
* Latitude and Longitude
* Seller type (`POSTED_BY`)
* Property type (`BHK/RK`)

---

## Model Used

* Linear Regression

---

## Model Performance

* Mean Absolute Error (MAE): ~131
* R² Score: ~0.40

---

## Project Structure

* `house-price-prediction.py` → Main Python script
* `Train.csv` → Dataset
* `README.md` → Project documentation

---

## How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/house-price-prediction.git
```

### 2. Navigate to the folder

```
cd house-price-prediction
```

### 3. Install required libraries

```
pip install pandas scikit-learn
```

### 4. Run the program

```
python house-price-prediction.py
```

---

## Example Output

The program will:

* Show model evaluation metrics (MAE, R²)
* Ask for user input
* Predict house price based on input

---

## Features of the Project

* Complete machine learning pipeline
* Data preprocessing and feature engineering
* Model training and evaluation
* Interactive user input for real-time prediction

---

## Limitations

The model provides moderate accuracy and may not capture all real-world factors affecting house prices.

---

## Future Improvements

* Use advanced models like Random Forest
* Add data visualization
* Build a web-based interface (Streamlit)

---

## Made by

Shweta Kumari 25BAI11470
