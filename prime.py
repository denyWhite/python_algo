"""
Некотроые алгебраические алгоритмы, свзянные с простыми числами
"""
import math
import random


def gcd(a, b):
    """НОД чисел a и b
        :return: int
        """
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    """НОК чисел a и b
        :return: int
        """
    return math.fabs(a * b) // gcd(a, b)


def multiply_m(a, b, m):
    """Умножение a на b по модулю m
        a*b % m
        :return: int
        Примечание:
        Это если бы Пайтон не поддерживал длинную арифметику,
        то можно было бы считать примерно так
         if b == 1:
            return a
         if b % 2 == 0:
            t = multiply_m(a, b / 2, m)
            return 2 * t % m
         return (multiply_m(a, b - 1, m) + a) % m
        """
    return a * b % m


def powers_m(a, b, m):
    """Возведение a в степень b по модулю m
        a ** b % m
        :return: int
        """
    if b == 0:
        return 1
    if b % 2 == 0:
        t = powers_m(a, b / 2, m)
        return multiply_m(t, t, m) % m
    return multiply_m(powers_m(a, b - 1, m), a, m) % m


def fact_m(a, m):
    """Факториал a по модулю m
            a! % m
            :return: int
            """
    if 0 <= a <= 2:
        return a % m
    else:
        res = 1
        for i in range(2, a + 1):
            res = res * i % m
        return res


def is_prime_ferma(n, cnt=100, max_int=1000000):
    """"Проверка на простоту тестом Ферма
        https://ru.wikipedia.org/wiki/Тест_Ферма
        Работает медленнее, чем перебор
        :param n: Число для проверки
        :param cnt: Колличество проверок
        :param max_int: предел диапазона для генерации слуячайного числа
        :return: bool
        """
    if n == 2:
        return True
    if n < 2:
        return False
    for _ in range(cnt):
        a = (random.randint(1, max_int) % (n - 2)) + 2
        if gcd(a, n) != 1 or powers_m(a, n - 1, n) != 1:
            return False
    return True


def is_prime_brute(n):
    """Проверка на простоту перебором
        :param n: Число для проверки
        :return: bool
        """
    if n < 2:
        return False
    if n == 3:
        return True
    for iCounter in range(5, int(n ** .5) + 1, 2):
        if n % iCounter == 0:
            return False
    return True


def is_prime_brute2(n):
    """Проверка на простоту перебором
        Варинт 2 через WHILE
        Чуть медленнее, но не хранит range
        :param n: Число для проверки
        :return: bool
        """
    if n < 2:
        return False
    dl: int = 2
    while dl * dl < n:
        if n % dl == 0:
            return False
        if dl == 2:
            dl = 3
        else:
            dl += 2
            if dl > 7 and (dl % 3 == 0 or dl % 5 == 0 or dl % 7 == 0):
                dl += 2
    return True


def is_prime_willson(n):
    """Проверка на простоту по теореме Вилсона
        Работает медленно из-за необходимости вычисления факториала
        https://ru.wikipedia.org/wiki/Теорема_Вильсона
        :param n: Число для проверки
        :return: bool
        """
    if n < 2:
        return False
    # return not (math.factorial(n - 1) + 1) % n
    # вместо факториала, считаем факториал по модулю
    return not (fact_m(n - 1, n) + 1) % n


