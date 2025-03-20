import sys
from multiprocessing import Pool, cpu_count

def is_prime(n):
    """Prime checking function using 6k +/- 1 rule"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def find_primes_parallel(limit):
    """Find all prime numbers up to a given limit using multiple processes"""
    with Pool(cpu_count()) as pool:
        numbers = range(2, limit + 1)
        results = pool.map(is_prime, numbers)
    primes = [n for n, is_prime_flag in zip(numbers, results) if is_prime_flag]
    return primes

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            test_number = int(sys.argv[1])
            print(f"Is {test_number} prime? {is_prime(test_number)}")
        else:
            limit = int(input("Enter a limit to find primes up to: ").strip())
            primes = find_primes_parallel(limit)
            print(f"Primes up to {limit}: {primes}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
