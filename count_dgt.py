num = input("Введите число: ")
counts = [0] * 10
for digit in num:
    counts[int(digit)] += 1
print("\nЧастота каждой цифры:")
for index in range(10):
    print(f"Цифра {index} встречается {counts[index]} раз(а)")