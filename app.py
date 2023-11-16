from flask import Flask, render_template, jsonify
from fetch_data import get_stock_price_from_api, predict_next_30_seconds

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch actual and previous prices
    actual_price, previous_price = get_stock_price_from_api("AAPL")

    # Predict the next 30 seconds
    next_30_seconds_prediction = predict_next_30_seconds("AAPL")

    return render_template('index.html',
                           actual_price=actual_price,
                           previous_price=previous_price,
                           next_30_seconds_prediction=next_30_seconds_prediction)

@app.route('/update_prices')
def update_prices():
    actual_price, previous_price = get_stock_price_from_api("AAPL")
    next_30_seconds_prediction = predict_next_30_seconds("AAPL")

    return jsonify({'actual_price': actual_price,
                    'previous_price': previous_price,
                    'next_30_seconds_prediction': next_30_seconds_prediction})

if __name__ == '__main__':
    app.run(debug=True)
