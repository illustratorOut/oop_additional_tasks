"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:
    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        self.start_time = time.time()


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        # print(self.elapsed_time)
        return self.elapsed_time


with Timer() as timer:
# блок кода
    pass
print("Execution time:", timer.elapsed_time)
