class User:
    def __init__(self, user_id, first_name, last_name, phone_number, password):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.password = password

        # relationships
        self.orders = []
        self.reviews = []
        self.carts = []   


class Order:
    def __init__(self, order_id, created_at, status, user):
        self.order_id = order_id
        self.created_at = created_at
        self.status = status
        self.user = user      # FK → User

        # relationships
        self.items = []
        self.payment = None


class Payment:
    def __init__(self, payment_id, amount, total_amount, method, status, order, done_at):
        self.payment_id = payment_id
        self.amount = amount
        self.total_amount = total_amount
        self.method = method
        self.status = status
        self.order = order        # FK → Order
        self.done_at = done_at


class OrderItem:
    def __init__(self, orderitem_id, quantity, product, order):
        self.orderitem_id = orderitem_id
        self.quantity = quantity
        self.product = product    # FK → Product
        self.order = order        # FK → Order


class Product:
    def __init__(self, product_id, name, description, price, category):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category  # FK → Category

        # relationships
        self.order_items = []
        self.cart_items = []
        self.reviews = []


class Category:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

        # relationships
        self.products = []


class Review:
    def __init__(self, review_id, rating, is_approved, created_at, user, product):
        self.review_id = review_id
        self.rating = rating
        self.is_approved = is_approved
        self.created_at = created_at
        self.user = user          # FK → User
        self.product = product    # FK → Product


class Cart:
    def __init__(self, cart_id, created_at, updated_at, user):
        self.cart_id = cart_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.user = user          # FK → User

        # relationships
        self.items = []


class CartItem:
    def __init__(self, cartitem_id, quantity, product, cart):
        self.cartitem_id = cartitem_id
        self.quantity = quantity
        self.product = product    # FK → Product
        self.cart = cart          # FK → Cart
