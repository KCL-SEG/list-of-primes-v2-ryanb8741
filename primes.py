"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 2

    if (number_of_primes < 1):
        raise (ValueError)

    while(1):
        if(isPrime(i) == True):
            list.append(i)
            if(len(list) == number_of_primes):
                break
            i += 1
        else:
            i+=1
    return list

def isPrime(n):
    for i in range(2, n//2 + 1):
        if(n % i == 0):
            return False
    return True