def prime_generator_willson(num_count, start=2, finish=0):
    """Генератор простых чисел, с помощью теоремы Вилсона
        :param num_count: - количество сгенерированных простых чисел
        :param start: если указан этот параметр, простые числа будут больше этого числа
        :param finish: - если указан этот параметр, простые числа будут не больше этого числа
        (даже если в итоге получилось меньше, чем num_count)
        Медленный генератор. Практиического значения не имеет
        Для генерации большого колличества простых чисел от 2 до n лучше использовать алгоритмы ниже
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


def prime_interval_habr(n):
    """
    Еще одна функция для генерации простых числе,
    работает намного быстрее, чем генератор по теореме Вислсона,
    однако не может быть генератором
    Взято с https://habr.com/post/122538/
    Работает быстрее примерно до n<3000, после этого лучше использовать решето Эратосфена
    :param n: Предел генерации
    :return: Список с простыми числами
    """
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def get_n_prime(n):
    """
    Модификация предыдущего алгоритма для получения n-го простого числа
    get_n_prime(1) - 2
    get_n_prime(7) - 17
    :param n: Порядковый номер простого числа
    :return: Просто число с данным порядковым номером
    """
    lst = [2]
    i = 3
    while len(lst) < n:
        if (i > 10) and (i % 10 == 5):
            i += 2
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 2
    return lst[-1]


def sieve_of_eatosthenes(n):
    """
    Реализация классического алгоритма Решето Эратосфена
    https://ru.wikipedia.org/wiki/Решето_Эратосфена
    :param n: Предел генерации
    :return: Список с простыми числами
    """
    a = list(range(n + 1))
    a[1] = 0
    lst = []
    i: int = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return lst


def factorization(n, as_dict=False):
    """
    Факторизация числа (разложение на простые множители)
    https://ru.wikipedia.org/wiki/Факторизация_целых_чисел
    :param n: число
    :param as_dict: Если истинно, вернуть словарем, где индекс - это множитель,
        а значение степень вхождения в разложение
    :return: список или словарь простых множителей
    """
    i: int = 2
    pfac = []
    while i * i <= n:
        while n % i == 0:
            pfac.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        pfac.append(n)
    if as_dict:
        dct = {}
        for num in pfac:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        return dct
    return pfac


def divider_count_bad(n):
    """
    Количество положительных делителей  числа перебором (жуть как медленно, так делать не надо)
    :param n: Число
    :return: Число, количество делителей
    """
    if n == 1:
        return 1
    cnt = 2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            cnt += 1
    return cnt


def divider_count(n):
    """
    Количество положительных делителей исходя из следущего факта:
    пусть n = r1^t1*r2^t2...rn^tn разложение числа n на простые множители,
    тогда число делителей числа n равно CNT = (t1+1)*(t2+1)*...*(tn+1)
    :param n: Число
    :return: Число, количество делителей
    """
    dct = factorization(n, True)
    cnt = 1
    for val in dct.values():
        cnt *= (val + 1)
    return cnt


def divider_sum(n):
    """
    Сумма всех делителей числа n
    :param n: Число
    :return: Сумма всех делителей
    """
    pw = factorization(n, True)
    sm = 1
    for num in pw:
        sm *= ((num ** (pw[num] + 1)) - 1) // (num - 1)
    return sm


def divider_sum_and_count(n):
    """
    Объединение предыдущих двух функция
    :param n: Число
    :return: кортеж (кол-во пол. делителей и сумма полож. делителей)
    """
    pw = factorization(n, True)
    sm: int = 1
    cnt = 1
    for num in pw:
        cnt *= (pw[num] + 1)
        sm *= ((num ** (pw[num] + 1)) - 1) // (num - 1)
    return sm, cnt


def euler(n):
    """
    Функция Эйлера
    https://ru.wikipedia.org/wiki/Функция_Эйлера
    :param n: Число
    :return: Число, функция Эйлера
    """
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount


if __name__ == '__main__':
    """
    from Profiler import Profiler
    prflr = Profiler()
    # Пример нахождения НОД и НОК
    print(gcd(45,27))
    print(lcm(45,27))



    # Умножения по модулю и возведения в степень по модулю
    prflr.start()
    print(powers_m(10, 999999, 3))
    prflr.finish()
    print((10 ** 999999) % 3)
    prflr.finish()



    # Пример проверки на простоту
    prflr.start()
    for num in range(30000, 30999):
        if not (is_prime_brute2(num) == is_prime_ferma(num) == is_prime_willson(num)):
            print(num, is_prime_brute2(num), is_prime_ferma(num), is_prime_willson(num))
    prflr.finish()

    for num in range(30000, 180999):
        is_prime_brute(num)
    prflr.finish()

    for num in range(30000, 180999):
        is_prime_brute2(num)
    prflr.finish()

    for num in range(30000, 30999):
        is_prime_ferma(num)
    prflr.finish()

    for num in range(30000, 30999):
        is_prime_willson(num)
    prflr.finish()



    # Пример генерации простых чисел
    prflr.start()
    print([i for i in prime_generator_willson(1000, 100)])
    prflr.finish()
    print(prime_interval_habr(1000))
    prflr.finish()
    print(sieve_of_eatosthenes(1000))
    prflr.finish()



    # Пример нахождения n-го простого числа
    prflr.start()
    print(get_n_prime(15000))
    prflr.finish()



    # Пример факторизации    
    prflr.start()
    print(factorization(100000204500456600, True))
    prflr.finish()



    # Пример нахождения колличества делителей
    prflr.start()
    print(divider_count(15432100))
    prflr.finish()
    print(divider_count_bad(15432100))
    prflr.finish()
    """
