# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

num = (int(input("digite um numero: ")))

def verificar_paridade ():
    if num % 2 == 0:
        print (f"numero {num} é par")
    else:
        print (f"numero {num} é impar")

fim = verificar_paridade ()
print (fim)