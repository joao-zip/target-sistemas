# Nome: João Pedro
# Exercício 2 - Verificação de String


if __name__ == "__main__":
    string = input('Digite a string: ')

    qtd_a = string.lower().count('a')
    print(f"A string contém {qtd_a} caracteres a") if qtd_a != 0 else print('A string não tem letras a')
