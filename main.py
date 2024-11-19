with open ("text.txt", "r", encoding="utf-8") as file:
    a = file.read()
    b = a.split()
    with open ("output.txt", "w", encoding="utf-8") as file1:
        for i in b:
            if len(i) > 5:
                file1.write(str(i))
