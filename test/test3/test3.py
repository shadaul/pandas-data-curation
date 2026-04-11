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

unique_ids = set(promo_ids_3)

target = 1
while target in unique_ids:
   target += 1

print(target)