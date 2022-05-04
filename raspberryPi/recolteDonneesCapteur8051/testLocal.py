import time

filename = "./projet_TC/raspberryPi/recolteDonneesCapteur8051/test.txt"

cpt = 0
while cpt <= 10:
    file = open(filename, 'r+')
    print(file.read())

    file.seek(0)
    file.write(str(cpt))
    file.truncate()

    file.close()

    time.sleep(1)
    cpt += 1
