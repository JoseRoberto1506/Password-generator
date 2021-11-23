from string import ascii_letters, digits
from secrets import choice

lenght = int(input("Você deseja uma senha de quantos caracteres? "))
special_characters = "!#$%&()*+,-./:;<=>?@[\]_{|}."
characters = ascii_letters + special_characters + digits

while True:
    password = ''.join(choice(characters) for i in range (lenght))
    if (any(c.islower() for c in password) and 
        any(c.isupper() for c in password) and 
        any(c.isdigit() for c in password) and
        any(sc in special_characters for sc in password)):
        break

print(password)
