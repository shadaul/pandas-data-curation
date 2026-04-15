# # Формат: [начало_интервала, конец_интервала]
# delivery_slots = [[1, 3], [2, 6], [8, 10], [15, 18]]

# # Ожидаемый результат: [[1, 6], [8, 10], [15, 18]]
# # (Интервалы [1, 3] и [2, 6] слились в [1, 6], остальные остались без изменений)


# delivery_slots.sort()
# merged = []

# for slot in delivery_slots:
#     if not merged:
#         merged.append(slot)

#     else:
#         last_merged = merged[-1]
        

#         if slot[0] <= last_merged[1]:
#             last_merged[1] = max(last_merged[1], slot[1])

#         else:
#             merged.append(slot)

# print(merged)

# Пример 1:
promo_ids_1 = [1, 3, 6, 4, 1, 2]
# Твой код должен вернуть: 5 (потому что 1, 2, 3, 4 есть, а 5 пропущена)

# Пример 2:
promo_ids_2 = [1, 2, 3]
# Твой код должен вернуть: 4 (тут пропусков нет, значит берем следующее число)

# Пример 3: (Коварный тест Codility)
promo_ids_3 = [-1, -3]
# Твой код должен вернуть: 1 (потому что 1 — это самое маленькое положительное число, а в списке его нет)

# unique_ids = set(promo_ids_3)

# target = 1
# while target in unique_ids:
#    target += 1

# print(target)


X = 5 # Нам нужны товары 1, 2, 3, 4, 5
# Массив A: индекс — это секунда, значение — это ID товара, который приехал
A = [1, 3, 1, 4, 2, 3, 5, 4]

# Ожидаемый ответ: 6
# (Именно на 6-й секунде приезжает товар №5, и у нас есть полный комплект 1,2,3,4,5)

# def get_ready_time(X, A):
#     collected = set()
    
#     for second, item in enumerate(A):
#         collected.add(item)  
        
#         if len(collected) == X:  
#             return second        
            
#     return -1

# answer = get_ready_time(X, A)
# print(f"Все товары собраны на секунде: {answer}")

# def rotate_carousel(A, K):
#     if len(A) == 0:
#         return A
    
#     K = K % len(A)

#     return A[-K:] + A[:-K]

# A = [3, 8, 9, 7, 6]
# K = 3
# b = rotate_carousel(A, K)
# print(b)

# def find_unpaired(A):
#     pairs = set()
#     for item in A:
#         if item not in pairs:
#             pairs.add(item)
#         else:
#             pairs.remove(item)
#     return pairs.pop()

# A = [9, 3, 9, 3, 9, 7, 9]
# print("Потерянный ботинок:", find_unpaired(A))

# A = [3, 1, 2, 4, 3]

# def find_min_difference(A):
#     total_weight = sum(A)
#     left_weight = 0
#     right_weight = total_weight
#     min_diff = float('inf')
#     for box in A[:-1]:
#         left_weight += box
#         right_weight -= box
#         current_diff = abs(left_weight - right_weight)
#         if current_diff < min_diff:
#             min_diff = current_diff
#     return min_diff

# b = find_min_difference(A)
# print(b)


# A = [4, 1, 3, 2]

# def is_ok(A):
#     collection = set(A)
#     if len(collection) != len(A):
#         return False
#     if max(collection) != len(A):
#         return False
#     return True

# Пример 1: Идеальная конфигурация
S = "{[()()]}"
# Результат: True (Все открытые скобки закрыты в правильном порядке)

# Пример 2: Сбой в системе
S = "([)()]"
# Результат: False (Круглая скобка открылась, но внутри нее попыталась закрыться квадратная - это ошибка синтаксиса)

# def is_valid_config(S):
#     stack = []
#     matching_brackets = {')': '(', ']': '[', '}': '{'}
#     for item in S:
#         if item in "{[(":
#             stack.append(item)

#         elif item in matching_brackets:
            
        
#             if len(stack) == 0:
#                 return False

#             last_open = stack.pop()
#             if matching_brackets[item] != last_open:
#                 return False
#     return len(stack) == 0

# A = [-3, 1, 2, -2, 5, 6]

# def find_max_product(A):
#     A.sort()
#     option1 = A[-1] * A[-2] * A[-3]
#     option2 = A[0] * A[1] * A[-1]
#     return max(option1, option2)

# b = find_max_product(A)
# print(b)

A = [9, 3, 9, 3, 9, 7, 9]

# Как это выглядит:
# Индексы 0 и 2: пара девяток (9, 9)
# Индексы 1 и 3: пара троек (3, 3)
# Индексы 4 и 6: пара девяток (9, 9)
# Индекс 5: одинокая семерка (7). Ожидаемый результат: 7

# def find_unpaired(A):
#     count = {}
#     for num in A:
#         count[num] = count.get(num, 0) + 1
#     return count

# b = find_unpaired(A)
# print(b)


# def find_unpaired(A):
#     result = 0
#     for num in A:
#         result ^=num
#     return result

# b = find_unpaired(A)
# print(b)

A = [23171, 21011, 21123, 21366, 21013, 21367]

def get_max_profit(A):
    min_price = float('inf')
    max_profit = 0
    for price in A:
        if price < min_price:
            min_price = price
        current_profit = price - min_price
        if current_profit > max_profit:
            max_profit = current_profit

    return max_profit

b= get_max_profit(A)
print(b) 