# Ввод  X
X = int(input("Введите натуральное число X: "))

# Счетчик натуральных делителей
divisor_count = 0

# Подсчет 
for i in range(1, X + 1):
    if X % i == 0:
        divisor_count += 1


print(divisor_count)
