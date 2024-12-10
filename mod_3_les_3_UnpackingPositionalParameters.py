# Самостоятельная работа по уроку "Распаковка позиционных параметров". Задача "Распаковка.

def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(10)
print_params(2, 3)
print_params(4, 5, 6)

values_list = [333, 'something', False]
values_dict = {'a':11, 'b':'second', 'c':True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('random', True)
print_params(*values_list_2, 42)

# Важно!
# Не передавайте списки задавая по умолчанию пустой список или другой изменяемый тип данных!
# В таком случае, если этот список будет изменён внутри функции, то на следующий вызов функции он останется в том же состоянии.
#
# def a(my_list = [])) – это приводит к ошибкам!
#
# Можно передавать вот так(список создаётся локально, мы не влияем на его изменение вне функции)
# def append_to_list(item, list_my=None):
#   if list_my is None:
#    list_my = []
#   list_my.append(item)
# print(list_my)
