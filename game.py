#BATALHA
import random
import os

#Setup do jogador
vida_max = 100
vida_heroi = vida_max
nivel = 1
xp = 0
prox_niv = nivel * 100
ouro = 0
h_atk_min = 10
h_atk_max = 20
loja = False

#Verficação de save
if os.path.exists("save.txt"):
    res = input("Um save foi encontrado. Deseja carrega-lo? (s, n)\n")
    if res.lower() == 's':
        with open("save.txt", 'r') as save:
            status = save.readline()
            status = status.split(',')
            vida_heroi = int(status[0])
            nivel = int(status[1])
            xp = int(status[2])
            ouro = int(status[3])
            h_atk_max, h_atk_min = int(status[4]), int(status[5])
    else:
        pass

#Setup dos inimigos
lista_monstros = [
     {'nome': 'Orc', 'vida': 80, 'atk_min': 5, 'atk_max': 15, 'xp': 75, 'ouro': 100},
     {'nome': 'Esqueleto', 'vida': 60, 'atk_min': 4, 'atk_max': 12, 'xp': 50, 'ouro': 75},
     {'nome': 'Bebê Dragão', 'vida': 120, 'atk_min': 8, 'atk_max': 18, 'xp': 120, 'ouro': 200},
     {'nome': 'Necromante', 'vida': 100, 'atk_min': 6, 'atk_max': 16, 'xp': 100, 'ouro': 150},
     {'nome': 'Zumbi', 'vida': 70, 'atk_min': 5, 'atk_max': 15, 'xp': 70, 'ouro': 90}
]
monstro = random.choice(lista_monstros)
monstro_id = monstro['nome']
vida_monstro = monstro['vida']
atk_min = monstro['atk_min']
atk_max = monstro['atk_max']
Mxp = monstro['xp']

#Loop do Jogo
while True:
    monstro = random.choice(lista_monstros)
    vida_monstro = monstro['vida']
    
    print(f"Oh não, um {monstro['nome']} apareceu!")
    while vida_monstro > 0 and vida_heroi > 0:
        print("-----------------")
        print("Você pode:\n [1] - Atacar;\n [2] - Defender;\n [3] - Fugir.")
        acao = (input("O que você vai fazer?\n"))
        #Checagem da ação do jogador
        if acao == '1':
            dano = random.randint(h_atk_min, h_atk_max)
            vida_monstro -= dano
            print(f"Você causou {dano} pontos de dano!")
            
        elif acao == '2':
            print("Você reduziu o dano recebido")
        elif acao == '3':
                print("Você fugiu da batalha")
                break
        else:
                print("Ação Inválida")
                continue
        #Mecânica do mostro (dano e defesa)
        if vida_monstro > 0:
            dano_monstro = random.randint(monstro['atk_min'], monstro['atk_max'])
            if acao == '2':
                dano_monstro = dano_monstro // 2
            vida_heroi -= dano_monstro
            print(f"O monstro causou {dano_monstro} pontos de dano")
        
        print('-' * 5)
        print("Fim do turno!")
        print(f"\nSua vida: {vida_heroi}")
        print(f"Vida do monstro: {vida_monstro}")

    #Condição de vitório ou derrota
    if vida_monstro <= 0:
        print("Você derrotou o monstro. Parabéns!")
        xp += monstro['xp']
        print(f"Você ganhou {monstro['xp']} pontos de xp. Seu xp atual: {xp}/{prox_niv}")
        ouro += monstro['ouro']
        print(f"Você recebeu {monstro['ouro']} de ouro")
        #PPB (Processamento Pós Batalha)
        if xp >= prox_niv:
            nivel += 1
            xp = xp - prox_niv
            prox_niv = nivel * 100
            vida_max += 20
            vida_heroi = vida_max
            h_atk_min += 2
            h_atk_max += 2
            print(f"Você subiu de nível! Seu nível atual é {nivel}")
        resposta = input("Deseja ir para a loja? s/n\n")
        if resposta.lower() == 's':
            loja = True

            while(loja):
                print(f"Ouro: {ouro}")
                print("Itens disponíveis:\n[1] - Cura (100)\n[2] - Melhoria de espada(150)\n[3] - Sair")
                decisao = input("::")
                if decisao.lower() in ['cura', '1']:
                    if ouro >= 100:
                        vida_heroi += 40
                        if vida_heroi > vida_max:
                            vida_heroi = vida_max
                        print(f"Sua vida foi regenerada!\nSua vida atual é {vida_heroi}")
                        ouro -= 100
                    else:
                        print("Ouro insuficiente")
                elif decisao.lower() in ['melhoria', '2']:
                    if ouro >= 150:
                        print(f"Você melhorou sua espada!")
                        h_atk_max += 2
                        h_atk_min += 2
                        ouro -= 150
                    else:
                        print("Ouro insuficiente")
                elif decisao.lower() in ['sair', '3']:
                    loja = False
                    
    elif vida_heroi <= 0:
         print("\nVocê foi derrotado.\nTente novamente!")
         break
     

    continuar = input("Deseja continuar? s/n\n")
    if continuar.lower() != 's':
        with open("save.txt", 'w', encoding="utf-8") as save:
            save.write(f"{vida_heroi}, {nivel}, {xp}, {ouro}, {h_atk_max}, {h_atk_min}")
        break
    else:
        continue