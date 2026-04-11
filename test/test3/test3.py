# Формат: [начало_интервала, конец_интервала]
delivery_slots = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Ожидаемый результат: [[1, 6], [8, 10], [15, 18]]
# (Интервалы [1, 3] и [2, 6] слились в [1, 6], остальные остались без изменений)


delivery_slots.sort()
merged = []

for slot in delivery_slots:
    if not merged:
        merged.append(slot)

    else:
        last_merged = merged[-1]
        

        if slot[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], slot[1])

        else:
            merged.append(slot)

print(merged)