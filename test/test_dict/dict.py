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

# clicks = [
#     {"user_id": 1, "page": "Главная"},
#     {"user_id": 2, "page": "Каталог"},
#     {"user_id": 1, "page": "Корзина"},
#     {"user_id": 3, "page": "Главная"},
#     {"user_id": 2, "page": "Оплата"}
# ]

# def group_clicks(logs):
#     my_dict = {}
#     for item in logs:
#         id = item["user_id"]
#         page = item["page"]

#         if id not in my_dict:
#             my_dict[id] = [page]
#         else:
#             my_dict[id].append(page)
#     return my_dict


# print(group_clicks(clicks))



# def is_anagram(word1, word2):
#     return sorted(word1) == sorted(word2)
# from collections import Counter

# def is_anagram(word1, word2):
#     return Counter(word1) == Counter(word2)

    
# # def is_anagram(word1, word2):
# #     if len(word1) != len(word2):
# #         return False
# #     dict1 = {}
# #     dict2 = {}
# #     for item in word1:
# #         dict1[item] = dict1.get(item, 0) + 1
# #     for i in word2:
# #         dict2[i] = dict2.get(i, 0) + 1
# #     return dict1 == dict2

# print(is_anagram("listen", "silent")) # Должно вернуть True
# print(is_anagram("triangle", "integral")) # Должно вернуть True
# print(is_anagram("apple", "papel")) # Должно вернуть True
# print(is_anagram("hello", "holla")) # Должно вернуть False


# nums1 = [2, 7, 11, 15]
# target1 = 9
# # Ожидаемый результат: [0, 1] (Потому что nums1[0] + nums1[1] = 2 + 7 = 9)

# nums2 = [3, 2, 4]
# target2 = 6
# # Ожидаемый результат: [1, 2] (Потому что 2 + 4 = 6)

# nums3 = [3, 3]
# target3 = 6
# # Ожидаемый результат: [0, 1]

# def two_sum(nums1):
#     seen_numbers = {}
#     for index, num in enumerate(nums1):
#         diff = target1 - num
#         if diff in seen_numbers:
#             return [seen_numbers[diff], index]
#         else:
#             seen_numbers[num] = index

# print(two_sum(nums1))


# def compress_string(text):
#     if not text:
#         return ""
#     count = 1
#     current_char = text[0]
#     result = ''
#     for letter in text[1:]:
#         if letter == current_char:
#             count += 1
#         else:
#             result = result + letter + str(count)
#             current_char = letter
#             count = 1

#     result = result + letter + str(count)
#     return result

# print(compress_string("AAABBC"))   # Должно вернуть "A3B2C1"
# print(compress_string("XYZ"))      # Должно вернуть "X1Y1Z1"
# print(compress_string("AABBAA"))   # Должно вернуть "A2B2A2" (Внимательно: 'A' тут встречается дважды, но мы не суммируем их все вместе, мы считаем только те, что идут ПОДРЯД)

# from collections import Counter
# logs1 = [101, 101, 101, 202, 202, 303]
# k1 = 2
# # Ожидаемый результат: [101, 202] (Потому что 101 купили 3 раза, 202 купили 2 раза. Это топ-2).

# logs2 = [777]
# k2 = 1
# # Ожидаемый результат: [777]

# def top_k_products(logs, k):
#     top_items = Counter(logs).most_common(k)

#     result = []
#     for item in top_items:
#         result.append(item[0])

#     return result

# print(top_k_products(logs1, 2))



# def is_valid(s):
#     stack = []
#     mapping = {")": "(", "]": "[", "}": "{"}
#     for item in s:
#         if item not in mapping:
#             stack.append(item)

#         elif item in mapping:

#             if len(stack) == 0:
#                 return False
            
#             top_element = stack.pop()
#             if mapping[item] != top_element:
#                 return False
            
#     return len(stack) == 0
            
