import string 


prime = []
str_prime = "The number is a prime number.\n"
str_notPrime = "The number is not a prime number.\n"


def prime_check():
    while True:
        u_input = input("Input number to check to see if number is prime: ")
        if all([n for l in (lambda l: (6*l) - 1)]): #+ [n for l in (lambda l: (6*l) + 1)]):
            prime.append(n)

        if u_input == prime:
            print(str_notPrime)


prime_check()   