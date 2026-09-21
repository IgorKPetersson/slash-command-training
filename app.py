def calculate_total(price, quantity, customer_type):
    if quantity < 1:
        raise ValueError("quantity must be at least 1")

    if price <= 0:
        raise ValueError("price must be greater than 0")

    total = price * quantity

    if customer_type == "premium":
        return total * 0.90

    if customer_type == "vip":
        return total * 0.80

    return total
