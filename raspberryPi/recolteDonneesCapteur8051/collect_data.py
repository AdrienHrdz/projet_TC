# à connecter au GPIO du 8051
from gpiozero import Button
from time import sleep

# TODO : changer le numéro du GPIO
button = Button(5)

# TODO : changer le nom du fichier
filename = '/home/pi/Documents/PTC/communicationPi-Ordi/GPIO_distance.txt' 


while True:
    # ouverture du fichier
    file = open(filename, 'r+')
    print(file.read())
    
    file.seek(0)

    if button.is_pressed:
	# button pressed => écrire 1
        file.write('1')
        print("Button is pressed")
    else:
        file.write('0')
        print("Button is not pressed")
    file.truncate()
    # fermeture du fichier    
    file.close()    
