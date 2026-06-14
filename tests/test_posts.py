def test_create_post(authorized_client, test_user):
    response = authorized_client.post("/posts/", json={"title": "Test boys", "content": "Billy Butcher vs Supes."})
    post = response.json()
    assert response.status_code == 201


def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    print(res.json())
    assert res.status_code == 200