# def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    # print(int(((sum([item ** 2 for item in [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]])) ** 0.5) / 2))

    # return int(((sum([item ** 2 for item in [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]])) ** 0.5) / 2)

def predict_age(*ages):
    return sum(a*a for a in ages)**.5//2


predict_age(65, 60, 75, 55, 60, 63, 64, 45)


# Составьте список возрастов, в которых умер каждый из ваших прадедов.
# Умножьте каждое число само по себе.
# Сложите их все вместе.
# Извлеките квадратный корень из результата.
# Разделите на два.

# Примечание: результат должен быть округлен в меньшую сторону до ближайшего целого числа.