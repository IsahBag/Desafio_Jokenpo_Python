#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random

options = ["pedra", "papel", "tesoura"]
score = 0 
rounds_played = 0

while True:
    random_choice = random.choice(options)  # inicializa o adversário
    player_choice = input("Escolha pedra, papel ou tesoura: ")  # escolha do usuário

    # escolheu pedra:
    if player_choice == "pedra":
        rounds_played += 1
        if random_choice == "pedra":
            print("Empate!")
        elif random_choice == "papel":
            print("Você perdeu")
        elif random_choice == "tesoura":
            print("Você ganhou!")
            score += 1

    # escolheu papel: 
    elif player_choice == "papel":
        rounds_played += 1
        if random_choice == "papel":
            print("Empate!")
        elif random_choice == "tesoura":
            print("Você perdeu")
        elif random_choice == "pedra":
            print("Você ganhou!")
            score += 1
    
    # escolheu tesoura:
    elif player_choice == "tesoura":
        rounds_played += 1
        if random_choice == "tesoura":
            print("Empate!")
        elif random_choice == "pedra":
            print("Você perdeu")
        elif random_choice == "papel":
            print("Você ganhou!")
            score += 1

    # escolheu algo diferente de pedra, papel ou tesoura:
    else:
        play_again = input("Deseja jogar novamente? (s/n) ")
        if play_again == "s":
            continue
        elif play_again == "n":
            print(f"Você ganhou {score} vez(es), em {rounds_played} rodada(s) jogada(s)")    
            break       