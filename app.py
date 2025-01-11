from flask import Flask, render_template, jsonify, request
import yfinance as yf
import pandas as pd 
import time
import datetime


CRYPTOS = {
    'bitcoin': 'BTC-USD',
    'ethereum': 'ETH-USD',
    'litecoin': 'LTC-USD',
    'ripple': 'XRP-USD',
    'dogecoin': 'DOGE-USD'
}

app = Flask(__name__)

def get_crypto_data(crypto_ticker):
    end_date = datetime.datetime.today()
    start_date = end_date - pd.DateOffset(months=1)
    
    data = yf.download(crypto_ticker, start=start_date, end=end_date)
    
    time.sleep(1) # wait for 1 second to avoid rate limiting

    timestamps = data.index.strftime('%Y-%m-%d').tolist()
    values = data['Close'].values.tolist()
    values = [item for sublist in values for item in sublist]
    return timestamps, values

def calculate_returns(crypto_ticker):
    # Get data for the cryptocurrency
    timestamps, values = get_crypto_data(crypto_ticker)
    
    # Calculate the simple return for the entire period
    initial_price = values[0]
    final_price = values[-1]
    return_percentage = ((final_price - initial_price) / initial_price) * 100
    
    return return_percentage

def get_all_crypto_data(normalized=False):
    print(normalized)
    data = {}
    returns = {}  # To store the returns of each cryptocurrency

    for crypto_name, crypto_ticker in CRYPTOS.items():
        timestamps, values = get_crypto_data(crypto_ticker)
        
        # Calculate returns for each cryptocurrency
        returns[crypto_name] = calculate_returns(crypto_ticker)

        if normalized:
            min_val = min(values)
            max_val = max(values)
            values = [(val - min_val) / (max_val - min_val) for val in values]

        data[crypto_name] = {
            'label': crypto_name.capitalize(),
            'data': values,
            'borderColor': f'#{hash(crypto_name) & 0xFFFFFF:06x}',
            'fill': False
        }
    
    # Returning both the data and the returns for each cryptocurrency
    return {
        'labels': timestamps,
        'datasets': list(data.values()),
        'returns': returns  # Include returns in the returned data
    }

@app.route('/')
def index():
    return render_template('index.html', cryptos=CRYPTOS)

@app.route('/get_data', methods=['POST'])
def get_data():
    crypto = request.form['crypto']
    timestamps, values = get_crypto_data(crypto)
    return jsonify(timestamps=timestamps, values=values)


@app.route('/get_all_data', methods=['GET'])
def get_all_data():
    normalized = request.args.get('normalized', 'false').lower() == 'true'
    data = get_all_crypto_data(normalized)
    return jsonify(data)

@app.route('/get_returns', methods=['GET'])
def get_returns():
    # Get the returns data
    data = get_all_crypto_data()
    returns = data['returns']
    
    return jsonify(returns)

if __name__ == "__main__":
    app.run(debug=True)
