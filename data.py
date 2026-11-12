order_data = {
    "firstName": "Chachka",
    "lastName": "Pipsov",
    "address": "Lenina street, 512",
    "metroStation": "4",
    "phone": "88005553535",
    "rentTime": 2,
    "deliveryDate": "2026-11-22",
    "comment": "Thank you for your service",
    "color": [
        "BLACK"
    ]
}

def create_order_data(color):
    test_data = order_data.copy()
    
    test_data['color'] = color
    
    if color is None:
        del test_data['color']

    return test_data


