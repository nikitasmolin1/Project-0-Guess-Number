"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np


number = np.random.randint(1, 101) # загадываем число


def guess_number(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = None # предполагаемое число
    min_number, max_number = 1, 100 # задаём рамки поиска
    
    while predict_number != number:
        count += 1
        predict_number = (min_number + max_number) // 2 # разбиваем пополам рамки поиска
        # сужаем рамки поиска
        if predict_number > number:
            max_number = predict_number
            
        elif predict_number < number:
            min_number = predict_number

    return count


def score_game(guess_number) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_lst = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_lst.append(guess_number(number))

    score = int(np.mean(count_lst)) # находим среднее количество попыток
    print(f'Your algorithm guesses the number in an average of {score} attempts!')
    
    return(score)


if __name__ == '__main__':
    score_game(guess_number)