# transactions = [
#     {"user_id": 101, "amount": 50.0, "status": "success"},
#     {"user_id": 102, "amount": 120.0, "status": "success"},
#     {"user_id": 101, "amount": 75.0, "status": "success"},
#     {"user_id": 103, "amount": 40.0, "status": "failed"}, # Ошибочные не считаем!
#     {"user_id": 102, "amount": 10.0, "status": "success"},
# ]

# def get_top_spenders(logs, n):
#     dicti = {}
#     for item in logs:
#         if item["status"] == "success":

#             user = item["user_id"]
#             money = item["amount"]

#             dicti[user] = dicti.get(user, 0) + money
#     sorted_dict = sorted(dicti.items(), key=lambda x: x[1], reverse=True)
#     top_ids = [x[0] for x in sorted_dict[:n]]

#     return top_ids

# print(get_top_spenders(transactions, 2))


# sessions = [
#     {"user_id": 1, "duration": 45},
#     {"user_id": 2, "duration": 12},
#     {"user_id": 1, "duration": 80},
#     {"user_id": 3, "duration": 25},
#     {"user_id": 2, "duration": 30}
# ]

# def get_max_session(logs):
#     my_dict = {}
#     for item in logs:
#         user = item["user_id"]
#         time = item["duration"]
#         if user not in my_dict:
#             my_dict[user] = time
#         else:
#             if time > my_dict[user]:
#                 my_dict[user] = time
#     return my_dict

# print(get_max_session(sessions))

# server_logs = [
#     {"status_code": 200, "message": "OK"},
#     {"status_code": 404, "message": "Not Found"},
#     {"status_code": 500, "message": "Internal Error"},
#     {"status_code": 200, "message": "OK"},
#     {"status_code": 404, "message": "Not Found"},
#     {"status_code": 403, "message": "Forbidden"},
#     {"status_code": 404, "message": "Not Found"}
# ]

# def count_errors(logs):
#     my_dict = {}
#     for item in logs:
#         status = item["status_code"]
#         mess = item["message"]
#         if status != 200:
#             my_dict[status] = my_dict.get(status, 0) + 1

#     return my_dict

# print(count_errors(server_logs))

# users = [
#     {"id": 1, "name": "Али"},
#     {"id": 2, "name": "Борис"},
#     {"id": 3, "name": "Витя"}
# ]

# purchases = [
#     {"user_id": 1, "amount": 500},
#     {"user_id": 2, "amount": 200},
#     {"user_id": 1, "amount": 100},
#     # Обрати внимание, Витя ничего не купил!
# ]

# def get_total_spent(users, purchases):
#     my_dict = {}
    
#     final_dict = {}


#     for person in users:
#         user_id = person["id"]
#         name = person["name"]
#         my_dict[user_id] = name

#         final_dict[name] = 0
#         print(my_dict)

#     for item in purchases:
#         u_id = item["user_id"]
#         money = item["amount"]

#         real_name = my_dict[u_id]

#         final_dict[real_name] = final_dict.get(real_name) + money

#     return final_dict

# print(get_total_spent(users, purchases))

clicks = [
    {"user_id": 1, "page": "Главная"},
    {"user_id": 2, "page": "Каталог"},
    {"user_id": 1, "page": "Корзина"},
    {"user_id": 3, "page": "Главная"},
    {"user_id": 2, "page": "Оплата"}
]

def group_clicks(logs):
    my_dict = {}
    for item in logs:
        id = item["user_id"]
        page = item["page"]

        if id not in my_dict:
            my_dict[id] = [page]
        else:
            my_dict[id].append(page)
    return my_dict


print(group_clicks(clicks))