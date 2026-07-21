from flask import Flask, render_template, request
from model import predict_stock

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    stock_symbol = request.form['symbol'].strip().upper()

    try:
        result = predict_stock(stock_symbol)

        return render_template(
            "result.html",
            symbol=result["symbol"],
            current_price=result["current_price"],
            predicted_price=result["predicted_price"],
            accuracy=result["accuracy"],
            graph=result["graph"]
        )

    except Exception as e:
        return render_template(
            "result.html",
            error=str(e)
        )


if __name__ == "__main__":
    app.run(debug=True)