
import requests

url = "https://api.coindcx.com/exchange/v1/markets_details"
response = requests.get(url)
data = response.json()

# ROSE ile ilgili olanları filtrele
btc_data = [market for market in data if 'ROSE' in market.get('symbol', '')]

# Filtrelenmiş verilerin min ve max değerlerini ekrana yazdır
for market in btc_data:
    print(f"Symbol: {market['symbol']}")
    print(f"Min Price: {market.get('min_price', 'N/A')}")
    print(f"Max Price: {market.get('max_price', 'N/A')}")
    print("---------")
