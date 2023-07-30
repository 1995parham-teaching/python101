class SecretCounter:
    __secret_count: int = 0

    def inc(self):
        self.__secret_count += 1
        print(f"secret counter increased to: {self.__secret_count}")


if __name__ == "__main__":
    counter = SecretCounter()
    counter.inc()
    counter.inc()

    # AttributeError: 'SecretCounter' object has no attribute '__secret_count'
    # print(counter.__secret_count)

    print(
        "access to hidden property by force: "
        f"{counter._SecretCounter__secret_count}"  # type: ignore
    )
