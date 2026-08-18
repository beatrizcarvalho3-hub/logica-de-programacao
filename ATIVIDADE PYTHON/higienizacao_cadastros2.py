cpf = input("CPF: ")
telefone = input("Telefone: ")

cpf = cpf.strip()
cpf = cpf.replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")

telefone = telefone.strip()
telefone = telefone.replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "")

print("CPF limpo:", cpf)
print("Telefone limpo:", telefone)