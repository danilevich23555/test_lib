import requests
import json
# # Авторизация пользователя
# response = requests.post(
#     'http://127.0.0.1:8000/user/login',
#     json={ 'email': 'admindD@gmail.com',
#           'password': 'wishdD',})
#
#
# # Работа с корзиной
#
# # response = requests.get(
# #     'http://127.0.0.1:8000/basket',
# #     {'token': '099d17042802d4e5d3cd3e97a221f82c49511592'})
#
#
# url='http://127.0.0.1:8000/basket'
# json1={
#       "items": [
#           {
#               "id": 224,
#               "name": "товар1",
#               "quantity": 3,
#               "contact_id": 1
#           }
#       ]
#    }
# print(json.dumps(json1))
# print(json1)
# headers = {"Content-Type": "application/json", "Authorization": "Token 60e7daf91556195e794a9f460655fc5f6c3fc2ff"}
# #
# response = requests.put(url, data=json.dumps(json1), headers=headers)
#
#
# # ---------------------ORDER-----------------
# url='http://127.0.0.1:8000/order'
# json1={
#
#               "id": 1,
#               "contact": 1,
#
#    }
# print(json.dumps(json1))
# print(json1)
# headers = {"Content-Type": "application/json", "Authorization": "Token 60e7daf91556195e794a9f460655fc5f6c3fc2ff"}
# #
# response = requests.post(url, data=json.dumps(json1), headers=headers)
#
# # -----------contact------------------------
# url='http://127.0.0.1:8000/user/contactsviewset'
# json1={
#               "city": "Москв",
#               "street": "Большая",
#               "house": "25",
#               "structure": "8",
#               "apartment": "681",
#               "phone": "79175066114"
#    }
# print(json.dumps(json1))
# print(json1)
# headers = {"Content-Type": "application/json", "Authorization": "Token 3f7e68b155f051e9614e0ecd04152564b2104b22"}
#
# response = requests.post(url, data=json.dumps(json1), headers=headers)


# --------------DELETE CONTACT--------------------------
# url='http://127.0.0.1:8000/user/contactsviewset/6'
# json1={
#     "items": str("1")
#
#    }
# print(json.dumps(json1))
# print(json1)
# headers = {"Content-Type": "application/json", "Authorization": "Token ef08d16260be0c534ee227aac456f3ce9866ce2b"}
#
# response = requests.delete(url, headers=headers)
# --------------get CONTACT--------------------------
# url='http://127.0.0.1:8000/user/contactsviewset/4'
#
# headers = {"Content-Type": "application/json", "Authorization": "Token ef08d16260be0c534ee227aac456f3ce9866ce2b"}
#
# response = requests.get(url, headers=headers)
# print(response.json())

# url = 'http://127.0.0.1:8000/user/contactsviewset'
# #
# json1 = {
#     "city": "Бишкек",
#     "street": "Большая",
#     "house": "25",
#     "structure": "8",
#     "apartment": "681",
#     "phone": "79175066114"
# }
# print(json.dumps(json1))
# print(json1)
# headers = {"Content-Type": "application/json", "Authorization": "Token 783551d0caea601689074f54ffa53e70dc3a7769"}
#
# response = requests.post(url, data=json.dumps(json1), headers=headers)
#
#
# # response = requests.get(
# #     'http://127.0.0.1:8000/basket',
# #     {'token': 'a5424f90317d1fc7a00ff3b9bade0bec05c702bc'})
#
#
# #Регистрация пользователя
response = requests.post(
    'http://127.0.0.1:8000/user/register',
    json={'first_name': 'Данила', 'last_name': 'Долгов', 'email': 'matushinoleg24d4D5@yandex.ru',
          'password': 'wishoting'})
#
#
# response = requests.post(
#     'http://127.0.0.1:8000/partner/update'
# )
#
# # response = requests.get(
# #     'http://127.0.0.1:8000/categories'
# # )
