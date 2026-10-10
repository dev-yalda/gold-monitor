import os
import requests

def get_gold_price():
    # دریافت قیمت سکه یا طلا
    url = "https://api.tgju.org/v1/price/current?item=sekee"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        price = data["data"]["p"]
        return f"قیمت لحظه‌ای سکه: {int(price):,} تومان"
    except Exception as e:
        return f"خطا در دریافت قیمت: {e}"

def send_alert(message):
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    if token and chat_id:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        requests.post(url, data={"chat_id": chat_id, "text": message})
    else:
        print(message)

if __name__ == "__main__":
    msg = get_gold_price()
    send_alert(msg)

