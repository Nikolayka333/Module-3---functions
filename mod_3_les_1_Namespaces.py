# Домашняя работа по уроку "Пространство имён"

calls = 0

def count_call():
    global calls
    calls += 1

def string_info(string:str = '')->tuple:
    string_= string
    up = string_.upper()
    low = string_.lower()
    final = (len(string_), up, low)
    count_call()
    return final

def is_cotains(string, list_to_search)->bool:
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_call()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            decision = True
            break
        else:
            decision = False
            continue
    return decision

print(string_info('text'))
print(string_info('text for test'))
print(string_info('Text_FOR_tesT_2'))
print(is_cotains('size',['Sizes', 'sizeble', 'sise']))
print(is_cotains('father',['mother', 'grandFather', 'FaTHer']))
print(calls)
print(f'Функции вызваны - {calls} раз(а)')
