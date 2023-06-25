from math import sqrt

def complex_operation(a, b):
    result = sqrt(a ** 2 + b ** 2) * (a + b) / (a * b)
    return result

def complex_function(n):
    total = 0
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                for k in range(n):
                    if j % 2 == 0:
                        for l in range(n):
                            if k % 2 == 0:
                                for m in range(n):
                                    if l % 2 == 0:
                                        value = complex_operation(i, j) + complex_operation(k, l) - complex_operation(m, n)
                                        total += value ** 2
    return total

# Пример вызова функции
result = complex_function(5)
print(result)
