#1- Peça um número e diga se é par ou ímpar.
# numero = int(input("Digite um número: "))
# if numero%2 == 0:
#     print("Número é par")
# else:
#     print("Número ímpar")

#2- Solicite idade e diga se é criança, adolescente ou adulto
# idade = int(input("Digite a idade: "))
# if idade < 12: 
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# else:
#     print("Adulto")

#3- Receba duas notas e informe: aprovado, recuperação ou reprovado.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1+nota2)/2

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")