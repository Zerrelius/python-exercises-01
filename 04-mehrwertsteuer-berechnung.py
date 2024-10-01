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