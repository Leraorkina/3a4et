def fib_gen(number):
    num1 = 0
    num2 = 1
    for currentIndex in range(number):
        yield num1
        num1, num2 = num2, num1 + num2

for currentNum in fib_gen(6):
    print(currentNum)