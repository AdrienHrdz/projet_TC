filename = "./docPi/recolteDonneesCapteur8051/test.txt"

cpt = 0
while cpt <= 10:
    file = open(filename, 'r+')
    print(file.read())

    file.seek(0)
    file.write(str(cpt))
    file.truncate()

    file.close()
    cpt += 1
