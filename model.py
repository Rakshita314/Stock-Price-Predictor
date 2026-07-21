import os
import warnings

import matplotlib
matplotlib.use("Agg")  # Required for Flask

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


def predict_stock(symbol):
    """
    Downloads historical stock data,
    trains a Linear Regression model,
    predicts the next day's closing price,
    and saves a graph.
    """

    # Download historical data
    df = yf.download(
        symbol,
        period="2y",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    # Check if data exists
    if df.empty:
        raise Exception("Invalid stock symbol or no data found.")

    # Keep only Close price
    df = df[["Close"]].copy()

    # Remove missing values
    df.dropna(inplace=True)

    # Create next-day prediction column
    df["Target"] = df["Close"].shift(-1)

    # Remove last row
    df.dropna(inplace=True)

    # Features and labels
    X = df[["Close"]]
    y = df["Target"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Accuracy
    y_pred = model.predict(X_test)
    accuracy = r2_score(y_test, y_pred) * 100

    # Current Price
    current_price = float(df["Close"].iloc[-1])

    # Predict Next Day Price
    next_price = float(
        model.predict(pd.DataFrame([[current_price]], columns=["Close"]))[0]
    )

    # Create graph folder
    os.makedirs("static/graphs", exist_ok=True)

    graph_name = f"{symbol}.png"
    graph_path = os.path.join("static", "graphs", graph_name)

    # Plot graph
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], color="royalblue", linewidth=2)
    plt.title(f"{symbol} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()

    return {
        "symbol": symbol,
        "current_price": round(current_price, 2),
        "predicted_price": round(next_price, 2),
        "accuracy": round(accuracy, 2),
        "graph": f"graphs/{graph_name}"
    }