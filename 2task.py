import requests

API_KEY = "39a691d4456e089afb2ccc688a32ce9a"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Введите город: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "ru",
}

resp = requests.get(BASE_URL, params=params, timeout=10)


if resp.status_code == 404:
    raise ValueError("Город не найден. Проверьте написание и попробуйте снова.")
resp.raise_for_status()  

data = resp.json()


cod = str(data.get("cod", "200"))
if cod != "200":
    msg = data.get("message", "Неизвестная ошибка")
    raise ValueError(f"Ошибка от API: {msg}")

temp = data["main"]["temp"]
desc = data["weather"][0]["description"]

print(f"В {city}: {temp} °C, {desc}")