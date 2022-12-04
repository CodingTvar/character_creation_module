from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: float):
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет: {calculate_square_root(your_number)}')


print(message)
calc(25.5)
