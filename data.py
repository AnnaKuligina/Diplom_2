class TestData:

    success_register_response = {'status_code': 200, "success": True, "accessToken": "", "refreshToken": ""}
    double_register_response = {'status_code': 403, "success": False, "message": "User already exists"}
    missing_data_register_response = {
        'status_code': 403, "success": False,
        "message": "Email, password and name are required fields",
    }

    success_login_response = {
        'status_code': 200,
        "success": True,
        "accessToken": "",
        "refreshToken": "",
        "user": {
            "email": '',
            "name": ''
        }
    }

    wrong_login_response = {
        'status_code': 401,
        "success": False,
        "message": "email or password are incorrect"
    }

    valid_ingredients = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
    invalid_ingredients = ["invalid"]

    valid_order = {
        "ingredients": valid_ingredients
    }

    invalid_order = {
        "ingredients": invalid_ingredients
    }

    empty_order = {
        "ingredients": []
    }

    success_order_response_without_auth = {
        "status_code": 200,
        "success": True,
        "name": "",
        "order": {
            "number": ''
        }
    }

    success_order_response_with_auth = {
        "status_code": 200,
        "success": True,
        "name": "Бессмертный бургер",
        "order": {
            "ingredients": [
                {
                    "_id": "61c0c5a71d1f82001bdaaa6f",
                    "name": "Мясо бессмертных моллюсков Protostomia",
                    "type": "main",
                    "proteins": 433,
                    "fat": 244,
                    "carbohydrates": 33,
                    "calories": 420,
                    "price": 1337,
                    "image": "https://code.s3.yandex.net/react/code/meat-02.png",
                    "image_mobile": "https://code.s3.yandex.net/react/code/meat-02-mobile.png",
                    "image_large": "https://code.s3.yandex.net/react/code/meat-02-large.png",
                    "__v": 0
                },
                {
                    "_id": "61c0c5a71d1f82001bdaaa6f",
                    "name": "Мясо бессмертных моллюсков Protostomia",
                    "type": "main",
                    "proteins": 433,
                    "fat": 244,
                    "carbohydrates": 33,
                    "calories": 420,
                    "price": 1337,
                    "image": "https://code.s3.yandex.net/react/code/meat-02.png",
                    "image_mobile": "https://code.s3.yandex.net/react/code/meat-02-mobile.png",
                    "image_large": "https://code.s3.yandex.net/react/code/meat-02-large.png",
                    "__v": 0
                }
            ],
            "_id": "",
            "owner": {
                "name": "",
                "email": "",
                "createdAt": "",
                "updatedAt": ""
            },
            "status": "done",
            "name": "Бессмертный бургер",
            "createdAt": "",
            "updatedAt": "",
            "number": '',
            "price": ''
        }
    }

    order_no_ingredients_response = {
        "status_code": 400,
        "success": False,
        "message": "Ingredient ids must be provided"
    }

    order_invalid_ingredients_response = {
        "status_code": 500
    }