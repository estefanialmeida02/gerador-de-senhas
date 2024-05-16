import random
import string

def gerar_senha(tamanho=12):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    todos_caracteres = letras + numeros + simbolos
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
    return senha

print("Bem-vindo ao gerador de senhas seguras!")
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha gerada é: {senha_gerada}")