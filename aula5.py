#estruturas condicionais

a = 5
b = 10

if a < b:
    print("a é menor que b")
if a > b:
    print("a é maior que b")
if a == b:
    print("a é igual a b")

#estrutura condicional composta
if a < b:
    print("a é menor que b")
else:   
    print("a é maior ou igual a b")

#estrutura condicional encadeada
if a < b:
    print("a é menor que b")
elif a > b:
    print("a é maior que b")
else:
    print("a é igual a b")

"""como funciona o elif
    o elif é uma estrutura condicional que permite verificar múltiplas condições de forma sequencial.
    Se a primeira condição for verdadeira, o bloco de código correspondente será executado.
    Se a primeira condição for falsa, o programa verifica a próxima condição.
    Se nenhuma das condições for verdadeira, o bloco de código do else será executado.
"""
#estrutura condicional aninhada
if a < b:
    print("a é menor que b")
    if a < 0:
        print("a é negativo")
    else:
        print("a é positivo ou zero")

#estrutura condicional com operadores lógicos
if a < b and a > 0:
    print("a é menor que b e positivo")
if a < b or a > 0:
    print("a é menor que b ou positivo")
if not a < b:
    print("a não é menor que b")

#definindo funcoes para verificar se um número é par ou ímpar
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
print(verificar_paridade(4))  # Isso retornará "par"
print(verificar_paridade(7))  # Isso retornará "ímpar"


#aplicando elif para verificar a faixa etária de uma pessoa
def verificar_faixa_etaria(idade):
    if idade < 0:
        return "Idade inválida"
    elif idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 65:
        return "Adulto"
    else:
        return "Idoso"
print(verificar_faixa_etaria(5))   # Isso retornará "Criança"
print(verificar_faixa_etaria(15))  # Isso retornará "Adolescente"
print(verificar_faixa_etaria(30))  # Isso retornará "Adulto"
print(verificar_faixa_etaria(70))  # Isso retornará "Idoso  "
print(verificar_faixa_etaria(-5))  # Isso retornará "Idade inválida"

"""Resumo:
- As estruturas condicionais permitem que o programa tome decisões com base em condições específicas.
Explocacao dos codigos:
- O primeiro bloco de código verifica se a é menor, maior ou igual a b usando ifs separados.
- O segundo bloco de código usa uma estrutura condicional composta (if-else) para verificar se a é menor que b ou não.
- O terceiro bloco de código usa uma estrutura condicional encadeada (if-elif-else) para verificar todas as possibilidades entre a e b.
- O quarto bloco de código mostra uma estrutura condicional aninhada, onde um if está dentro de outro if para verificar se a é negativo ou positivo.
- O quinto bloco de código demonstra o uso de operadores lógicos (and, or, not  ) para combinar condições em uma única expressão condicional.
- O operador and retorna True se ambas as condições forem verdadeiras, o operador or retorna True se pelo menos uma das condições for verdadeira, e o operador not inverte o valor booleano da condição.
o sexto bloco de código define uma função para verificar se um número é par ou ímpar usando o operador módulo (%).
- O sétimo bloco de código define uma função para verificar a faixa etária de uma pessoa usando uma estrutura condicional encadeada (if-elif-else) para categorizar a idade em diferentes faixas etárias.
- O resumo final destaca a importância das estruturas condicionais para permitir que o programa tome decisões com base em condições específicas, e a explicação dos códigos detalha como cada bloco de código funciona para implementar diferentes tipos de estruturas condicionais.

"""