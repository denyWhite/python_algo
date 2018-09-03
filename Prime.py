import random, math # Для работы с классом Primes
import time # Для работы с классом Profiler


class Profiler():
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)

class Primes()
        
# НОД чисел a и b
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a % b)


# Умножение a на b по модулю m
def mul(a,b,m):
    if b==1:
        return a
    if b%2==0:
        t = mul(a, b/2, m)
        return 2*t % m
    return (mul(a, b-1,m) + a) % m


# Возведение a в степень b по модулю m
def pows(a, b, m):
    if b==0:
        return 1;
    if b%2==0:
        t = pows(a, b/2, m)
        return mul(t, t, m) % m
    return mul(pows(a, b-1, m), a, m) % m


# Проверка на простоту тестом Ферма
# https://ru.wikipedia.org/wiki/Тест_Ферма
# По тестам работает медленнее, чем перебор
def ferma(x):    
    random.seed
    if x == 2:
        return True
    for _ in range(100):
        a = (random.randint(0, 32767) % (x - 2)) + 2
        if gcd(a,x) != 1:            
            return False
        if pows(a, x-1, x) != 1:
            return False
    return True


# Проверка на простоту перебором
def bruteprime(n):
    for i in range(2, int(n ** .5)):
        if n%i==0:
            return False
        return True


# Проверка на простоту по теореме Вильсона
def wilson(n):
    return not (math.factorial(n - 1) + 1) % n


print(wilson(7))
