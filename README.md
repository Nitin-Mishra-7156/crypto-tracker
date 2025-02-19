# CryptoTracker - Cryptocurrency Dashboard

**CryptoTracker** is a web-based cryptocurrency dashboard built using Flask, Python, and Chart.js. It allows users to track and compare trends in the prices of various cryptocurrencies, visualize data through interactive charts, and view returns on investment for each cryptocurrency. The application provides real-time data and supports dynamic cryptocurrency selection, normalization comparison, and more.

---

## Features

- **Real-Time Data**: View real-time cryptocurrency data such as Bitcoin, Ethereum, Litecoin, Ripple, and Dogecoin.
- **Line Charts**: Interactive line charts to visualize cryptocurrency price trends.
- **Comparison Charts**: Compare the price of multiple cryptocurrencies over time.
- **Normalization Comparison**: Visualize the normalized price comparison between cryptocurrencies.
- **Returns**: Calculate and display the percentage returns for each cryptocurrency over the last month.
- **Dynamic Selection**: Select a specific cryptocurrency from a dropdown to visualize its data.

---

## Technologies Used

- **Backend**: 
  - Python 3
  - Flask (Web framework)
  - yfinance (To fetch cryptocurrency data)
  - Pandas (For data manipulation)
  
- **Frontend**:
  - HTML5
  - Bootstrap 5 (For responsive design)
  - Chart.js (For data visualization)
  - jQuery (For AJAX requests)

---

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/cryptotracker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd cryptotracker
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use 'venv\Scripts\activate'
   ```

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open a browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

3. You will be able to select cryptocurrencies, view interactive charts, and track returns.

---

## API Endpoints

- **GET `/get_all_data`**: Fetches data for all cryptocurrencies.
- **GET `/get_returns`**: Fetches the percentage return for each cryptocurrency.
- **POST `/get_data`**: Fetches data for a specific cryptocurrency.

---

## Folder Structure

```
cryptotracker/
│
├── app.py             # Flask application logic
├── templates/         # HTML templates
│   └── base.html     # Main dashboard HTML template
│   └── footer.html
│   └── header.html
│   └── index.html 
├── static/            # Static files (CSS, JS)
│   └── style.css      # Custom styles (if any)
└── README.md          # Project README
```

---


## Acknowledgments

- **yfinance**: For providing easy access to historical financial data.
- **Chart.js**: For creating beautiful and interactive charts.
- **Bootstrap**: For responsive, mobile-first design.


![image](https://github.com/user-attachments/assets/99c4b26d-6945-481a-a9b9-310c5970a0c3)
![image](https://github.com/user-attachments/assets/23e90d70-baaa-4d22-91af-dfdb3445cd69)
![image](https://github.com/user-attachments/assets/a2d79575-d638-492f-8d9c-88154d92fdbb)
![image](https://github.com/user-attachments/assets/90256e0c-6a99-43b6-9b25-d88da78b68ab)
