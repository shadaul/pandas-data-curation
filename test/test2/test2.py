import pandas as pd

# raw_response = {
#     "status": "success",
#     "meta": {"timestamp": "2026-04-09T10:00:00"},
#     "data": {
#         "batch_id": "REQ_9921",
#         "transactions": [
#             {"tx_id": 1, "user": {"id": 101, "name": "Ivan"}, "amount": 250.0},
#             {"tx_id": 2, "user": {"id": 102}, "amount": 15.5},  # У юзера нет имени
#             {"tx_id": 3, "user": {"id": 103, "name": "Anna"}, "amount": None} # Ошибка в сумме (None/Null)
#         ]
#     }
# }

# df = pd.json_normalize(raw_response['data'],['transactions'])
# df["user.name"] = df["user.name"].fillna("unknown")
# df['amount'] = df['amount'].fillna(0)
# print(df)


# purchases = [
#     {"item": "Laptop", "category": "Electronics", "price": 1200},
#     {"item": "Mouse", "category": "Electronics", "price": 50},
#     {"item": "Desk", "category": "Furniture", "price": 300},
#     {"item": "Chair", "category": "Furniture", "price": 150},
#     {"item": "Keyboard", "category": "Electronics", "price": 100}
# ]

# # Ожидаемый результат, который должен вывести print:
# # {'Electronics': 1350, 'Furniture': 450}

# total = {}

# for item in purchases:
#     category_name = item["category"]
#     item_price = item["price"]

#     total[category_name] = total.get(category_name, 0) + item_price

# print(total)

# sales_data = [
#     {"region": "North", "sales": 100, "costs": 50},
#     {"region": "South", "sales": 200, "costs": 80},
#     {"region": "North", "sales": 150, "costs": 70},
#     {"region": "South", "sales": 120, "costs": 60},
#     {"region": "West",  "sales": 300, "costs": 150}
# ]

# df = pd.DataFrame(sales_data)

# df = df.groupby('region')[['sales', 'costs']].sum()

# print(df)

# logs = [
#     "192.168.1.1", "10.0.0.2", "192.168.1.1", 
#     "10.0.0.3", "192.168.1.1", "10.0.0.2", 
#     "172.16.0.1", "10.0.0.2", "192.168.1.1"
# ]

# repeat = {}

# for item in  logs:
#     repeat[item] = repeat.get(item, 0) + 1

# print(repeat)

# session_id = "abacabad"

# unique = {}

# for item in session_id:
#     unique[item] = unique.get(item, 0 ) + 1

# for letter in session_id:
#     if unique[letter] == 1:
#         print(f"first unique letter: {letter}")
#         break

prices = [40, 20, 60, 10, 80, 50]
target = 100

seen_price = set()

for price in prices:
    diff = target - price

    if diff in seen_price:
        print(f"we found a pare: {diff} and {price}")
        break
    
    seen_price.add(price)
