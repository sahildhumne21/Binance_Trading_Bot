from logger import setup_logger
import binance_api as api

def main():
    logger = setup_logger()
    logger.info("Starting Binance Testnet Bot")

    # 1️⃣ Check server time
    server_time = api.get_server_time(logger)
    print("Server Time:", server_time)

    # 2️⃣ Get account info
    account = api.get_account_info(logger)
    if "error" in account:
        print("Failed to fetch account:", account["error"])
        return
    print("Can Trade:", account.get("canTrade", "Unknown"))

    # 3️⃣ Place market order (example)
    print("\nPlacing Market BUY Order for BTCUSDT...")
    order_resp = api.place_order(symbol="BTCUSDT", side="BUY", order_type="MARKET", quantity=0.001, logger=logger)
    print(order_resp)


if __name__ == "__main__":
    main()
