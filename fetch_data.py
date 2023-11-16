import datetime
import finnhub
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Set up the Finnhub client
finnhub_api_key = 'Your finnhub_api_key HERE'
finnhub_client = finnhub.Client(api_key=finnhub_api_key)

def get_stock_price_from_api(symbol):
    # Fetch actual stock price
    actual_price = finnhub_client.quote(symbol)['c']

    # Fetch previous stock price (closing price from the previous day)
    start_date = int((datetime.datetime.now() - datetime.timedelta(days=2)).timestamp())
    end_date = int((datetime.datetime.now() - datetime.timedelta(days=1)).timestamp())
    resolution = 'D'
    prev_price = finnhub_client.stock_candles(symbol, resolution, start_date, end_date)['c'][-1]

    print(f"Raw Data from API - Actual Price: {actual_price}, Previous Price: {prev_price}")

    return actual_price, prev_price

# Define the stock symbol
symbol = 'AAPL'

# Get actual and previous stock prices
actual_price, prev_price = get_stock_price_from_api(symbol)

# Print the results
print(f"Actual Price from API: {actual_price}")
print(f"Previous Price from API: {prev_price}")

def predict_next_30_seconds(symbol):
    # Fetch historical data for the last 7 days
    start_date = int((datetime.datetime.now() - datetime.timedelta(days=7)).timestamp())
    end_date = int(datetime.datetime.now().timestamp())
    resolution = '1'
    historical_data = finnhub_client.stock_candles(symbol, resolution, start_date, end_date)

    # Create a DataFrame from the historical data
    df = pd.DataFrame(historical_data)
    df['t'] = pd.to_datetime(df['t'], unit='s')
    df.set_index('t', inplace=True)

    # Feature engineering: Use time as a feature (you can add more features)
    df['timestamp'] = df.index.astype('int64') // 10 ** 9  # Convert nanoseconds to seconds
    X = df[['timestamp']]
    y = df['c']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions for the next 30 seconds
    next_30_seconds_timestamp = int((datetime.datetime.now() + datetime.timedelta(seconds=30)).timestamp())
    next_30_seconds_prediction = model.predict(np.array([[next_30_seconds_timestamp]]))[0]

    return next_30_seconds_prediction

# Get prediction for the next 30 seconds
next_30_seconds_prediction = predict_next_30_seconds(symbol)
print(f"Prediction for the Next 30 Seconds: {next_30_seconds_prediction}")
