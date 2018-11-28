# code om een nummer te raden
# het te raden nummer eerst vastzetten in variabele secret
secret = 27
# opdracht geven om te raden naar het nummer
guess = int (raw_input("Welk getal tussen 1 en 30 zit er in mijn hoofd?"))

#evalueren of de gok gelijk is aan het ingestelde getal
if secret == guess:
    print ("Goed gegokt, misschien  mee doen de lotto?")

else :
    print ("Je mag 3 keer raden voor 12 euro!!")

