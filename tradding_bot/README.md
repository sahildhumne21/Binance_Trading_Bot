

## 🧾 README.md — Binance Futures Testnet Trading Bot

# 🚀 Binance Futures Testnet Trading Bot (USDT-M)

A simple Python-based trading bot for the **Binance Futures Testnet**, designed to help users understand API-based trading.
It supports **market** and **limit** orders, both **buy** and **sell** sides, and includes **logging**, **error handling**, and **command-line input validation**.



## 🧠 Features

✅ Place **Market** and **Limit** orders
✅ Supports **BUY** and **SELL** sides
✅ Connects to **Binance Futures Testnet (USDT-M)**
✅ Logs all **requests, responses, and errors**
✅ Validates user input via **command line**
✅ Fetches **account status** after order execution



## ⚙️ Requirements

Install the dependencies using pip:

```bash
pip install requests python-dotenv
```



## 🔑 Setup Instructions

1. Create a **Binance Futures Testnet** account:
   👉 [https://testnet.binancefuture.com](https://testnet.binancefuture.com)

2. Generate your **API Key** and **Secret Key** from your Testnet dashboard.

3. Create a `.env` file in your project directory:

   ```
   BINANCE_API_KEY=your_api_key_here
   BINANCE_SECRET_KEY=your_secret_key_here
   ```

4. Run the bot:

   ```bash
   python trading_bot.py
   ```



## 💻 Command-Line Example

```
🚀 Binance Futures Testnet Trading Bot (USDT-M)
-----------------------------------------------
Enter trading pair (e.g., BTCUSDT): BTCUSDT
Enter order side (BUY/SELL): BUY
Enter order type (MARKET/LIMIT): LIMIT
Enter quantity: 0.001
Enter price: 65000
```


## 🧩 File Structure


📂 binance-trading-bot/
 ├── trading_bot.py        # Main bot code
 ├── .env                  # Your API credentials (not uploaded to GitHub)
 ├── trading_bot.log       # Log file with request/response details
 ├── README.md             # Documentation
```



## 🧾 Logging

All API requests, responses, and errors are saved to a file named:

```
trading_bot.log
```

This helps debug and verify successful order placements.



## 🧠 Future Enhancements

* Add **Stop-Limit** and **OCO orders**
* Integrate **WebSocket live order updates**
* Add **automatic balance monitoring**



## 👩‍💻 Author

**anisha Anil Kiratkar**
Electrical Engineering Student | Python Developer |  AI Engineer
📧 [anishakhiratkar2003@gmail.com]
🌐 [https://github.com/anishakiratkar/binance-trading-bot
]



Would you like me to include a short **GitHub project description** and **tags** (so it looks more professional when you upload it)?
