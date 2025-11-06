import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200, "Неверный статус-код"
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0, "Список постов пуст"


def test_create_post():
    payload = {"title": "QA test", "body": "Autotest example", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, "Пост не создан"
    data = response.json()
    assert data["title"] == payload["title"]
    assert "id" in data, "Нет ID в ответе"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code in [200, 204], "Удаление прошло некорректно"
