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


sessions = [
    {"user_id": 1, "duration": 45},
    {"user_id": 2, "duration": 12},
    {"user_id": 1, "duration": 80},
    {"user_id": 3, "duration": 25},
    {"user_id": 2, "duration": 30}
]

def get_max_session(logs):
    my_dict = {}
    for item in logs:
        user = item["user_id"]
        time = item["duration"]
        my_dict[user] = max(time, my_dict.get(user, 0))
    return my_dict

print(get_max_session(sessions))