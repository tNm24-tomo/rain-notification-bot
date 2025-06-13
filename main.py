# import requests
# import os
# from dotenv import load_dotenv

# # .envを読み込む
# load_dotenv()

# # 環境変数から値を取得
# API_KEY = os.getenv("OPENWEATHER_API_KEY")
# LAT = os.getenv("LAT")
# LON = os.getenv("LON")
# LINE_TOKEN = os.getenv("LINE_TOKEN")
# USER_ID = os.getenv("USER_ID")

# def get_weather():
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&lang=ja"
#     res = requests.get(url)
#     data = res.json()
#     return data["weather"][0]["description"]

# def send_line_message(message):
#     url = "https://api.line.me/v2/bot/message/push"
#     headers = {
#         "Authorization": f"Bearer {LINE_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     body = {
#         "to": USER_ID,
#         "messages": [{"type": "text", "text": message}]
#     }
#     requests.post(url, headers=headers, json=body)

# weather = get_weather()
# if "雨" in weather:
#     send_line_message(f"今日の天気は「{weather}」です。傘を忘れずに☂️")
# else:
#     print("雨ではありません")


# ----------------------------------------------------------------------------
# 以下テストコード

# weather_notify.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
LAT = os.getenv("LAT")
LON = os.getenv("LON")
LINE_TOKEN = os.getenv("LINE_TOKEN")
USER_ID = os.getenv("USER_ID")

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&lang=ja"
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    return data["weather"][0]["description"]

def send_line_message(message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {LINE_TOKEN}",
        "Content-Type": "application/json"
    }
    body = {
        "to": USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    requests.post(url, headers=headers, json=body)

def main():
    weather = get_weather()
    if "雨" in weather:
        send_line_message(f"今日の天気は「{weather}」です。傘を忘れずに☂️")
    else:
        print("雨ではありません")

if __name__ == "__main__":
    main()
