#1- Nome, idade e cidade → mensagem completa.
# nome = "Ricardo"
# idade = 44
# cidade = "Rio de Janeiro"

# print(f"Meu nome é {nome}, tenho {idade} anos e moro no {cidade}")



#2- Número → positivo, negativo ou zero.
# numero = int(input("Digite um número: "))
# if numero > 0: 
#     print('Positivo')
# elif numero < 0:
#     print('negativo')
# else:
#     print('Zero')

#3- IMC → calcular e classificar (Abaixo, Normal, Sobrepeso, Obesidade). 
# imc = peso / (altura ** 2)
#imc < 18.5 - abaixo do peso
#imc < 25 - normal
#imc < 30 - sobrepeso
#obesidade
# peso = 70
# altura = float(input('Digite a sua altura: '))

# imc = peso / (altura ** 2)
# print(f"o imc é {imc:.2f}")

# if imc < 18.5:
#     print('abaixo do peso')
# elif imc < 25:
#     print('normal')
# elif imc < 30:
#     print('sobrepeso')
# else:
#     print('obesidade')

#Exemplo 3 — Verificação de Desconto

# valor = float(input("Digite o valor da compra: "))

# if valor >= 200:
#     print("Desconto de 10% aplicado!")
#     # valor *= 0.9
#     valor = valor * 0.9
# else:
#     print("Sem desconto.")   
 
# print(f"Total a pagar: R${valor:.2f}")

# If aninhado (decisão dentro de decisão)

# nota = float(input("Nota: "))

# if nota >= 7:
#     participacao = input("Participou de todas as aulas? (s/n): ")
#     if participacao == "s":
#         print("Aluno aprovado com excelência.")
#     else:
#         print("Aprovado, mas com ressalvas de frequência.")
# else:
#     print("Aluno reprovado.")

#Exemplo — Sistema de Descontos por Categoria

# categoria = input("Digite o tipo de cliente (comum, vip, parceiro): ")
# valor = float(input("Valor da compra: "))

# if categoria == "vip":
#     desconto = 0.15
# elif categoria == "parceiro":
#     desconto = 0.10
# else:
#     desconto = 0.05

# valor_final = valor - (valor * desconto)
# print(f"Desconto aplicado: {desconto*100}%")
# print(f"Valor final: R${valor_final:.2f}")

# import time

# for segundos in range(5, 0, -1):
#     print(f"Iniciando em {segundos}...")
#     time.sleep(1)
# print("Começou!")

# Exemplo 2 — Soma de Números com Condição
total = 0
contador = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        break
    total += numero
    # contador += 1
    if total != 0:
        
        # media = total / contador
        print(f"Soma total: {total}")
        # # print(f"Soma Contador: {contador}")
        # print(f"Média dos números: {media:.2f}")
