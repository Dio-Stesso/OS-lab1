import threading
import queue
import time
import random


def f(x):
    # Simulate computation and errors
    time.sleep(random.uniform(0.1, 0.5))  # simulate computation time
    if random.choice([True, False]):
        return x * 2  # simulate calculation
    else:
        raise ValueError("Critical error in f(x)")  # simulate critical failure


def g(x):
    # Simulate computation and errors
    time.sleep(random.uniform(0.1, 0.5))
    if random.choice([True, False]):
        return x + 3
    else:
        raise ValueError("Critical error in g(x)")


def binary_operation(f_result, g_result):
    return f_result + g_result


class Manager:
    def __init__(self, x):
        self.x = x
        self.f_result = None
        self.g_result = None
        self.f_thread = threading.Thread(target=self.compute_f)
        self.g_thread = threading.Thread(target=self.compute_g)
        self.result_queue = queue.Queue()

    def compute_f(self):
        try:
            self.result_queue.put(('f', f(self.x)))
        except Exception as e:
            self.result_queue.put(('f_error', e))

    def compute_g(self):
        try:
            self.result_queue.put(('g', g(self.x)))
        except Exception as e:
            self.result_queue.put(('g_error', e))

    def manage_computation(self):
        self.f_thread.start()
        self.g_thread.start()

        # Wait for threads to finish and handle results
        while self.f_result is None or self.g_result is None:
            result_type, result = self.result_queue.get()
            if result_type == 'f':
                self.f_result = result
            elif result_type == 'g':
                self.g_result = result
            elif 'error' in result_type:
                print(f"Error occurred: {result}")
                return "Computation failed due to error."

        if self.f_result is not None and self.g_result is not None:
            return binary_operation(self.f_result, self.g_result)


def main():
    x = int(input("Enter an integer x: "))
    manager = Manager(x)
    result = manager.manage_computation()
    if result != "Computation failed due to error.":
        print(f"The result of the binary operation is: {result}")
    else:
        print(result)


if __name__ == "__main__":
    main()
