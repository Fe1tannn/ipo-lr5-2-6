with open ("text.txt", "r", encoding="utf-8") as file: #Открываем файл
    a = file.read() #Сохраняем данные файла в переменной a
    b = a.split() #Сохраняем слова в список b
    with open ("output.txt", "w", encoding="utf-8") as file1: #Открываем файл
        for i in b: #Перебор
            if len(i) > 5: #Условие
                file1.write(str(i)) #Записываем элемент i в файл
