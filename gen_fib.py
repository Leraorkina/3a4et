class Fibonacci:
    def __init__(self, count_limit):
        self.count_limit = count_limit

    def __iter__(self):
        first = 0
        second = 1
        generated = 0
        while generated < self.count_limit:
            yield first
            first, second = second, first + second
            generated += 1

# Пример
count = int(input("Сколько чисел Фибоначчи нужно: "))
fib_sequence = Fibonacci(count)

print("Первый цикл:")
for number in fib_sequence:
    print(number)