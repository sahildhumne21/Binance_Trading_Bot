import os, time, hmac, hashlib, requests
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_SECRET")
BASE = "https://testnet.binance.vision/api"  # Binance Testnet

headers = {"X-MBX-APIKEY": API_KEY}

# --- Helper to sign parameters ---
def _sign(params: dict):
    query = urlencode(params)
    signature = hmac.new(API_SECRET.encode(), query.encode(), hashlib.sha256).hexdigest()
    return f"{query}&signature={signature}"

# --- Generic API call wrapper with logging ---
def _api_request(method, endpoint, params=None, logger=None):
    try:
        url = f"{BASE}{endpoint}"
        if method == "GET":
            r = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            query = _sign(params)
            r = requests.post(f"{url}?{query}", headers=headers)
        else:
            raise ValueError("Unsupported method")

        if logger:
            logger.info(f"{method} {endpoint} -> {r.status_code} | {r.text[:200]}")

        r.raise_for_status()
        return r.json()

    except requests.RequestException as e:
        if logger:
            logger.error(f"API Error: {e}")
        return {"error": str(e)}

# --- REST Endpoints ---
def get_server_time(logger=None):
    return _api_request("GET", "/v3/time", None, logger)

def get_account_info(logger=None):
    ts = int(time.time() * 1000)
    params = {"timestamp": ts}
    query = _sign(params)
    url = f"{BASE}/v3/account?{query}"
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        if logger:
            logger.info(f"GET /v3/account -> {r.status_code} | {r.text[:200]}")
        return r.json()
    except requests.RequestException as e:
        if logger:
            logger.error(f"Account Info Error: {e}")
        return {"error": str(e)}

def place_order(symbol, side, order_type, quantity=None, price=None, stopPrice=None, logger=None):
    ts = int(time.time() * 1000)
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "timestamp": ts
    }

    # Add optional fields
    if quantity:
        params["quantity"] = str(quantity)
    if price:
        params["price"] = str(price)
    if stopPrice:
        params["stopPrice"] = str(stopPrice)

    return _api_request("POST", "/v3/order", params, logger)

# Example for OCO (One Cancels the Other) Order
def place_oco_order(symbol, side, quantity, price, stopPrice, stopLimitPrice, logger=None):
    ts = int(time.time() * 1000)
    params = {
        "symbol": symbol,
        "side": side,
        "quantity": str(quantity),
        "price": str(price),
        "stopPrice": str(stopPrice),
        "stopLimitPrice": str(stopLimitPrice),
        "stopLimitTimeInForce": "GTC",
        "timestamp": ts
    }
    return _api_request("POST", "/v3/order/oco", params, logger)

