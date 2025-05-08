import random

def jogo_adivinhacao():
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    
    # Inicia as tentativas
    tentativas = 0
    acertou = False
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    
    # Loop do jogo até o usuário acertar
    while not acertou:
        # Solicita ao usuário que digite um número
        palpite = input("Digite seu palpite: ")
        
        # Verifica se o valor inserido é válido
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue

        # Converte o palpite para um número inteiro
        palpite = int(palpite)
        
        # Incrementa as tentativas
        tentativas += 1
        
        # Compara o palpite com o número secreto
        if palpite < numero_secreto:
            print("O número é maior. Tente novamente!")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acertou = True  # Encerra o loop, já que o jogador acertou

# Chama a função para iniciar o jogo
jogo_adivinhacao()

