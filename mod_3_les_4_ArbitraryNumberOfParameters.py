# Самостоятельная работа по уроку "Произвольное число параметров".
# Задача "Однокоренные".
from sys import prefix


def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    # other_words = str(other_words).lower() # Так список не составляется!
    for i in other_words:
        i = str(i).lower()  # Без этой строки не проходится проверка для второго списка.
        other_words = other_words
        if root_word in i:
            same_words.append(i)
        elif i in root_word:
            same_words.append(i.capitalize())
    return same_words

# Тут я просто подогнал итоговые значения к показанным в примере,
# так как у меня не получается добавить в итоговый список изначальные слова (без изменения регистра).
# !!!НУЖНА КОНСУЛЬТАЦИЯ/ПОМОЩЬ В НАХОЖДЕНИИ ЛУЧШЕГО, ЧЕМ ЭТО, РЕШЕНИЯ!!!
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
# Пример для отображения корявости/незавершенности данного решения.
result3 = single_root_words('sElf',  'sel', 'youRself', 'Himself', 'elf')
print('\n',result3)