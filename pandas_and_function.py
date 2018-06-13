# -*- coding: utf-8 -*-
import pandas
import pandas.core.series as Series
import numpy as np
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

# выводит заголовки таблицы вместо вывода всей большой таблицы
print list(data)
# print data

# Какое самое популярное женское имя на корабле?
def get_first_name(full_name):
    first_name = 'null'
    words = full_name.split()

    if "Miss." in words:
        index = words.index("Miss.")
        # print index
        first_name = words[index+1]

    if "Missis." in words:
        index = words.index("Missis.")
        # print index
        first_name = words[index+1]

    return first_name

# применяем функцию к каждой ячейке в столбце Name
data['Name'] = data['Name'].apply(get_first_name)
#  вышеуказанную функцию можно выполнить и так. Смысл тот же, но
#  первая запись короче
#  data['Name'] = data['Name'].apply(lambda x: get_first_name(x))

# выбираем только те строки, где в столбце Name не null (то есть
# только женские имена, потому что мужские не преобразовались)
onlyGirlsFirstNames = data.loc[data['Name'] != 'null']
# после применения groupby структура таблицы меняется, поэтому
# в конце требуется переиндексировать таблицу используя reset_index()
girlsNamesCount = onlyGirlsFirstNames.groupby(['Name']).size().reset_index()
# поскольку таблица изменилась и теперь содержит новую колонку с количеством встречаемых имен
# то надо переопределить имена колонок
girlsNamesCount.columns = ['Name', 'Count']
# метод sort принимает два аргумента. первый это имя\индекс столбица
# по которому идет сортировка.
# второй аргумент - это направление сортировки, по возрастанию или нет
girlsNamesCount_Sort = girlsNamesCount.sort_values(by=['Count'],ascending=False)
print girlsNamesCount_Sort

