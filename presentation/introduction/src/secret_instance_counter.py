class SecretCounter:
    def __init__(self):
        self.__secret_count: int = 0

    def inc(self):
        self.__secret_count += 1


if __name__ == "__main__":
    counter1 = SecretCounter()
    counter1.inc()
    counter1.inc()
    counter2 = SecretCounter()

    # AttributeError: 'SecretCounter' object has no attribute '__secret_count'
    # print(counter.__secret_count)

    print(
        "access to hidden property by force:\n"
        f"counter1: {counter1._SecretCounter__secret_count}\n"  # type: ignore
        f"counter2: {counter2._SecretCounter__secret_count}"  # type: ignore
    )
