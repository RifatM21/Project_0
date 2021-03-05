import numpy as np


def find_num(number, predict, left=1, right=100): # рекурсивная функция, аргументы функции: загаданное число, угадываемое число, левая граница, правая граница
    global count # счётчик попыток виден глобально
    while predict != number: # цикл, который прервётся, когда угадываемов число станет равным загадонному
        count += 1 # при каждом входе в цикл, увеличение счётчика на 1
        if right - left == 2: # если диапозон, угадываемого числа равен 2, то загаданное число равно среднему значению границ диапозона
            predict = (left + right) // 2 
        elif predict > number: # нахождение правой границы
            if right > predict:
                right = predict
            else:
                predict = right
            predict -= ((left + right) // 2) # уменьшение угадываемого числа на половину диапозона
            return find_num(number, predict, left, right) # рекурсия с изменённой правой границей 
        else:
            if left < predict: # нахождение левой границы
                left = predict
            else:
                predict = left
            predict += ((right - left) // 2) + 1  # увеличение угадываемого числа на половину диапозона
            return find_num(number, predict, left, right) # рекурсия с изменёнными левой границей
    return count


def game_core_v3(number):
    global count # счётчик попыток виден глобально
    count = 1
    predict = np.random.randint(1, 101) # генерация угадываемого числа от 1 до 100 включительно
    find_num(number, predict) # вызов рекурсивной функции для поиска загаданного числа
    return count


def score_game(game_core_v3): # функция для нахождения среднего значения попыток
    count_ls = [] # пустой список для хранения значений счётчика
    np.random.seed(1) # фиксирование RANDOM SEED, чтобы эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=1000) # список из 1000 загадываемых чисел
    for number in random_array:
        count_ls.append(game_core_v3(number)) # запись значений счётчика попыток для каждого из 1000 загаданного числа
    score = int(np.mean(count_ls)) # среднее значение списка
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток") # вовыд среднего значения
    return score # вовзвращение среднего значения


score_game(game_core_v3)
