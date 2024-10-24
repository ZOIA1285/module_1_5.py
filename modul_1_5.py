immutable_var = ('a', 12, 'd', False)
print(immutable_var)
# immutable_var[0] = 1
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Кортеж - неизменяемый тип данных
mutable_list = ['SDEK', 243, 0.4, 'f', True]
mutable_list[3] = 'j'
# меняем значение элемента по индексу
mutable_list.remove(0.4)
# убираем элемнт из списка
mutable_list.append(False)
# добавляем элемент всписок
mutable_list.extend('SDEK')
# добавляем элмент с перебором всех символов
print(mutable_list)