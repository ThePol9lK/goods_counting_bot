import requests

def get_admin_users() -> list:
    """
    Получает список администраторов из API.

    :return: Список администраторов
    """
    response = requests.get("http://10.5.0.5:8000/user/all")
    if response.status_code == 200:
        users = response.json()
        admin_users = [user for user in users if user.get("admin")]

        return admin_users
    else:
        print(f"Ошибка при запросе к API: {response.status_code}")
        return []