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
RE_CHARGE_SPEED_MAX = 7 # max is 11

# config.py

# Dictionary of coordinates and their corresponding colors
PAINT_COORDINATES = {
    (100, 200): "#FFFFFF",  # White
    (300, 400): "#000000",  # Black
    (500, 600): "#00CC78",  # Green
    (700, 800): "#BE0039",  # Red
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
    "45.151.162.198:6600:acgrnzwt:e0zx7luc76ok",
    "154.36.110.199:6853:acgrnzwt:e0zx7luc76ok",
    "104.239.105.125:6655:acgrnzwt:e0zx7luc76ok",
    "167.160.180.203:6754:acgrnzwt:e0zx7luc76ok",
    "173.211.0.148:6641:acgrnzwt:e0zx7luc76ok",
    "107.172.163.27:6543:acgrnzwt:e0zx7luc76ok",
    "207.244.217.165:6712:acgrnzwt:e0zx7luc76ok",
    "198.23.239.134:6540:acgrnzwt:e0zx7luc76ok",
    "38.154.227.167:5868:acgrnzwt:e0zx7luc76ok",
    # Add more proxies as needed
]
