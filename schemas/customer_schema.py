def customer_serializer(customer) -> dict:
    result = {
        "email": customer["_id"],
        "first_name": customer["first_name"],
        "last_name": customer["last_name"],
        "hashed_and_salted_password": customer["hashed_and_salted_password"],
        "email_verified": customer["email_verified"],
    }
    if customer["address"] is not None:
        result["address"] = {
            "country": customer["address"]["country"],
            "street1": customer["address"]["street1"],
            "street2": customer["address"]["street2"],
            "city": customer["address"]["city"],
            "state": customer["address"]["state"],
            "zip": customer["address"]["zip"]
        }
    if customer["shipping_address"] is not None:
        result["shipping_address"] = {
            "country": customer["shipping_address"]["country"],
            "street1": customer["shipping_address"]["street1"],
            "street2": customer["shipping_address"]["street2"],
            "city": customer["shipping_address"]["city"],
            "state": customer["shipping_address"]["state"],
            "zip": customer["shipping_address"]["zip"]
        }

    return result


def customers_serializer(customers) -> list:
    return [customer_serializer(customer) for customer in customers]