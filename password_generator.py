import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Mindestens ein Zeichentyp muss ausgewählt sein!")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Beispiel: Benutzerdefinierte Eingaben
    try:
        length = int(input("Länge des Passworts: "))
        use_upper = input("Großbuchstaben verwenden? (j/n): ").lower() == 'j'
        use_lower = input("Kleinbuchstaben verwenden? (j/n): ").lower() == 'j'
        use_digits = input("Zahlen verwenden? (j/n): ").lower() == 'j'
        use_symbols = input("Sonderzeichen verwenden? (j/n): ").lower() == 'j'

        pwd = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"🔐 Dein generiertes Passwort: {pwd}")
    except ValueError as e:
        print(f"Fehler: {e}")
