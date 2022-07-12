import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

imagens_jogo = [pedra, papel, tesoura]

escolha_usuario = int(input("\nO que voce escolhe. 0 - Pedra, 1 - Papel ou 2 - Tesoura:"))
print(imagens_jogo[escolha_usuario])

if escolha_usuario >= 3 or escolha_usuario < 0:
    print("Voce digitou um numero errado, voce perdeu!")
else:
    escolha_computador = random.randint(0, 2)
    print("Computador escolheu:")
    print(imagens_jogo[escolha_computador])

    if escolha_usuario == 0 and escolha_computador == 2:
        print("Voce ganhou")
    elif escolha_usuario == escolha_computador:
        print("Empate!")
    elif escolha_usuario == 2 and escolha_computador == 0:
        print("Voce perdeu!")
    elif escolha_usuario > escolha_computador:
        print("Voce ganhou!")
    elif escolha_computador > escolha_usuario:
        print("Computador ganhou!")
