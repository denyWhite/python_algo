import random, math


class Primes():
    # НОД чисел a и b
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    # Умножение a на b по модулю m
    def mul(self, a, b, m):
        if b == 1:
            return a
        if b % 2 == 0:
            t = self.mul(a, b/2, m)
            return 2*t % m
        return (self.mul(a, b-1,m) + a) % m

    # Возведение a в степень b по модулю m
    def pows(self, a, b, m):
        if b == 0:
            return 1;
        if b % 2 == 0:
            t = self.pows(a, b/2, m)
            return self.mul(t, t, m) % m
        return self.mul(self.pows(a, b-1, m), a, m) % m

    # Проверка на простоту тестом Ферма
    # https://ru.wikipedia.org/wiki/Тест_Ферма
    # По тестам работает медленнее, чем перебор
    def ferma(self, x):
        random.seed
        if x == 2:
            return True
        for _ in range(100):
            a = (random.randint(0, 32767) % (x - 2)) + 2
            if self.gcd(a,x) != 1:
                return False
            if self.pows(a, x-1, x) != 1:
                return False
        return True

    # Проверка на простоту перебором
    def brute(self, n):
        for i in range(2, int(n ** .5)):
            if n%i == 0:
                return False
            return True

    # Проверка на простоту по теореме Вильсона
    def wilson(self, n):
        return not (math.factorial(n - 1) + 1) % n


if __name__ == '__main__':
    from Profiler import Profiler
    pr = Primes()
    pflr = Profiler()
    pflr.start()
    print(pr.brute(14353453545434071234353453454723131124327))
    pflr.finish()
