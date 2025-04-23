from fastapi import FastAPI

app = FastAPI()

# Kullanıcı listesi örneği
fake_users_db = [
    {"id": 1, "username": "admin"},
    {"id": 2, "username": "johndoe"},
]

@app.get("/users")
def get_users():
    return fake_users_db

@app.post("/users")
def create_user(user: dict):
    new_id = max([u["id"] for u in fake_users_db]) + 1
    user["id"] = new_id
    fake_users_db.append(user)
    return user
