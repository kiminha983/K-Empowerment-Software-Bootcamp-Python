# prime number v0.4

number = int(input("input number : "))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')


