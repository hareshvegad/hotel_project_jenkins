import pytest
from hotel.models import User

@pytest.mark.django_db
def test_create_user_success(api_client):
    response = api_client.post("/api/users/", {
        "email": "test@example.com",
        "name": "Test User",
        "number": "1234567890"
    })
    assert response.status_code == 201
    assert response.data["email"] == "test@example.com"

@pytest.mark.django_db
def test_create_user_missing_field(api_client):
    response = api_client.post("/api/users/", {
        "name": "Missing Email",
        "number": "1234567890"
    })
    assert response.status_code == 400
    assert "email" in response.data

@pytest.mark.django_db
def test_list_users_empty(api_client):
    response = api_client.get("/api/users/")
    assert response.status_code == 200
    assert response.data == []

@pytest.mark.django_db
def test_retrieve_user(api_client):
    user = User.objects.create(email="retrieve@example.com", name="R", number="000")
    response = api_client.get(f"/api/users/{user.uuid}/")
    assert response.status_code == 200
    assert response.data["email"] == user.email

@pytest.mark.django_db
def test_update_user(api_client):
    user = User.objects.create(email="old@example.com", name="Old", number="111")
    response = api_client.put(f"/api/users/{user.uuid}/", {
        "email": "updated@example.com",
        "name": "Updated",
        "number": "222",
        "is_active": True,
    })
    assert response.status_code == 200
    assert response.data["email"] == "updated@example.com"

@pytest.mark.django_db
def test_delete_user(api_client):
    user = User.objects.create(email="delete@example.com", name="Del", number="999")
    response = api_client.delete(f"/api/users/{user.uuid}/")
    assert response.status_code == 204
    assert not User.objects.filter(uuid=user.uuid).exists()
