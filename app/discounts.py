def apply_discount(price, discount_percentage):
    if price <= 0:
        raise ValueError("El precio debe ser mayor que 0")

    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount

    return final_price
