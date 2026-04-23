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



def is_palindrome(word):
    return word == word[::-1] 

print(is_palindrome("radar")) # Должно вернуть True (радар = радар)
print(is_palindrome("level")) # Должно вернуть True (левел = левел)
print(is_palindrome("apple")) # Должно вернуть False (аппле != елппа)