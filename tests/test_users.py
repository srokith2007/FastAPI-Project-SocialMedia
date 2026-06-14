from app import schemas    
from app.configs import settings
from jose import jwt
import pytest



def test_create_user(client):
    response = client.post("/users/", json={"email_id": "xyz@example.com", "password": "password123"})
    new_user = schemas.UserOut(**response.json())
    assert new_user.email_id == "xyz@example.com"
    assert response.status_code == 201

def test_login_user(client,test_user):
    response = client.post("/login", data={"username": test_user['email_id'], "password": test_user['password']})
    print(response.json())
    res = response.json()
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert response.status_code == 200

def test_incorrect_login(client,test_user):
    response = client.post("/login", data={"username": test_user['email_id'], "password": "wrongpassword"})
    assert response.status_code == 403
    