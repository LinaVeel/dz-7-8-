import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Привет, мир",
    "body": "Это тестовый пост через JSONPlaceholder",
    "userId": 1,
}


def create_post(url: str, data: dict, timeout: int = 10) -> dict:
    try:
        resp = requests.post(url, json=data, timeout=timeout)
        resp.raise_for_status()
        try:
            return resp.json()
        except ValueError as json_err:
            raise RuntimeError(f"Некорректный JSON в ответе: {json_err}")
    except requests.exceptions.Timeout:
        raise TimeoutError("Истек таймаут запроса")
    except requests.exceptions.HTTPError as http_err:

        raise RuntimeError(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise ConnectionError(f"Сетевая ошибка: {req_err}")


if __name__ == "__main__":
    try:
        data = create_post(BASE_URL, payload, timeout=10)
        post_id = data.get("id")
        print(f"Создан пост с ID: {post_id}")
        print("Содержимое ответа:")
        print(data)
    except Exception as e:
        print(f"Не удалось создать пост: {e}")
