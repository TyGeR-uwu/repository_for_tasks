import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # начало измерения времени
        result = func(*args, **kwargs)
        end_time = time.time()  # конец измерения времени
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.6f} секунд")
        return result

    return wrapper


@timing_decorator
def sum_console(a, b):
    result = a + b
    print(f"Сумма {a} + {b} = {result}")
    return result


@timing_decorator
def sum_file(input_file='input.txt', output_file='output.txt'):
    with open(input_file, 'r') as file:
        a = int(file.readline().strip())
        b = int(file.readline().strip())

    result = a + b

    with open(output_file, 'w') as file:
        file.write(str(result))

    print(f"Результат записан в файл '{output_file}'")
    return result


# test part
if __name__ == "__main__":
    sum_console(5, 7)

    with open('input.txt', 'w') as f:
        f.write('10\n20\n')

    sum_file('input.txt', 'output.txt')
