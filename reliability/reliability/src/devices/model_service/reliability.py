import datetime
import os
import matplotlib.pyplot as plt

from devices.models import Element
import math

My_k = 1
plan_dir = os.getcwd() + '\\files\\plan.txt'


def count_schem(schem_type: str, period: int, reliability: float) -> float:
    """Расчёт схемы (вернем последнюю надежность)"""
    result_list = list()
    for x in range(1, period):
        result = 1

        for i in range(1, len(schem_type)+1):
            result = result * part_counter(schem_type[i-1], i, x)
        if result < reliability:
            replacer(schem_type, x)  # если результат ниже ожидаемой надежности заменяем элемент
        print('Надёжность системы=', result)
        result_list.append(result)
    # График
    plt.plot(range(1, period), result_list)
    plt.savefig(os.getcwd() + '\\files\\graph.png')

    return result


def part_counter(schem_type: str, schem_part: int, x: int) -> float:
    """Расчет надежности для части схемы"""
    elements_number = get_number_of_elements(schem_type)
    element_array = list()
    for i in range(1, elements_number + 1):
        element_array.append(Element.objects.get(number=i, sub_system=schem_part))
    # try:
    match schem_type:
        case 'A':
            return function(count_time(element_array[0].date, x),
                            element_array[0].operating_time)
        case 'B':
            e1 = function(count_time(element_array[0].date, x), element_array[0].operating_time)
            e2 = function(count_time(element_array[1].date, x), element_array[1].operating_time)
            return 1 if (e1 + e2) > 1 else e1 + e2
        case 'C':
            e1 = (function(count_time(element_array[1].date, x), element_array[1].operating_time) * 
                  function(count_time(element_array[2].date, x), element_array[2].operating_time))
            e2 = function(count_time(element_array[0].date, x), element_array[0].operating_time)
            return 1 if (e1 + e2) > 1 else e1 + e2
        case 'D':
            e1 = (function(count_time(element_array[0].date, x), element_array[0].operating_time) *
                  function(count_time(element_array[1].date, x), element_array[1].operating_time))
            e2 = (function(count_time(element_array[2].date, x), element_array[2].operating_time) *
                  function(count_time(element_array[3].date, x), element_array[3].operating_time))
            return 1 if (e1 + e2) > 1 else e1 + e2
        case _:
            return 0
    # except IndexError:
    #     print('Не были указаны параметры для части схемы!')


def function(x, operating_time) -> float:
    """Функция распределения; My_lambda - интенсивность отказов; x - время работы"""
    my_lambda = 1/operating_time
    # f = 1 - math.exp(-my_lambda*x)  # Экспоненциальное
    # (My_k / my_lambda) * ((x / my_lambda) ** (My_k - 1)) * math.exp(-(x / my_lambda) ** My_k)  # Вейбула
    # print('Лямбда=', my_lambda)
    # print('Время в расчёте=', x)
    if x < 0:
        print(x)
        print('Ошибка!')
        f = 1
    else:
        f = math.exp(-my_lambda*x)
    return f


def get_number_of_elements(schem_type: str):
    """Количество элементов в схеме"""
    match schem_type:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
        case 'D':
            return 4
        case _:
            return 0


def replacer(schem_type, x):
    """Заменяет элемент вышедший из строя"""
    part_result = list()
    for i in range(1, len(schem_type)+1):
        part_result.append(part_counter(schem_type[i - 1], i, x))

    min_result = min(part_result)
    for part_number, part in enumerate(part_result, start=1):
        if part == min_result:
            replace_element(part_number, schem_type[part_number-1], x)  # меняем элемент в определенной части схемы


def replace_element(part_number: int, schem_type: str, x: int):
    """Меняет самый слабый элемент в части схемы"""
    elements = Element.objects.filter(sub_system=part_number)
    match schem_type:
        case 'A':
            change_date(elements[0], part_number, x)
        case 'B':
            e1 = function(count_time(elements[0].date, x), elements[0].operating_time)
            e2 = function(count_time(elements[1].date, x), elements[1].operating_time)
            if e1 > e2:
                change_date(elements[1], part_number, x)
            else:
                change_date(elements[0], part_number, x)
        case 'C':
            e1 = (function(count_time(elements[1].date, x), elements[1].operating_time) *
                  function(count_time(elements[2].date, x), elements[2].operating_time))
            e2 = function(count_time(elements[0].date, x), elements[0].operating_time)
            if e2 > e1:
                if (function(count_time(elements[1].date, x), elements[1].operating_time) > 
                        function(count_time(elements[2].date, x), elements[2].operating_time)):
                    change_date(elements[2], part_number, x)
                else:
                    change_date(elements[1], part_number, x)
            else:
                change_date(elements[0], part_number, x)

        case 'D':
            e1 = (function(count_time(elements[0].date, x), elements[0].operating_time) *
                  function(count_time(elements[1].date, x), elements[1].operating_time))
            e2 = (function(count_time(elements[2].date, x), elements[2].operating_time) *
                  function(count_time(elements[3].date, x), elements[3].operating_time))
            if e2 > e1:
                if (function(count_time(elements[0].date, x), elements[0].operating_time) >
                        function(count_time(elements[1].date, x), elements[1].operating_time)):
                    change_date(elements[1], part_number, x)
                else:
                    change_date(elements[0], part_number, x)
            else:
                if (function(count_time(elements[2].date, x), elements[2].operating_time) >
                        function(count_time(elements[3].date, x), elements[3].operating_time)):
                    change_date(elements[3], part_number, x)
                else:
                    change_date(elements[2], part_number, x)
        case _:
            print('Неизвестный тип схемы!')


def change_date(el, part_number, x):
    """Меняем дату устаовки в модели и записываем в файл"""

    print(f'Меняем {el.element} | Часть схемы: {part_number} | Элемент схемы: 1 | Время {x} д.')
    print(el.date)
    el.date = datetime.date.today() + datetime.timedelta(days=x)
    print(el.date)
    with open(plan_dir, 'a') as f:
        f.write(f'\nМеняем {el.element} |'
                f' Часть схемы: {part_number} |'
                f' Элемент схемы: 1 |'
                f' Время {x} д. спустя начала работы |'
                f' {el.date} - дата замены.')
    el.save()


def count_time(date: datetime, x: int) -> int:
    """Расчет времени работы"""
    x1 = (datetime.date.today()-date).days
    # print('Прошло времени =', x1)
    return int(x1 + x)
