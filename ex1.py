# Nome: João Pedro
# Exercício 1 - Fibonacci


def calculateFib(choice: int) -> bool:
    if choice == 0 or choice == 1:
        return True
    
    a,b = 0, 1
    c = a + b # 1
    while c <= choice:
        a = b
        b = c
        c = a + b
        if c == choice:
            return True

    return False


if __name__ == "__main__":
    choice = int(input("Digite o primeiro número: "))
    
    if calculateFib(choice):
        print(f"O número {choice} pertence a sequência!")
    else:
        print(f"O número {choice} não pertence a sequência!")
