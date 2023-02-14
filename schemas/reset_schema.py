def reset_serialize(reset) -> dict:
    return{
        "customer_id": reset["customerId"],
        "token": reset["token"],
        "status": reset["status"],
        "expiration": reset["expiration"],
        "request_time": reset["request_time"]
    }


def resets_serialize(resets) -> list:
    return [reset_serialize(reset) for reset in resets]
