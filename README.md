# 📈 Stock Price Predictor

A Machine Learning based web application that predicts the next day's stock closing price using **Linear Regression**.

The application is built using **Python, Flask, HTML, CSS, Scikit-learn, Pandas, and yFinance**.

---

# Features

- Predict next day's stock price
- Download live historical stock data
- Machine Learning using Linear Regression
- Beautiful and responsive web interface
- Displays current stock price
- Displays predicted stock price
- Shows model accuracy
- Displays stock price graph
- Handles invalid stock symbols

---

# Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- yFinance

---

# Project Structure

```
Stock-Price-Predictor/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── graphs/
│
└── screenshots/
```

---

# Installation

## Step 1

Clone the project

```
git clone <repository-link>
```

Or download the ZIP file.

---

## Step 2

Open the project folder in VS Code.

---

## Step 3

Install all required libraries.

```
pip install -r requirements.txt
```

---

## Step 4

Run the Flask application.

```
python app.py
```

---

## Step 5

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# How to Use

1. Open the application.
2. Enter a stock symbol.

Examples

```
AAPL
TSLA
MSFT
GOOGL
AMZN
RELIANCE.NS
TCS.NS
INFY.NS
```

3. Click the **Predict** button.
4. The application will display:

- Current Price
- Predicted Next Day Price
- Model Accuracy
- Historical Stock Graph

---

# Machine Learning Workflow

```
Historical Stock Data
          │
          ▼
Data Cleaning
          │
          ▼
Feature Engineering
          │
          ▼
Train-Test Split
          │
          ▼
Linear Regression Model
          │
          ▼
Prediction
          │
          ▼
Display Result
```

---

# Screenshots

Add screenshots here after running the project.

Example:

- Home Page
- Prediction Result
- Graph

---

# Future Improvements

- LSTM Deep Learning Model
- Multiple Stock Comparison
- Candlestick Charts
- Live Stock Market Dashboard
- Download Prediction Report
- User Login System
- Dark Mode
- Prediction History

---

# Author

Rakshita Patil

MCA Student

Machine Learning & Data Science Enthusiast

---

# License

This project is developed for educational purposes.