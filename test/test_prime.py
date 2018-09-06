import unittest
import prime


class TestPrime(unittest.TestCase):
    def test_gcd(self):
        assert (prime.gcd(1000, 1000) == 1000)

    def test_gcd2(self):
        assert (prime.gcd(1, 1) == 1)

    def test_gcd3(self):
        assert (prime.gcd(17, 13) == 1)

    def test_lcm(self):
        assert (prime.lcm(30, 18) == 90)

    def test_multyply_m(self):
        assert (prime.multiply_m(17, 19, 3) == 2)

    def test_powers_m(self):
        assert (prime.powers_m(17, 2, 3) == 1)

    def test_fact_m(self):
        assert (prime.fact_m(5, 7) == 1)

    def test_is_prime_ferma(self):
        assert (not prime.is_prime_ferma(1))

    def test_is_prime_ferma2(self):
        assert (prime.is_prime_ferma(2))

    def test_is_prime_ferma3(self):
        assert (not prime.is_prime_ferma(100000))

    def test_is_prime_ferma4(self):
        assert (prime.is_prime_ferma(97777))

    def test_is_prime_brute(self):
        assert (not prime.is_prime_brute(1))

    def test_is_prime_brute2(self):
        assert (prime.is_prime_brute(2))

    def test_is_prime_brute3(self):
        assert (not prime.is_prime_brute(100000))

    def test_is_prime_brute4(self):
        assert (prime.is_prime_brute(97777))

    def test_is_prime_brute20(self):
        assert (not prime.is_prime_brute2(1))

    def test_is_prime_brute22(self):
        assert (prime.is_prime_brute2(2))

    def test_is_prime_brute23(self):
        assert (not prime.is_prime_brute2(100000))

    def test_is_prime_brute24(self):
        assert (prime.is_prime_brute2(97777))

    def test_is_prime_willson(self):
        assert (not prime.is_prime_willson(1))

    def test_is_prime_willson2(self):
        assert (prime.is_prime_willson(2))

    def test_is_prime_willson3(self):
        assert (not prime.is_prime_willson(100000))

    def test_prime_generator_willson(self):
        assert (sum([i for i in prime.prime_generator_willson(2, 1000, 1100)]) == 2022)

    def test_prime_interval_habr(self):
        assert (sum(prime.prime_interval_habr(100)) == 1060)

    def test_get_n_prime(self):
        assert (prime.get_n_prime(500) == 3571)

    def test_sieve_of_eatosthenes(self):
        assert (sum(prime.sieve_of_eatosthenes(100)) == 1060)

    def test_divider_count_bad(self):
        assert (prime.divider_count_bad(1000) == 16)

    def test_divider_count(self):
        assert (prime.divider_count(1000) == 16)

    def test_divider_sum(self):
        assert (prime.divider_sum(1000) == 2340)

    def test_divider_sum_and_count(self):
        assert (prime.divider_sum_and_count(1000) == (2340, 16))

    def test_euler(self):
        assert (prime.euler(997) == 996)

    def test_euler2(self):
        assert (prime.euler(1000) == 400)

    def test_big_test(self):
        prime_num = prime.get_n_prime(10000)
        sm, cnt = prime.divider_sum_and_count(prime_num)
        assert (sm + prime.euler(prime_num) == prime_num * cnt)


if __name__ == '__main__':
    unittest.main()
