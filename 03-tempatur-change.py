# In diesem Programm soll eine Funktion eine Grad Änderung von Fahrenheit zu Celsius berechnet werden

# Benutzer Eingabe mit umwandlung in Integer
benutzereingabe = input("Bitte Gradzahl eingeben: ")
c = int(benutzereingabe)

# Function
def tempeture(x):
    F = (9//5 * x + 32)
    print(f"{F}")

# Ausgabe
print("Temperatur in Fahrenheit der Nutzer eingabe:")
tempeture(c)

# Zweiter Teil der Aufgabe
celsius1 = 25
celsius2 = 10

print("Temperatur in Fahrenheit bei 25°C:")
tempeture(celsius1)
print("Temperatur in Fahrenheit bei 10°C:")
tempeture(celsius2)