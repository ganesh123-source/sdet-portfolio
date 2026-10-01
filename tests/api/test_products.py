import requests 
import pytest

@pytest.mark.smoke
@pytest.mark.api
def test_get_all_products(api_base):
    """GET /products returns a list of products"""
    response = requests.get(f"{api_base}/products")
    assert response.status_code ==200
    products = response.json()["products"]
    assert isinstance(products,list)
    assert len(products)>0

@pytest.mark.smoke
@pytest.mark.api
def test_products_have_required_fields(api_base):
    """Every product must have id, title, price, category"""
    response = requests.get(f"{api_base}/products")
    assert response.status_code ==200

    products = response.json()["products"]
    req_fields = ["id","title","price","category"]

    for product in products:
        for field in req_fields:
            assert field in product, f"missing field: {field}\n id:{product.get('id')}"

@pytest.mark.regression
@pytest.mark.api
def test_create_product(api_base):
    """POST /products/add creates a product and returns 201"""
    payload = {
        "title": "SDET Test Product",
        "price": 49.99
    }
    response = requests.post(f"{api_base}/products/add", json= payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "SDET Test Product"
    assert "id" in data

@pytest.mark.regression
@pytest.mark.api
@pytest.mark.parametrize("product_id",[1,5,10],ids= ["product-1","product-5","product-10"])
def test_get_product_by_id(api_base,product_id):
    response = requests.get(f"{api_base}/products/{product_id}")
    assert response.status_code== 200
    assert "title" in response.json()
    assert "price" in response.json()
    