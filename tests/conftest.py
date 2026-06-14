from fastapi.testclient import TestClient
from app import models
from app.main import app
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configs import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models
from app.routers import posts


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()



@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture()
def test_user(client):
    user_data = {"email_id": "xyz@example.com", "password": "password123"}
    response = client.post("/users/", json=user_data)
    user = response.json()
    assert response.status_code == 201
    user["password"] = user_data["password"]
    print(user)
    return user
    
@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture()   
def authorized_client(client, token):
    client.headers = {  
    **client.headers,
    "Authorization": f"Bearer {token}"
    }
    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
    "title": "first title",
    "content": "first content",
    "owner_id": test_user['id']
    }, 
    {
    "title": "2nd title",
    "content": "2nd content",
    "owner_id": test_user['id']
    },
    {
    "title": "3rd title",
    "content": "3rd content",
    "owner_id": test_user['id']
    }]
    def create_post_model (post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    session.commit()
    posts = session.query(models. Post).all()
    return posts