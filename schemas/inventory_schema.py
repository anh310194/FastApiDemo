def inventory_serializer(inventory) -> dict:
    return {
        "id": str(inventory["_id"]),
        "item": inventory["item"],
        "price": inventory["price"],
        "qty": inventory["qty"],
        "size": {
            "height": inventory["size"]["height"],
            "length": inventory["size"]["length"],
            "width": inventory["size"]["width"]
        },
        "features": inventory["features"],
        "categories": inventory["categories"],
        "image": inventory["image"]
    }


def inventories_serializer(inventories) -> list:
    return [inventory_serializer(inventory) for inventory in inventories]
