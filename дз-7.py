"""     Задание №1    """


# 1. Функция "ближайшее число"
def nearest_number(numbers, target):
    # Сортируем список по абсолютной разнице между числом и целевым числом
    sorted_numbers = sorted(numbers, key=lambda x: abs(x - target))
    return target, sorted_numbers


# Пример использования
numbers = [10, 3, 14, 5, 7]
target = 6
result = nearest_number(numbers, target)

print("Результат функции nearest_number:", result)  # (6, [5, 7, 3, 10, 14])

"""     Задание №2    """

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
squart_numbers = list(map(lambda x: x ** 2, numbers_list))

"""     Задание №3    """


def get_element_by_index(iterable: [1, 2, 3, 4, 5]):
    while 1:
        try:
            index = input(f'Введите индекс от 0 до {len(iterable) - 1} или введите exit для выхода: ').lower()
            if index == 'exit':
                print('выход из программы')
                break
            index = int(index)
            print(f'Элемент по индексу {index}: {iterable[index]}')
        except ValueError:
            print('Пожалуйста введите числовое значение индекса или exit для выхода')
        except IndexError:
            print(f'Неверный индекс ввадите индекс от 0 до {len(iterable) - 1}')


get_element_by_index([10, 20, 30, 40, 50])

print(even_numbers)
print(squart_numbers)