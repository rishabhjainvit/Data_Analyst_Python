# kiteapp.py

from kiteconnect import KiteConnect

# Initialize Kite API using your API key
api_key = "your_api_key_here"
api_secret = "your_api_secret_here"

# Initialize KiteConnect instance
kite = KiteConnect(api_key=api_key)

# Function to generate session and access token
def login_and_get_access_token(request_token):
    # Generate access token using the request token and API secret
    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
        kite.set_access_token(data["access_token"])
        print("Login successful. Access token:", data["access_token"])
    except Exception as e:
        print("Error generating session:", e)
    
    return kite

# Function to fetch live market data for a symbol
def fetch_live_market_data(symbol):
    try:
        # Fetch live quote for the symbol
        live_data = kite.ltp("NSE:" + symbol)
        print(f"Live market data for {symbol}:", live_data)
    except Exception as e:
        print("Error fetching market data:", e)

# Function to place a buy order
def place_order(symbol, quantity):
    try:
        order = kite.place_order(
            tradingsymbol=symbol,
            exchange="NSE",
            transaction_type="BUY",
            quantity=quantity,
            order_type="MARKET",
            product="CNC",  # Cash and carry product for delivery
            variety="regular"
        )
        print("Order placed successfully:", order)
    except Exception as e:
        print("Error placing order:", e)

# Example usage of the above functions
if __name__ == "__main__":
    # Enter your request token here (after generating it manually)
    request_token = "your_request_token_here"
    
    # Step 1: Log in and get the access token
    kite = login_and_get_access_token(request_token)

    # Step 2: Fetch live market data for a symbol (e.g., INFY)
    fetch_live_market_data("INFY")

    # Step 3: Place a buy order for a symbol (e.g., INFY)
    place_order("INFY", 10)
