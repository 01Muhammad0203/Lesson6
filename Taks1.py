# Ввод  N
N = int(input("Введите количество чисел N: "))

# Счетчик нулей
zero_count = 0


for _ in range(N):
    number = int(input())
    if number == 0:
        zeroCounter += 1

# Вывод результата
print(zeroCounter)
