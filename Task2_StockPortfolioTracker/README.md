# 📈 Stock Portfolio Tracker

A Python script that reads stock holdings from a CSV file, calculates current investment value and profit/loss, and generates a formatted report. Built as part of the **CodeAlpha Python Development Internship** (Task 2: Stock Portfolio Tracker).

---

## 🚀 Features

- 📥 Reads holdings from CSV (symbol, quantity, buy price)
- 💰 Calculates invested amount, current value, and P/L
- 📊 Prints a clean tabular report to terminal
- 💾 Exports results to `output/portfolio_report.csv`
- 🛡️ Gracefully handles missing/invalid rows
- 🧮 Uses Python standard library only (no dependencies)

---

## 📁 Project Structure

```
Task2_StockPortfolioTracker/
│
├── src/
│   └── portfolio_tracker.py       # Main script
├── data/
│   └── stocks.csv                 # Input holdings
├── output/
│   └── portfolio_report.csv       # Generated report
├── screenshots/
│   └── demo.png
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🛠️ Requirements

- Python 3.8 or higher
- No external libraries needed

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/anshumanhq/codealpha_tasks.git
   cd codealpha_tasks/Task2_StockPortfolioTracker
   ```

2. **Run the tracker**
   ```bash
   python src/portfolio_tracker.py
   ```

3. **Check the report**
   - Terminal pe formatted table dikhega
   - `output/portfolio_report.csv` me CSV report save hogi

---

## 📥 Input Format (`data/stocks.csv`)

```csv
symbol,quantity,buy_price
AAPL,10,150.00
GOOGL,5,2800.00
MSFT,8,310.50
```

| Column | Description |
|--------|-------------|
| `symbol` | Stock ticker (e.g., AAPL) |
| `quantity` | Number of shares |
| `buy_price` | Purchase price per share |

---

## 🧠 How It Works

1. **Read CSV** — `csv.DictReader` se holdings load karta hai
2. **Lookup prices** — `CURRENT_PRICES` dict se current market price uthata hai
3. **Calculate** — invested, current value, P/L, percentage
4. **Display** — formatted table print karta hai
5. **Export** — results ko naye CSV me save karta hai

---

## 🔮 Future Improvements

- 🌐 Fetch live prices from an API (e.g., `yfinance`, Alpha Vantage)
- 📊 Add charts using `matplotlib`
- 🖥️ Build a Streamlit/Flask UI
- 🗄️ Store history in SQLite

---

## 👨‍💻 Author

**Anshuman Singh**
- GitHub: [@anshumanhq](https://github.com/anshumanhq)
- Email: anshumansingh3697@gmail.com

---

## 📜 License

MIT License — see [LICENSE](./LICENSE) file for details.

---

## 🙏 Acknowledgement

Thanks to **CodeAlpha** for the internship opportunity.