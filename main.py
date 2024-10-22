import time
import random
from collections import deque


"""
Вопрос №1

На языке Python написать алгоритм (функцию)
определения четности целого числа,
который будет аналогичен нижеприведенному по функциональности,
но отличен по своей сути.
Объяснить плюсы и минусы обеих реализаций.
Пример:

def isEven(value):

      return value % 2 == 0
"""


def my_is_even(value: int) -> int:
    """
    Моё представление определения чётности числа
    """
    return (value // 2) * 2 == value


"""
В вашем примере реализован остаток от деления,
если он равен 0 - то число чётное.

Мой пример предлагает аналогичный результат, используя другой оператор
// - целочисленное деление, если его умножить на 2, значит число четное.

Эти две функции находят чётные числа, используя разные
операторы Python.
Ваш пример - самый удобный по нахождению. Как я считаю,
его удобно использовать для алгоритмических задач.

Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих
циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Оценивается:

Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""


class Decoder:
    """
    Класс расшифровывает входящую строчную команду.
    FIFO - это стак, когда первым извлекают элемент,
    который добавили раньше всех.
    "Первый вошёл - первый вышел."
    """

    def __init__(self, data: str):
        """
        Конструктор класса, Decoder принимает
        один аргумент для обратотки методом decode.
        """
        self.data = data

    def decode(self) -> str:
        stack: list = []
        current_string: str = ''
        prev_string: str = ''
        prev_num: int = 0
        num_token: str = ''

        for character in self.data:
            if character.isdigit():
                num_token += character
            elif character == '[':
                stack.append((current_string, int(num_token)))
                current_string = ''
                num_token = ''
            elif character == ']':
                prev_string, prev_num = stack.pop()
                current_string = prev_string + current_string * prev_num
            else:
                current_string += num_token
                num_token = ''
                current_string += character

        return current_string


class MyDeque(Decoder):
    """
    Унаследовавшись от Decoder - мы используем его
    конструктор __init__, этот принцип ООП - наследование.

    Класс реализует подсчёт вставки элементов
    в список и выводит результаты
    для обычной вставки
    и с использованием дек.
    Дек - работает с данными с двух сторон.
    Каждый элемент обрабатывается как O(1)
    В списке обработка происходит как O(n)
    """

    def run(self):
        start_time = time.time()
        data1 = []
        for data_index in range(self.data):
            data1.insert(0, data_index)
        first_answer: float = time.time() - start_time

        start_time = time.time()
        data2 = deque()
        for data_index in range(self.data):
            data2.appendleft(data_index)
        second_answer: float = time.time() - start_time
        return print(f'\nбез deque {first_answer}'
                     f' с использованием deque {second_answer}')


if __name__ == '__main__':
    """
    Такая конструкция позволяет использовать код,
    как отдельные модули: классы и их методы.
    Здесь мы будем их вызывать с определёнными параметрами.
    """
    instruction_list = [
        "3[ab]", "2[3[a]b]", "3[a2[c]]", "2[abc]3[de]", "3[abc2[de]]"
    ]
    for inst in instruction_list:
        decoder = Decoder(inst)
        print(f'Вход: {inst}, результат decode: {decoder.decode()}')

    data = 100000
    my_deque = MyDeque(data)
    my_deque.run()


"""
Вопрос №3

На языке Python предложить алгоритм,
который быстрее всего (по процессорным тикам)
отсортирует данный ей массив чисел.
Массив может быть любого размера со случайным порядком чисел
(в том числе и отсортированным).
Объяснить, почему вы считаете, что функция соответствует заданным критериям.
"""


def quicksort(data):
    """
    Я думаю, что Быстрая сортировка - это хороший вариант,
    Не только по скорости, но и по области применения.
    Средний случай:
    O(n log(n))
    """
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        less = [i for i in data[1:] if i < pivot]
        greather = [i for i in data[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greather)


data = [random.randint(1, 1000) for _ in range(100)]


start_time = time.time()
sorted_data = quicksort(data)
end_time = time.time()
print('\nИсходный массив:', data)
print("\nОтсортированный массив:", sorted_data)
print(f"\nВремя сортировки для data: {end_time - start_time:.6f} секунд")
