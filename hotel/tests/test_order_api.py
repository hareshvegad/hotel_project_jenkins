import pytest
from hotel.models import User, Order

@pytest.mark.django_db
def test_create_order_success(api_client):
    user = User.objects.create(email="order@example.com", name="Buyer", number="777")
    response = api_client.post("/api/orders/", {
        "user": str(user.uuid),
        "item_name": "Pasta",
        "quantity": 3,
        "status": "confirmed"
    })
    assert response.status_code == 201
    assert response.data["item_name"] == "Pasta"

@pytest.mark.django_db
def test_create_order_invalid_user(api_client):
    response = api_client.post("/api/orders/", {
        "user": "00000000-0000-0000-0000-000000000000", 
        "item_name": "Burger",
        "quantity": 1,
        "status": "cooked"
    })
    assert response.status_code == 400
    assert "user" in response.data

@pytest.mark.django_db
def test_list_orders_empty(api_client):
    response = api_client.get("/api/orders/")
    assert response.status_code == 200
    assert response.data == []

@pytest.mark.django_db
def test_retrieve_order(api_client):
    user = User.objects.create(email="r@o.com", name="OrderR", number="100")
    order = Order.objects.create(user=user, item_name="Soup", quantity=1, status="served")
    response = api_client.get(f"/api/orders/{order.uuid}/")
    assert response.status_code == 200
    assert response.data["item_name"] == "Soup"

@pytest.mark.django_db
def test_update_order(api_client):
    user = User.objects.create(email="u@o.com", name="OrderU", number="200")
    order = Order.objects.create(user=user, item_name="Rice", quantity=1, status="pending")
    response = api_client.put(f"/api/orders/{order.uuid}/", {
        "user": str(user.uuid),
        "item_name": "Fried Rice",
        "quantity": 2,
        "status": "ready"
    })
    assert response.status_code == 200
    assert response.data["item_name"] == "Fried Rice"
    assert response.data["status"] == "ready"
    

@pytest.mark.django_db
def test_delete_order(api_client):
    user = User.objects.create(email="d@o.com", name="OrderD", number="300")
    order = Order.objects.create(user=user, item_name="Ice Cream", quantity=1, status="delivered")
    response = api_client.delete(f"/api/orders/{order.uuid}/")
    assert response.status_code == 204
    assert not Order.objects.filter(uuid=order.uuid).exists()