# print(is_valid("()"))      # True (Всё четко)
# print(is_valid("()[]{}"))  # True (Открыли-закрыли, всё по очереди)
# print(is_valid("(]"))      # False (Открыли круглую, а закрыли квадратной — ошибка!)
# print(is_valid("([)]"))    # False (Порядок нарушен: попытались закрыть круглую до того, как закрыли квадратную)
# print(is_valid("{[]}"))    # True (Открыли фигурную, внутри открыли и закрыли квадратную, потом закрыли фигурную — идеально)


# print(longest_unique_substring("abcabcbb")) 
# # Должно вернуть 3. (Самая длинная уникальная часть — "abc", ее длина 3).

# print(longest_unique_substring("bbbbb"))    
# # Должно вернуть 1. (Уникальная часть только одна — "b").


# Должно вернуть 3. (Подстрока "wke", длина 3. Обрати внимание, "pw" — это 2, а потом идет 'w' и всё ломает).

# def longest_unique_substring(s):
#     left = 0
#     max_length = 0
#     seen_chars = {}
#     for right, char in enumerate(s):
#         if char in seen_chars:
#             left = max(left, seen_chars[char] + 1)
#             seen_chars[char] = right
#             current_lenght = right - left + 1

#             max_length = max(max_length, current_lenght)
#     return max_length

# print(longest_unique_substring("pwwkew"))   



# def is_palindrome(word):
#     return word == word[::-1] 

# print(is_palindrome("radar")) # Должно вернуть True (радар = радар)
# print(is_palindrome("level")) # Должно вернуть True (левел = левел)
# print(is_palindrome("apple")) # Должно вернуть False (аппле != елппа)



# def find_missing(nums):
#     n = len(nums)
#     ideal_num = n * (n + 1) // 2

#     return ideal_num - sum(nums)


# print(find_missing([3, 0, 1])) 
# # Должно вернуть 2. (Потому что массив длиной 3, значит числа должны быть 0, 1, 2, 3. Двойки не хватает).

# print(find_missing([0, 1, 2, 4, 5])) 
# # Должно вернуть 3.

# print(find_missing([1, 0])) 
# # Должно вернуть 2. (Массив длиной 2, числа должны быть 0, 1, 2. Двойки нет).




# def find_single(nums):
#     ideal_sum = sum(set(nums)) * 2
#     sec_sum = sum(nums)
#     total = ideal_sum - sec_sum
#     return total

# print(find_single([2, 2, 1])) 
# # Должно вернуть 1 (Двойки — пара, единица — без пары).

# print(find_single([4, 1, 2, 1, 2])) 
# # Должно вернуть 4 (Единицы и двойки — пары, четверка — одна).



# def aggregate_transactions(logs):
#     result = {}
#     for item in logs:
#         user = item["user_id"]
#         money = item["amount"]
#         result[user] = result.get(user, 0) + money
#     return result

# raw_logs = [
#     {"user_id": 101, "amount": 1000},
#     {"user_id": 102, "amount": 500},
#     {"user_id": 101, "amount": 300},
#     {"user_id": 103, "amount": 2000},
#     {"user_id": 102, "amount": 100}
# ]

# print(aggregate_transactions(raw_logs))
# # Должно вернуть: {101: 1300, 102: 600, 103: 2000}



# def find_pair(nums, target):
#     memory = {}
#     for index, num in enumerate(nums):
#         diff = target - num
#         if diff in memory:
#             return [memory[diff], index]
#         memory[num] = index



# # Транзакции: 2000, 7000, 11000, 15000. Ищем сумму 9000.
# print(find_pair([2000, 7000, 11000, 15000], 9000)) 
# # Должно вернуть: [0, 1] (т.к. 2000 + 7000 = 9000, а их индексы 0 и 1)

# print(find_pair([300, 200, 400], 600)) 
# # Должно вернуть: [1, 2] (т.к. 200 + 400 = 600)




# def top_frequent(nums, k):
#     counts = {}
#     for num in nums:
#         if num not in counts:
#             counts[num] = counts.get(num, 0) + 1
#     sorted_keys = sorted(counts, key=counts.get, reverse=True)
#     return sorted_keys[:k]

