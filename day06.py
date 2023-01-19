def a():  # generator
    yield 1
    yield 2
    yield 3


def b():  # normal function
    return 1  # stop
    return 2
    return 3


print(a(), b())
c = a()
print(c)
for i in c:
    print(i)

for i in c:
    print(i)
