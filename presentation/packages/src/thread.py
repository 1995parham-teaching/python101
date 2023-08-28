import threading
import time


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        super().__init__()
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f"starting {self.name}...")
        print_time(self.name, 5, self.counter)
        print(f"exiting {self.name}...")


def print_time(thread_name: str, delay: int, counter: int):
    while counter:
        time.sleep(delay)
        print(f"{thread_name} {time.ctime(time.time())}")
        counter -= 1


if __name__ == "__main__":
    # create new threads
    thread1 = MyThread(1, "thread-1", 1)
    thread2 = MyThread(2, "thread-2", 2)

    # start new Threads
    thread1.start()
    thread2.start()

    print("exiting the main thread")
