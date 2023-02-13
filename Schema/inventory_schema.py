def inventory_serializer(inventory) -> dict:
    return {
        "id": str(inventory["_id"]),
        "item": inventory["item"],
        "price": inventory["price"],
        "qty": inventory["qty"]
    }


def inventories_serializer(inventories) -> list:
    return [inventory_serializer(inventory) for inventory in inventories]
