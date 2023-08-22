import io


if __name__ == "__main__":
    f = open("hello.txt", "w", encoding="utf-8")
    f.seek(100, io.SEEK_SET)
    f.write("Hello World")
    f.close()
