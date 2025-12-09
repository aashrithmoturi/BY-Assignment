from unittest.mock import MagicMock
from app import crud
from app.schemas import ProductCreate, ProductUpdate
from app import models


def test_get_all_products():
    db = MagicMock()
    fake_products = [models.Product(id=1, name="A", price=10, category="X")]
    db.query().all.return_value = fake_products

    result = crud.get_all_products(db)

    assert result == fake_products


def test_get_product_by_id():
    db = MagicMock()
    fake_product = models.Product(id=1, name="A", price=10, category="X")
    db.query().filter().first.return_value = fake_product

    result = crud.get_product_by_id(1, db)

    assert result == fake_product


def test_create_product():
    db = MagicMock()
    product_data = ProductCreate(name="A", price=10, category="X")
    db.refresh.side_effect = lambda obj: None  
    
    result = crud.create_product(product_data, db)

    assert result.name == "A"
    assert result.price == 10
    assert result.category == "X"


def test_update_product():
    db = MagicMock()
    original = models.Product(id=1, name="A", price=10, category="X")
    db.query().filter().first.return_value = original
    update_data = ProductUpdate(name="Updated")
   
    result = crud.update_product(1, update_data, db)

    assert result.name == "Updated"
    assert result.price == 10
    assert result.category == "X"


def test_update_product_not_found():
    db = MagicMock()
    db.query().filter().first.return_value = None

    result = crud.update_product(1, ProductUpdate(name="X"), db)

    assert result is None


def test_delete_product():
    db = MagicMock()
    fake_product = models.Product(id=1, name="A", price=10, category="X")
    db.query().filter().first.return_value = fake_product

    result = crud.delete_product(1, db)

    assert result == fake_product


def test_delete_product_not_found():
    db = MagicMock()
    db.query().filter().first.return_value = None

    result = crud.delete_product(1, db)

    assert result is None
