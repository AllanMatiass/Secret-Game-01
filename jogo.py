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
atualizado = atualizado % 100
d3 = atualizado // 10
d4 = atualizado % 10

continuar = 1
acertou = False

# Tela inicial
print("*********************************")
print("*       Jogo de Adivinhação     *")
print("*     Tente acertar o número    *")
print("*********************************")

print('Aperte "Enter" para continuar...')
input()

os.system('cls')

# Início do jogo
while continuar == 1:
    digito_correto_1 = ''
    digito_correto_2 = ''
    digito_correto_3 = ''
    digito_correto_4 = ''
    chutes = 10
    while chutes > 0 and not acertou:

        print(f"Você tem {chutes} tentativas restantes.")

        n = int(input('Digite um número inteiro de 4 dígitos: '))
        dica_apresentada = False
        chutes -= 1
        resposta = f'{n}'
        dica = ''
        certos = 0
        errados = 0

        if n < 1000 or n > 9999:
            os.system('cls')
            if chutes < 10:
                chutes += 1
            print('Impossível realizar operação,'
                  ' digite um número entre 1000 e 9999')
            input('Aperte Enter para tentar novamente...')
            os.system('cls')

        else:
            # Separando os dígitos
            n1 = n // 1000
            n_atualizado = n % 1000
            n2 = n_atualizado // 100
            n_atualizado = n_atualizado % 100
            n3 = n_atualizado // 10
            n4 = n_atualizado % 10

            if resposta == str_aleatorio:
                os.system('cls')
                print(f'Parabéns! Você acertou restando {chutes} tentativas!')
                print(f'O código era: {aleatorio}')
                acertou = True

            else:
                # Dígito 1
                if n1 == d1:
                    if digito_correto_1 != f'{d1}':
                        digito_correto_1 = f'{n1}'
                        certos += 1
                else:
                    if chutes <= 5 and not dica_apresentada:
                        if d1 % 2 == 0:
                            digito_correto_1 = '(par)'
                            dica = 'DICA: O primeiro dígito é par'

                        elif d1 < 5:
                            digito_correto_1 = '(<5)'
                            dica = 'DICA: O primeiro dígito é menor que 5'

                        else:
                            digito_correto_1 = '_'
                        dica_apresentada = True
                        os.system('cls')
                        print(dica)

                    elif digito_correto_1 != f'{d1}':
                        digito_correto_1 = '_'

                    if n1 == d2 or n1 == d3 or n1 == d4:
                        errados += 1

                # Dígito 2
                if n2 == d2:
                    if digito_correto_2 != f'{d2}':
                        digito_correto_2 = f'{n2}'
                        certos += 1
                else:
                    if chutes <= 5 and not dica_apresentada:
                        if d2 % 2 == 0:
                            digito_correto_2 = '(par)'
                            dica = 'DICA: O segundo dígito é par'

                        elif d2 < 5:
                            digito_correto_2 = '(<5)'
                            dica = 'DICA: O segundo dígito é menor que 5'

                        else:
                            digito_correto_2 = '_'
                        dica_apresentada = True
                        os.system('cls')
                        print(dica)

                    elif digito_correto_2 != f'{d2}':
                        digito_correto_2 = '_'

                    if n2 == d1 or n2 == d3 or n2 == d4:
                        errados += 1

                # Dígito 3
                if n3 == d3:
                    if digito_correto_3 != f'{d3}':
                        digito_correto_3 = f'{n3}'
                        certos += 1
                else:
                    if chutes <= 5 and not dica_apresentada:
                        if d3 % 2 == 0:
                            digito_correto_3 = '(par)'
                            dica = 'DICA: O terceiro dígito é par'

                        elif d3 < 5:
                            digito_correto_3 = '(<5)'
                            dica = 'DICA: O terceiro dígito é menor que 5'

                        else:
                            digito_correto_3 = '_'
                        dica_apresentada = True
                        os.system('cls')
                        print(dica)

                    elif digito_correto_3 != f'{d3}':
                        digito_correto_3 = '_'

                    if n3 == d1 or n3 == d2 or n3 == d4:
                        errados += 1

                # Dígito 4
                if n4 == d4:
                    if digito_correto_4 != f'{d4}':
                        digito_correto_4 = f'{n4}'
                        certos += 1
                else:
                    if chutes <= 5 and not dica_apresentada:
                        if d4 % 2 == 0:
                            digito_correto_4 = '(par)'
                            dica = 'DICA: O quarto dígito é par'

                        elif d4 < 5:
                            digito_correto_4 = '(<5)'
                            dica = 'DICA: O quarto dígito é menor que 5'

                        else:
                            digito_correto_4 = '_'
                        dica_apresentada = True
                        os.system('cls')
                        print(dica)

                    elif digito_correto_4 != f'{d4}':
                        digito_correto_4 = '_'

                    if n4 == d1 or n4 == d2 or n4 == d3:
                        errados += 1

                tentativa = f'{digito_correto_1}{digito_correto_2}{digito_correto_3}{digito_correto_4}'
                print(f'Seu código: {tentativa}')
                print(f'Você acertou {certos} números dessa vez')
                print(f'Há {errados} números na posição errada')

        if chutes == 0 and not acertou:
            print('Você perdeu! O código secreto era:', aleatorio)

    continuar = int(input('Quer continuar? 1 = Sim: '))

    if continuar == 1:
        aleatorio = random.randint(1000, 9999)
        str_aleatorio = f'{aleatorio}'

        d1 = aleatorio // 1000
        atualizado = aleatorio % 1000
        d2 = atualizado // 100
        atualizado = atualizado % 100
        d3 = atualizado // 10
        d4 = atualizado % 10

        chutes = 10
        acertou = False
        os.system('cls')
        print("*********************************")
        print("*       Jogo de Adivinhação     *")
        print("*     Tente acertar o número    *")
        print("*********************************")
        print('Aperte "Enter" para continuar...')
        input()
        os.system('cls')
