# Ввод  A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# первое четное число в отрезке A, B
if A % 2 != 0:
    A += 1

# Вывод всех четных чисел от A до B 
even_numbers = []
for number in range(A, B + 1, 2):
    even_numbers.append(str(number))

print(" ".join(even_numbers))
