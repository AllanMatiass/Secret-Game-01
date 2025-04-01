import random
import os

# Limpar o terminal
os.system('cls')

# Gerar número aleatório
aleatorio = random.randint(1000, 9999)
str_aleatorio = f'{aleatorio}'

d1 = aleatorio // 1000
atualizado = aleatorio % 1000
d2 = atualizado // 100
atualizado %= 100
d3 = atualizado // 10
d4 = atualizado % 10

continuar = 1
acertou = False

# Tela inicial
print("*********************************")
print("*       Jogo de Adivinhação     *")
print("*     Tente acertar o número   *")
print("*********************************")

print('Aperte "Enter" para continuar...')
input()

os.system('cls')
print(aleatorio)
# Início do jogo
while continuar == 1:

    chutes = 10
    while chutes > 0 and not acertou:

        print(f"Você tem {chutes} tentativas restantes.")

        # Definindo variáveis default
        n = int(input('Digite um numero inteiro de 4 dígitos: '))
        dica_apresentada = False
        tentativa = ''
        chutes -= 1
        resposta = f'{n}'
        dica = ''
        certos = 0
        errados = 0

        # Separando dígitos
        n1 = n // 1000
        n_atualizado = n % 1000

        n2 = n_atualizado // 100
        n_atualizado %= 100

        n3 = n_atualizado // 10

        n4 = n_atualizado % 10

        d1_correto = n1 == d1
        d2_correto = n2 == d2
        d3_correto = n3 == d3
        d4_correto = n4 == d4

        if resposta == str_aleatorio:
            os.system('cls')
            print(f'Parabéns! Você acertou restando {chutes} tentativas!')
            print(f'O código era: {aleatorio}')
            acertou = True

        else:
            if not d1_correto:
                tentativa += '_'

                if (n1 == d2 or n1 == d3 or n1 == d4):
                    errados += 1

                if chutes <= 5 and not dica_apresentada:
                    if d1 % 2 == 0:
                        dica = 'DICA: O primeiro dígito é par'

                    elif d1 < 5:
                        dica = 'DICA: O primeiro dígito é menor que 5'

                    dica_apresentada = True
                    os.system('cls')
                    print(dica)

            else:
                tentativa += f'{n1}'
                certos += 1

            if not d2_correto:
                tentativa += '_'

                if (n2 == d1 or n2 == d3 or n2 == d4):
                    errados += 1

                if chutes <= 5 and not dica_apresentada:
                    if d2 % 2 == 0:
                        dica = 'DICA: O segundo dígito é par'

                    elif d2 < 5:
                        dica = 'DICA: O segundo dígito é menor que 5'

                    dica_apresentada = True
                    os.system('cls')
                    print(dica)
            else:
                tentativa += f'{n2}'
                certos += 1

            if not d3_correto:
                tentativa += '_'
                if (n3 == d1 or n3 == d2 or n3 == d4):
                    errados += 1

                if chutes <= 5 and not dica_apresentada:
                    if d3 % 2 == 0:
                        dica = 'DICA: O terceiro dígito é par'

                    elif d3 < 5:
                        dica = 'DICA: O terceiro dígito é menor que 5'

                    dica_apresentada = True
                    os.system('cls')
                    print(dica)
            else:
                tentativa += f'{n3}'
                certos += 1

            if not d4_correto:
                tentativa += '_'
                if (n4 == d1 or n4 == d2 or n4 == d3):
                    errados += 1

                if chutes <= 5 and not dica_apresentada:
                    if d4 % 2 == 0:
                        dica = 'DICA: O quarto dígito é par'

                    elif d4 < 5:
                        dica = 'DICA: O quarto dígito é menor que 5'

                    dica_apresentada = True
                    os.system('cls')
                    print(dica)
            else:
                tentativa += f'{n4}'
                certos += 1

            print(f'Seu código: {tentativa}')
            print(f'Há {certos} números na posição certa')
            print(f'Há {errados} números na posição errada')

            if n > 9999 or n < 1000:
                os.system('cls')
                if chutes < 10:
                    chutes += 1

                print('Impossível realizar operação, '
                      'digite um número entre 1000 e 9999')

    continuar = int(input('Quer continuar? 1 = Sim: '))

    if continuar == 1:
        # Atualizando número aleatório
        aleatorio = random.randint(1000, 9999)
        str_aleatorio = f'{aleatorio}'

        d1 = aleatorio // 1000
        atualizado = aleatorio % 1000
        d2 = atualizado // 100
        atualizado %= 100
        d3 = atualizado // 10
        d4 = atualizado % 10

        chutes = 10
        acertou = False
        os.system('cls')
        print("*********************************")
        print("*       Jogo de Adivinhação     *")
        print("*     Tente acertar o número   *")
        print("*********************************")

        print('Aperte "Enter" para continuar...')
        input()

        os.system('cls')
