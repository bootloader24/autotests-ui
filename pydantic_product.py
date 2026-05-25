from pydantic import BaseModel, Field


class Market(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Цена должна быть больше 0")  # поле с дополнительными настройками
    tags: list[str] = []
    market: Market

# Инициализация модели
product_data = {
    "name": "Phone",
    "price": 499.99,
    "tags": ["electronics", "smartphone"],
    "market": {  # можно использовать вложенные модели
        "id": 1,
        "name": "Amazon"
    }
}

product = Product(**product_data)
print('Product: ', product)
print('Product market name: ', product.market.name)

# Альтернативная инициализация модели
new_product = Product(
    name="Phone",
    price=499.99,
    tags=["electronics", "smartphone"],
    market=Market(id=1, name="Amazon")
)

print('New product: ', new_product)
