from typing import Dict, List
_users: List[Dict] = []
_next_user_id: int = 1


def create_user(email: str, password: str) -> Dict:
    global _next_user_id

    user = {
        "id": _next_user_id,
        "email": email,
        "password": password,
    }

    _users.append(user)
    _next_user_id += 1
    return user
