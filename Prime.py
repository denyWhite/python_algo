"""
Модуль для работы с простыми числами
"""
import random
import math


def gcd(a, b):
    """НОД чисел a и b"""
    if b == 0:
        return a
    return gcd(b, a % b)


def multiply(a, b, m):
    """"Умножение a на b по модулю m"""
    if b == 1:
        return a
    if b % 2 == 0:
        t = multiply(a, b/2, m)
        return 2*t % m
    return (multiply(a, b-1, m) + a) % m


def powers(a, b, m):
    """"Возведение a в степень b по модулю m"""
    if b == 0:
        return 1
    if b % 2 == 0:
        t = powers(a, b/2, m)
        return multiply(t, t, m) % m
    return multiply(powers(a, b-1, m), a, m) % m


def ferma(n, cnt=100):
    """"Проверка на простоту тестом Ферма
        https://ru.wikipedia.org/wiki/Тест_Ферма
        Работает медленнее, чем перебор"""
    if n == 2:
        return True
    if n < 2:
        return False
    random.seed
    for _ in range(cnt):
        a = (random.randint(0, 2 ** 8) % (n - 2)) + 2
        if gcd(a, n) != 1 or powers(a, n-1, n) != 1:
            return False
    return True


def brute(n):
    """Проверка на простоту перебором"""
    if n < 2:
        return False
    for iCounter in range(2, int(n ** .5) + 1):
        if n % iCounter == 0:
            return False
    return True


def wilson(n):
    """Проверка на простоту по теореме Вилсона
        Работает медленно из-за необходимости вычисления факториала
        https://ru.wikipedia.org/wiki/Теорема_Вильсона"""
    if n < 2:
        return False
    return not (math.factorial(n - 1) + 1) % n


def wilson_generator(num_count, start=2, finish=0):
    """Генератор простых чисел, с помощью теоремы Вилсона
        num_count - количество сгенерированных простых чисел
        start - если указан этот параметр, простые числа будут больше этого числа
        finish - если указан этот параметр, простые числа будут не больше этого числа
        (даже если в итоге получилось меньше, чем num_count)
        """
    count = 0
    if start < 2:
        start = 2
    n = start
    fact = math.factorial(start - 1)
    while count < num_count:
        if finish != 0 and n > finish:
            break
        if not (fact + 1) % n:
            count += 1
            yield n
        fact *= n
        n += 1


if __name__ == '__main__':
    from Profiler import Profiler
    prflr = Profiler()
    """"
    # Пример проверки на простоту
    prflr.start()
    for num in range(1, 100):
        print(brute(num), ferma(num), wilson(num))        
    prflr.finish()
    """
    """
    # Пример генерации простых чисел
    prflr.start()
    print([i for i in wilson_generator(100)])
    prflr.finish()
    """
