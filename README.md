# Erste Aufgaben in Python zur Einführung

Dies sind erste Aufgaben die ich in meinem Programmierer Kurs gestellt bekommen habe, um Python besser zu verstehen.

___

## Python Basics

Hier werden einfache Variablen gesetzt und wieder ausgegeben.
```python
# Es sollen verschiedene Variablen gesetzt und wieder in der Konsole ausgegeben werden.

# Variablen definieren
first_name = "Thorsten"
last_name = "Zwegat"
birth_year = 1997
has_license = False

# Ausgabe
print(first_name)
print(last_name)
print(birth_year)
print(has_license)
```

___

## Mathematic Operations

Hier werden erste und einfache Mathematischen Operationen durchgeführt.
```python
# Hier sollen zwei Ganzzahlen definiert und dann mit verschiedenen Mathematischen Operationen berechnet werden.

# Variablen definieren
a = 10
b = 3

# Mathematische Operationen mit Ausgabe
print("Summe:",a+b)
print("Differenz:",a-b)
print("Produkt:",a*b)
print("Ganzzahliger Quotient:",a//b)
print("Rest der Divison:",a%b)
print("Hochrechnung:",a**b)
```

___

## Temperatur Changes

Hier soll die Temperatur von Celsius in Fahrenheit umgerechnet werden. Dies passiert einmal mit einer Benutzereingabe und anschließend mit vorgegebenen Werten.
```python
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
```

___

## Mehrwertsteuer-Berechnung

In diesem Programm soll zu einem Netto-Preis eines Produkts die Mehrwertsteuer hinzu addiert werden die bei 19% vom Netto-Preis liegt.
Dies passiert einmal mit einer Nutzereingabe und dann mit zwei vorgegebenen Werten.

```python
# Dies ist ein Programm das zu einem Preis die Mehrwertsteuer hinzu rechnen soll um den finalen Kaufpreis anzugeben

# Benutzer Eingabe mit umwandlung in Integer
benutzereingabe = input("Bitte Netto Preis eingeben: ")
c = float(benutzereingabe)

# Function
def price_with_tax(x):
    F = x * 1.19
    print(f"{F}" "€")

# Ausgabe
print("Ausgabe des Preises mit Mehrwertsteuer der Nutzereingabe:")
price_with_tax(c)

# Zweiter Teil der Aufgabe

artikel_preis1 = 99.99
artikel_preis2 = 1.99

# Ausgabe
print("Ausgabe des Preises mit Mehrwertsteuer mit einem Preis von 99,99€:")
price_with_tax(artikel_preis1)
print("Ausgabe des Preises mit Mehrwertsteuer mit einem Preis von 1,99€:")
price_with_tax(artikel_preis2)
```

___