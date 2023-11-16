# Stock Price Prediction

This project utilizes machine learning to predict stock prices in real-time, fetching data from the Finnhub API and providing predictions for the next 30 seconds.

## Getting Started

### Prerequisites

- Git
- Python 3.6 or higher
- Pip

### Installation

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/your-username/stock-price-prediction.git
    cd stock-price-prediction
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Obtain a Finnhub API key:**

    - Visit [Finnhub](https://finnhub.io/) to get your API key.

4. **Update the Finnhub API key:**

    - Open `fetch_data.py` and update the `finnhub_api_key` variable with your key.

5. **Run the Flask application:**

    ```bash
    python app.py
    ```

6. **Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).**

## Contributions

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests. Please follow the [Contribution Guidelines](

## License
This project is licensed under the MIT License - see the LICENSE file for details.