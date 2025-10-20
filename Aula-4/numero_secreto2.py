import random
print(18*"-")
print("| Descubra o valor |")
print(18*"-")

numero_oculto = random.randrange(1,100)
chances = 0
pontos = 100
perder = 0
nivel = int(input("Escolha um nível:\n 1-Facil\n 2-Médio\n 3-Difícil\n Esolha: "))

if nivel == 1:
    chances = 30
    perder = 10
elif nivel == 2:
    chances = 15
    perder = 20
elif nivel == 3:
    chances = 5
    perder = 50
else:
    print("Esta opção não é aceita. Digite apena 1, 2 ou 3")

print(f"Você tem {pontos} pontos")

for tentativa in range(1,chances+1):
    print(f"Tentativa {tentativa} de {chances}")
    valor_usuario = int(input("Informe um valor entre 10 e 100: "))
    if pontos < 0:
        pontos = 0
    else:    
        if valor_usuario == numero_oculto:
            print("Parabéns!!! Você acertou o número")
            break
        elif valor_usuario > numero_oculto:
            tentativa -= tentativa
            pontos -= perder
            print(f"O valor digitado {valor_usuario} é maior que o número secreto. Você tem {tentativa} tentativas ")
        else:     
            tentativa -= tentativa
            pontos -= perder
            print(f"O valor digitado {valor_usuario} é menor que o número secreto. Você tem {tentativa} tentativas")

print(f"Sua pontuação foi: {pontos} ")
print(f"O valor oculto era: {numero_oculto}")
print("Fim do jogo!")