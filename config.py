# config.py

# List of query data for each account
QUERY_DATA = [
    "",
    "",
    # Add more accounts as needed
]

# =============[upgrades]================
# default is 5 level you can change it your self
PAINT_REWARD_MAX = 5 # max is 7
ENERGY_LIMIT_MAX = 5 # max is 6
RE_CHARGE_SPEED_MAX = 5 # max is 11

# config.py

# Dictionary of coordinates and their corresponding colors
PAINT_COORDINATES = {
    (100, 200): "#FFFFFF",  # White
    (300, 400): "#000000",  # Black
    (500, 600): "#00CC78",  # Green
    (700, 800): "#BE0039",  # Red
    # Add more coordinates and colors as needed
}

# ================[proxy]================
USE_PROXY = True # or put True if you want use it
# List of proxies in the format: ip:port:username:password
PROXIES = [
    "206.41.172.74:6634:stwajhwx:tmrt92jg3099",
    "another.proxy.ip:port:username:password",  # Add more proxies as needed
]
