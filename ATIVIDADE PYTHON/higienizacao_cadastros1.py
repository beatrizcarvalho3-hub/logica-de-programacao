nome = input("Nome: ")
email = input("E-mail: ")

nome = nome.strip().upper()
email = email.strip().lower()

print("Nome higienizado:", nome)
print("E-mail higienizado:", email)
