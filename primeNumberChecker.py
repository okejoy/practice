
# this is to check for prime numbers
# numbers divisible by 1 and themselves
def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
            return "It is a prime number"
    else:
            return "It is not a prime number"


num = int(input("Enter number to check \n"))
print(prime_number(num))
