import random as rd

print("\n ")
print("\n Bem vindo ao jogo de adivinhação!")
print("\n ")

#Declaração de variáveis
n_secreto = rd.randrange(1,101)
tentativas = 10
rodada = 1

for rodada in range(1,tentativas +1): 
    print(f"Tentativa {rodada} de {tentativas}")
    entrada = int(input("Digite um número de 1 a 100: "))  
    if (entrada >  100 or entrada < 1): 
        print("VOCÊ NÃO SABE LER???? O valor digitado não é permitido")
        continue
    acerto = entrada ==  n_secreto
    numero_maior = entrada > n_secreto
    numero_menor = entrada < n_secreto

    
    #Digitar o número
    print(f"Você digitou o número: {entrada}")
    print("\n")

    #Condicional de acerto ou erro
    if (acerto):
        print("PARABÉNS!!!! Você acertou o número secreto")
        break
    else:
        if(numero_maior):
            print("O número digitado foi MAIOR do que o número secreto")
        if(numero_menor):
            print("O número digitado foi MENOR do que o número secreto")
    rodada = rodada + 1
print("\n")
print("GAME OVER!!!")