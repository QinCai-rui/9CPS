import sys

def is_prime(n):
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

def find_primes(limit):
    ordinal = 1
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(f'Prime {ordinal} is {n}')
            ordinal += 1
    return primes

if __name__ == "__main__":
    #UP_TO = 100
    #
    # primes = find_primes(UP_TO)
    #print(f"Primes up to {UP_TO}: {primes}")

    test_number = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("enter a number to check if it's prime: "))
    print(f"Is {test_number} prime? {is_prime(test_number)}")