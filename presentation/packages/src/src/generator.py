def fibonacci(count):
    # these seed values generate 0 and 1 when fed into the loop
    a, b = -1, 1
    while count > 0:
        # yield the value for this iteration
        c = a + b
        yield c
        # update values for next iteration
        a, b = b, c
        count -= 1


def yielder():
    print("-0-")
    yield 1
    print("-1-")
    yield 2
    print("-2-")
    yield 3
    print("-3-")


if __name__ == "__main__":
    # generator
    gen = (value for value in range(10) if value > 5)
    # list
    lst = [value for value in range(10) if value % 2 == 0]
    print(gen)
    print(lst)
    print(min(lst))
    print(min(lst))
    print(min(gen))
    # we will get an error on this because you can iterate a generator only once
    # print(min(gen))

    print(f"\n{' fibonacci sequence: ':=^50s}\n")
    for x in fibonacci(10):
        print(x)

    fibonacci_generator = fibonacci(10)
    print(next(fibonacci_generator))

    print(f"\n{' yielder sequence: ':=^50s}\n")

    for x in yielder():
        print(x)
        print(f"{'':*<10s}")

    print(f"{'':=<50s}")
