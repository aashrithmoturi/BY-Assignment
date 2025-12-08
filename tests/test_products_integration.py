def test_create_product(client):
    payload = {
        "name": "Laptop",
        "price": 999.99,
        "category": "Electronics"
    }

    response = client.post("/products/", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["id"] > 0
    assert data["name"] == payload["name"]
    assert data["price"] == payload["price"]
    assert data["category"] == payload["category"]


def test_get_all_products(client):
    # Insert two products
    product1 = {"name": "A", "price": 10, "category": "X"}
    product2 = {"name": "B", "price": 20, "category": "Y"}

    client.post("/products/", json=product1)
    client.post("/products/", json=product2)

    response = client.get("/products/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2


def test_get_product_by_id_success(client):
    product = {"name": "Watch", "price": 50, "category": "Fashion"}
    create_resp = client.post("/products/", json=product)
    pid = create_resp.json()["id"]

    response = client.get(f"/products/{pid}")

    assert response.status_code == 200
    assert response.json()["name"] == "Watch"


def test_get_product_by_id_not_found(client):
    response = client.get("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_update_product(client):
    product = {"name": "Phone", "price": 400, "category": "Electronics"}
    create_resp = client.post("/products/", json=product)
    pid = create_resp.json()["id"]

    update = {"price": 500}

    response = client.put(f"/products/{pid}", json=update)
    assert response.status_code == 200
    assert response.json()["price"] == 500


def test_update_product_not_found(client):
    response = client.put("/products/999", json={"price": 1000})
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"


def test_delete_product(client):
    product = {"name": "Mouse", "price": 20, "category": "Electronics"}
    create_resp = client.post("/products/", json=product)
    pid = create_resp.json()["id"]

    response = client.delete(f"/products/{pid}")
    assert response.status_code == 200

    # Now product should be gone
    response2 = client.get(f"/products/{pid}")
    assert response2.status_code == 404


def test_delete_product_not_found(client):
    response = client.delete("/products/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Product not found"