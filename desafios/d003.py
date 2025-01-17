# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

# Leitura de um valor pelo teclado
valor = input("Digite algo: ")

# Exibindo as informações sobre o valor digitado
print("Tipo primitivo:", type(valor))
print("É numérico?", valor.isnumeric())
print("É alfabético?", valor.isalpha())
print("É alfanumérico?", valor.isalnum())
print("Está em maiúsculas?", valor.isupper())
print("Está em minúsculas?", valor.islower())
print("Está capitalizado?", valor.istitle())
print("É um espaço em branco?", valor.isspace())
