from datetime import datetime


class User:
    def __init__(
        self,
        user_id: str,        # PK
        first_name: str,
        last_name: str,
        phone_number: str,
        password: str
    ):
        self.user_id: str = user_id  # PK
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.phone_number: str = phone_number
        self.password: str = password


class Order:
    def __init__(
        self,
        order_id: str,       # PK
        created_at: datetime,
        status: str,
        user_id: str         # FK → User.user_id
    ):
        self.order_id: str = order_id    # PK
        self.created_at: datetime = created_at
        self.status: str = status
        self.user_id: str = user_id      # FK


class Payment:
    def __init__(
        self,
        payment_id: str,     # PK
        amount: float,
        total_amount: float,
        method: str,
        status: str,
        order_id: str,       # FK → Order.order_id
        done_at: datetime
    ):
        self.payment_id: str = payment_id    # PK
        self.amount: float = amount
        self.total_amount: float = total_amount
        self.method: str = method
        self.status: str = status
        self.order_id: str = order_id        # FK
        self.done_at: datetime = done_at


class OrderItem:
    def __init__(
        self,
        orderitem_id: str,   # PK
        quantity: int,
        product_id: str,     # FK → Product.product_id
        order_id: str        # FK → Order.order_id
    ):
        self.orderitem_id: str = orderitem_id  # PK
        self.quantity: int = quantity
        self.product_id: str = product_id      # FK
        self.order_id: str = order_id          # FK


class Product:
    def __init__(
        self,
        product_id: str,     # PK
        name: str,
        description: str,
        price: float,
        category_id: str     # FK → Category.category_id
    ):
        self.product_id: str = product_id  # PK
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.category_id: str = category_id  # FK


class Category:
    def __init__(
        self,
        category_id: str,    # PK
        name: str,
        description: str
    ):
        self.category_id: str = category_id  # PK
        self.name: str = name
        self.description: str = description


class Review:
    def __init__(
        self,
        review_id: str,      # PK
        rating: int,
        is_approved: bool,
        created_at: datetime,
        user_id: str,        # FK → User.user_id
        product_id: str      # FK → Product.product_id
    ):
        self.review_id: str = review_id    # PK
        self.rating: int = rating
        self.is_approved: bool = is_approved
        self.created_at: datetime = created_at
        self.user_id: str = user_id        # FK
        self.product_id: str = product_id  # FK


class Cart:
    def __init__(
        self,
        cart_id: str,        # PK
        created_at: datetime,
        updated_at: datetime,
        user_id: str         # FK → User.user_id
    ):
        self.cart_id: str = cart_id  # PK
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at
        self.user_id: str = user_id  # FK


class CartItem:
    def __init__(
        self,
        cartitem_id: str,    # PK
        quantity: int,
        product_id: str,     # FK → Product.product_id
        cart_id: str         # FK → Cart.cart_id
    ):
        self.cartitem_id: str = cartitem_id  # PK
        self.quantity: int = quantity
        self.product_id: str = product_id    # FK
        self.cart_id: str = cart_id          # FK
