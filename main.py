with open ("text.txt", "r", encoding="utf-8") as file:
    a = file.read()
    b = a.split()
    c = []
    for i in b:
        if len(i) == 5:
            c.append()
    with open ("output.txt", "w", encoding="utf-8") as file1:
        file1.write(c)
