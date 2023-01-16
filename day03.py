# prime number v0.3

number = int(input("input number : "))
counts = 0

for k in range(2, number):
    if number % k == 0:
        counts = counts + 1

if counts:
    print(f'{number} is NOT prime number.')
else:
    print(f'{number} is prime number!')

