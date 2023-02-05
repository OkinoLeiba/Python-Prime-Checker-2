import string, itertools
from typing import Iterator



str_prime = "The number is a prime number.\n"
str_notPrime = "The number is not a prime number.\n"
n = 0

def prime_check():
    while True:
        
        u_input = input("Input number to check t2o see if number is prime: ")
        for i in range(100):
            # prime = []
            prime = [lambda p: (6*i) - 1]
            #for l in itertools.takewhile(lambda l: (6*l) - 1, prime)) 
            all(n for i in itertools.takewhile(lambda l: (6*l) + 1, prime))
            # prime.append(n)
            i += 1

            if u_input == prime:
                print(str_notPrime)
            else:
                print(str_prime)


prime_check()   