# # Ищем топ-2 самые частые суммы
# print(top_frequent([100, 100, 100, 500, 500, 200], 2)) 
# # Должно вернуть: [100, 500] 
# # (потому что 100 встречается 3 раза, 500 — 2 раза, а 200 — всего 1 раз).

# print(top_frequent([50, 50, 10, 10, 10, 30], 1)) 
# # Должно вернуть: [10] (так как десятка встречается чаще всех).

# def clean_logs(logs):
#     correct = []
#     for item in logs:
        
#         if item >= 0:
#             correct.append(item)
        
#     return correct
    
# print(clean_logs([1500, -200, 5000, -10, 300]))

# raw_logs = [
#     {"player_id": 101, "playtime": 150, "status": "active"},
#     {"player_id": 102, "playtime": -20, "status": "active"},  # Баг: отрицательное время
#     {"player_id": 103, "playtime": 300, "status": ""},        # Баг: пустой статус
#     {"player_id": 104, "playtime": 45,  "status": "banned"},
#     {"player_id": 105, "playtime": 0,   "status": "active"}   # Нулевое время тоже убираем
# ]


# def clean_game_logs(logs):
#     clean = []
#     for item in logs:
#         time = item['playtime']
#         status = item['status']
#         if time > 0 and status != "":
#             clean.append(item)
#     return clean

# print(clean_game_logs(raw_logs))

# import pandas as pd

# # Сырые данные покупок во внутриигровом магазине
# data = {
#     'player_id': [101, 102, 103, 104, 105],
#     'item': ['Sword', 'Shield', 'Axe', 'Potion', 'Bow'],
#     'coins_spent': [250, -50, 300, 0, 150],  # Баги: отрицательные и нулевые траты
#     'transaction_status': ['success', 'success', 'failed', 'success', 'error']
# }

# df = pd.DataFrame(data)

# clean_df = df[(df['coins_spent'] > 0) & (df['transaction_status'] == 'success')]
# print("Исходный DataFrame:\n", clean_df, "\n")


# import pandas as pd

# data = {
#     'player_id': [1, 2, 3, 4, 5],
#     'item_used': ['Health Potion', 'Aimbot', 'Sword', 'Wallhack', 'Shield']
# }
# df = pd.DataFrame(data)

# # Список запрещенных предметов
# banned_items = ['Aimbot', 'Wallhack']

# cheaters_df = df[df['item_used'].isin(banned_items)]
# print(cheaters_df)

# import pandas as pd
# import numpy as np  # Импортируем библиотеку NumPy, чтобы использовать np.nan (пустоту)

# # Сырые данные с "дырами"
# data = {
#     'player_id': [101, 102, 103, 104, 105],
#     'experience': [1500, np.nan, 3200, np.nan, 4100],  # np.nan - это системная пустота
#     'status': ['active', 'banned', np.nan, 'active', 'active']
# }
# df = pd.DataFrame(data)

# df['experience'] = df['experience'].fillna(0)
# clean_df = df.dropna(subset=['status'])

# print("Сырые данные:\n", clean_df, "\n")

# import pandas as pd

# data = {
#     'player_id': [1, 2, 3, 4, 5, 6],
#     'item_category': ['Weapon', 'Armor', 'Weapon', 'Potion', 'Armor', 'Weapon'],
#     'price': [150, 300, 200, 50, 400, 100]
# }
# df = pd.DataFrame(data)


# revenue_df = df.groupby('item_category')['price'].sum()

# # Выводим результат
# print("Выручка по категориям:\n", revenue_df)


import pandas as pd

# Таблица 1: Профили игроков
users_data = {
    'player_id': [101, 102, 103],
    'nickname': ['ShadowNinja', 'GamerPro', 'NoobMaster']
}
users_df = pd.DataFrame(users_data)

# Таблица 2: Транзакции
purchases_data = {
    'transaction_id': [991, 992, 993, 994],
    'player_id': [101, 103, 101, 102],
    'amount_spent': [500, 150, 1000, 300]
}
purchases_df = pd.DataFrame(purchases_data)

# Твоя задача: объединить users_df и purchases_df
full_data = pd.merge(users_df, purchases_df, on='player_id', how='inner')

print(full_data)