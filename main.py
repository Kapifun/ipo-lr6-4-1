# Написать программу, которая:

# - Создаёт список из 6 строк (*строки определяются в коде, на ваш вкус*).
# - Подсчитывает количество строк, содержащих букву `г`.
# - Использует циклы для подсчета.

spis=["где", "там", "мно", "лекции", "по", "ИПО", "Когда"]#создание списка
g=0 #инициализация переменной g
for i in spis:#цикл
    char="г"#инициализация переменной char
    if  char in i:#проверка на количество букв г
        g +=1#добавление количество букв г
print('Кол-во строк в которых есть буква г:',g)#вывод данных
