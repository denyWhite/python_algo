"""
екотроые алгоритмы свзянные с простыми числами
"""
import random
import math


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
    return int(math.fabs(a * b) / gcd(a, b))


def multiply(a, b, m):
    """"Умножение a на b по модулю m
        :return: int
        """
    if b == 1:
        return a
    if b % 2 == 0:
        t = multiply(a, b / 2, m)
        return 2 * t % m
    return (multiply(a, b - 1, m) + a) % m


def powers(a, b, m):
    """"Возведение a в степень b по модулю m
        :return: int
        """
    if b == 0:
        return 1
    if b % 2 == 0:
        t = powers(a, b / 2, m)
        return multiply(t, t, m) % m
    return multiply(powers(a, b - 1, m), a, m) % m


def ferma(n, cnt=100):
    """"Проверка на простоту тестом Ферма
        https://ru.wikipedia.org/wiki/Тест_Ферма
        Работает медленнее, чем перебор
        :param n: Число для проверки
        :param cnt: Колличество проверок
        :return: bool
        """
    if n == 2:
        return True
    if n < 2:
        return False
    random.seed
    for _ in range(cnt):
        a = (random.randint(0, 2 ** 8) % (n - 2)) + 2
        if gcd(a, n) != 1 or powers(a, n - 1, n) != 1:
            return False
    return True


def brute(n):
    """Проверка на простоту перебором
        :param n: Число для проверки
        :return: bool
        """
    if n < 2:
        return False
    for iCounter in range(2, int(n ** .5) + 1):
        if n % iCounter == 0:
            return False
    return True


def wilson(n):
    """Проверка на простоту по теореме Вилсона
        Работает медленно из-за необходимости вычисления факториала
        https://ru.wikipedia.org/wiki/Теорема_Вильсона
        :param n: Число для проверки
        :return: bool
        """
    if n < 2:
        return False
    return not (math.factorial(n - 1) + 1) % n


def wilson_generator(num_count, start=2, finish=0):
    """Генератор простых чисел, с помощью теоремы Вилсона
        :param num_count: - количество сгенерированных простых чисел
        :param :start: если указан этот параметр, простые числа будут больше этого числа
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


def habr_prime(n):
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


def primfacs(n, as_dict=False):
    """
    Факторизация числа (разложение на простые множители)
    https://ru.wikipedia.org/wiki/Факторизация_целых_чисел
    :param n: число
    :param as_dict: Если истинно, вернуть словарем, где индекс - это множитель, а значение степень вхождения в разложение
    :return: список или словарь простых множителей
    """
    i: int = 2
    pfac = []
    while i * i <= n:
        while n % i == 0:
            pfac.append(i)
            n = int(n / i)
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


def mult_count_bad(n):
    """
    Количество делителей положительного числа перебором (жуть как медленно, так делать не надо)
    :param n: Число
    :return: Число, количество делителей
    """
    if n == 1:
        return 1
    cnt = 2
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            cnt += 1
    return cnt


def mult_count(n):
    """
    Количество делителей положительного исходя из следущего факта:
    пусть n = r1^t1*r2^t2...rn^tn разложение числа n на простые множители,
    тогда число делителей числа n равно CNT = (t1+1)*(t2+1)*...*(tn+1)
    :param n: Число
    :return: Число, количество делителей
    """
    dct = primfacs(n, True)
    cnt = 1;
    for val in dct.values():
        cnt *= (val + 1)
    return cnt


if __name__ == '__main__':
    from Profiler import Profiler
    prflr = Profiler()

    """
        # Пример нахождения НОД и НОК
        print(gcd(45,27))
        print(lcm(45,27))
    """

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
    print([i for i in wilson_generator(1000, 100)])
    prflr.finish()
    print(habr_prime(1000))
    prflr.finish()
    print(sieve_of_eatosthenes(1000))
    prflr.finish()
    """

    """
    # Пример факторизации    
    prflr.start()
    print(primfacs(100000204500456600, True))
    prflr.finish()
    """

    """
    # Пример нахождения колличества делителей
    prflr.start()
    print(mult_count(15432100))
    prflr.finish()
    print(mult_count_bad(15432100))
    prflr.finish()
    """
