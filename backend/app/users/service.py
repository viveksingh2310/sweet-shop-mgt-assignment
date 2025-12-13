_fake_users_db = []
_id_counter = 1

def create_user(email: str, password: str):
    global _id_counter

    user = {
        "id": _id_counter,
        "email": email,
        "password": password  # hashing comes later
    }
    _fake_users_db.append(user)
    _id_counter += 1
    return user
