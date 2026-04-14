"""
valores booleanos são usados para representar a verdade ou a falsidade de uma afirmação. Eles são comumente usados em programação para controlar o fluxo de execução de um programa, tomar decisões e realizar comparações. Em Python, os valores booleanos são representados por True e False.

"""

#Exemplo

lista = [1, 2, 3, 4, 5]
print(3 in lista)  # Isso retornará True, pois 3 está presente na lista
print(6 in lista)  # Isso retornará False, pois 6 não está presente

print(5 > 3)  # Isso retornará True, pois 5 é maior que 3
print(2 < 1)  # Isso retornará False, pois 2 não é menor que 1

print(True and False)  # Isso retornará False, pois ambos os operandos precisam ser True para o resultado ser True
print(True or False)   # Isso retornará True, pois pelo menos um dos operandos é True
print(not True)        # Isso retornará False, pois o operador not inverte o valor booleano

print(lista[0] == 1)  # Isso retornará True, pois o primeiro elemento da lista é igual a 1
print(lista[1] == 2)  # Isso retornará True, pois o segundo

print(lista not in lista)  # Isso retornará False, pois a lista está presente nela mesma