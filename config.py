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

# ================[proxy]================
USE_PROXY = False # or put True if you want use it
PROXIES = {
    "http":"socks5://127.0.0.1",
    "https":"socks5://127.0.0.1", # if you using socks4 or http only replace it with "socks5"
}
