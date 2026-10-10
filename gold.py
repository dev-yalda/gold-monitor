import requests

URL = "https://api.tgju.org/v1/price/current?item=sekee"

def get_gold_price():
    response = requests.get(URL)
    data = response.json()
    price = data["data"]["p"]  # قیمت سکه به تومان
    return int(price)

if __name__ == "__main__":
    price = get_gold_price()
    print(f"قیمت سکه: {price:,} تومان")

