data = [654, 42185, 619, 39910,
        809, 4915, 921, 5699,
        -535, 20835, 225, -8805,
        760, 13690, 113, 2691,
        163, -11635, 919, -61531,
        808, -1722, -58, -856,
        -860, -61046, 501, 34224,
        -74, -5540, -170, -12740,
        418, -21771, -965, 51528,
        -160, 12544, 60, -5936]

answers = []
for i, j, k, l in zip(range(0, len(data), 4), range(1, len(data), 4), range(2, len(data), 4), range(3, len(data), 4)):
    a = (data[l] * data[k] - data[j]) // (data[k] - data[i])
    b = data[j] - a * data[i]
    answers.append(a)
    answers.append(b)
for i, j in zip(range(0, len(answers), 2), range(1, len(answers), 2)):
    print(f"({answers[i]} {answers[j]})", end=' ')


# if abs(result - int(result)) >= 0.5:
#     if result > 0:
#         result = int(result) + 1
#     else:
#         result = int(result) - 1
# else:
#     result = int(result)
