# Listas principais usadas no sistema
jogadoras = []      # Armazena jogadoras cadastradas (nome, camisa, posição, time)
times = []          # Armazena os times cadastrados
vagas_goleira = []  # Vagas de goleira por time
vagas_defensora = []# Vagas de defensora por time
vagas_meio = []     # Vagas de meio por time
vagas_atacante = [] # Vagas de atacante por time
partidas = []       # Armazena as partidas

# Padrão de formação do time
PADRAO_GOLEIRA = 1
PADRAO_DEFENSORA = 2
PADRAO_MEIO = 2
PADRAO_ATACANTE = 2

# Senha de admin
senha_admin = "1234"


# Função para validar se o valor digitado é um número (retorna inteiro)
def Veri_numero(msg):
    num = input(msg) # pede um valor
    while not num.isnumeric(): # enquanto não for número
        print("Só caracteres numéricos!")
        num = input(msg) # pede de novo
    return int(num)  # já retorna inteiro


# Função para criar um novo time automaticamente
def CriarTimeAutomatico():
    nome = f"Time {len(times)+1}"  # nome do time sequencial
    times.append(nome)  # adiciona na lista de times
    vagas_goleira.append(PADRAO_GOLEIRA)  # define vagas iniciais
    vagas_defensora.append(PADRAO_DEFENSORA)
    vagas_meio.append(PADRAO_MEIO)
    vagas_atacante.append(PADRAO_ATACANTE)
    print(f"\nNovo {nome} criado automaticamente!")
    return len(times)-1  # retorna índice do time


# Função para inscrever jogadora
def Cadastrajoga():
    print("\n--- INSCRIÇÃO DE JOGADORA ---")
    nome = input("Insirá nome da jogadora: ")
    camisa = Veri_numero("Insirá número da camiseta: ")

    # Loop para garantir posição válida
    while True:
        print("Posições disponíveis: Goleira, Defensora, Meio, Atacante")
        posicao = input("Posição da jogadora: ")
        if posicao in ["Goleira", "Defensora", "Meio", "Atacante"]:
            break
        print("Posição inválida! Tente novamente.")

    # Tenta alocar jogadora em um time existente
    alocada = False
    for i in range(len(times)):
        if posicao == "Goleira" and vagas_goleira[i] > 0:
            vagas_goleira[i] -= 1
            jogadoras.append([nome, camisa, posicao, times[i]])
            print(f"Jogadora {nome} inscrita no {times[i]}!")
            alocada = True
            break
        elif posicao == "Defensora" and vagas_defensora[i] > 0:
            vagas_defensora[i] -= 1
            jogadoras.append([nome, camisa, posicao, times[i]])
            print(f"Jogadora {nome} inscrita no {times[i]}!")
            alocada = True
            break
        elif posicao == "Meio" and vagas_meio[i] > 0:
            vagas_meio[i] -= 1
            jogadoras.append([nome, camisa, posicao, times[i]])
            print(f"Jogadora {nome} inscrita no {times[i]}!")
            alocada = True
            break
        elif posicao == "Atacante" and vagas_atacante[i] > 0:
            vagas_atacante[i] -= 1
            jogadoras.append([nome, camisa, posicao, times[i]])
            print(f"Jogadora {nome} inscrita no {times[i]}!")
            alocada = True
            break

    # Se não conseguiu alocar em nenhum time existente, cria novo time
    if not alocada:
        i = CriarTimeAutomatico()
        if posicao == "Goleira":
            vagas_goleira[i] -= 1
        elif posicao == "Defensora":
            vagas_defensora[i] -= 1
        elif posicao == "Meio":
            vagas_meio[i] -= 1
        elif posicao == "Atacante":
            vagas_atacante[i] -= 1
        jogadoras.append([nome, camisa, posicao, times[i]])
        print(f"Jogadora {nome} inscrita no {times[i]}!")


# Função para listar times e suas jogadoras
def ListaTime():
    print(f"\nTimes cadastrados:")
    for i, time in enumerate(times, start=1):  # percorre a lista de times
        print(f"{i}. {time}")  # printa cada time numerado


def ListaTimesComJogadoras():
    if not times:
        print("Nenhum time formado ainda.")
        return
    for i, nome_time in enumerate(times):
        print(f"\n{nome_time} - Vagas restantes: G:{vagas_goleira[i]} D:{vagas_defensora[i]} M:{vagas_meio[i]} A:{vagas_atacante[i]}")
        jogas = [j for j in jogadoras if j[3] == nome_time]
        if jogas:
            for j in jogas:
                print(f"  - {j[0]} | Camisa {j[1]} | {j[2]}")
        else:
            print("  Nenhuma jogadora ainda.")


# Função para gerenciar partidas
def GerenciaPartida(): # fica em loop até escolher 3. para voltar ao menu principal
    while True:
        print("\nGERENCIAMENTO DE PARTIDAS\n"
              "1. Cadastrar nova Partida\n"
              "2. Listar Partidas\n"
              "3. Editar Partidas\n"
              "4. Remover Partidas\n"
              "5. Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            CadastraPartida()
        elif opcao == "2":
            ListaPartida()
        elif opcao == "3":
            EditarPertida()
        elif opcao == "4":
            RemoverPartida()
        elif opcao == "5":
            break
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar partida
def CadastraPartida():
    if len(times) < 2:
        print("É necessário ter pelo menos 2 times cadastrados.")
        return

    print("\nTimes disponíveis:")
    ListaTime()

    t1 = Veri_numero("Digite o número do 1º time: ")
    t2 = Veri_numero("Digite o número do 2º time: ")

    if t1 <= 0 or t1 > len(times) or t2 <= 0 or t2 > len(times) or t1 == t2:
        print("Escolha inválida de times!")
        return

    time1 = times[t1 - 1]
    time2 = times[t2 - 1]

    gols1 = Veri_numero(f"Gols do {time1}: ")
    gols2 = Veri_numero(f"Gols do {time2}: ")

    partidas.append([time1, gols1, time2, gols2])
    print(f"Partida registrada: {time1} {gols1} x {gols2} {time2}")


# Função para listar partidas
def ListaPartida():
    if len(partidas) == 0:
        print("Nenhuma partida registrada ainda.")
        return
    print("\nPartidas registradas:")
    for i, p in enumerate(partidas, start=1):
        print(f"{i}. {p[0]} {p[1]} x {p[3]} {p[2]}")

# Função De editar prtidas
def EditarPertida():
    if len(partidas) <= 0:
        print("Nenhuma partida cadastrada")
        return
    print("Editar Partidas")
    ListaPartida()
    num = Veri_numero("\nQual partida deseja editar?\n->")
    if num <= 0 or num > len(partidas):
        print("Número inválido")
        return
    partida = partidas[num - 1]
    print(f"\nPartida atual: {partida[0]} {partida[1]} x {partida[3]} {partida[2]}")

    print("\nDigite os novos placares:")
    novo_gols1 = Veri_numero(f"Gols do {partida[0]}: ")
    novo_gols2 = Veri_numero(f"Gols do {partida[2]}: ")

    partidas[num - 1][1] = novo_gols1
    partidas[num - 1][3] = novo_gols2

    print(f"Partida atualizada: {partida[0]} {novo_gols1} x {novo_gols2} {partida[2]}")
#Função para remover partidas:
def RemoverPartida():
    if len(partidas) == 0:
        print("Nenhma partida cadastrada")
        return
    print("Remover Partida")
    ListaPartida()
    num = Veri_numero("\nQual partida você deseja cancelar?\n->")
    if num <= 0 or num > len(partidas):
        print("Número inválido")
        return
    partida = partidas[num - 1]
    print(f"\nVocê irá cancelar: {partida[0]} {partida[1]} x {partida[3]} {partida[2]}")
    confirmar = input("Tem certeza? (s/n)\n->")
    if confirmar == "s":
        partidas.pop(num-1)
        print("Partida Cancelada!")
    else:
        print("Opção cancelada")


# Relatório de jogadoras por time
def RelatorioJogadorasPorTime():
    if len(times) == 0:
        print("Nenhum time cadastrado.")
        return
    for i, nome_time in enumerate(times):
        print(f"\nTime: {nome_time}")
        jogas = [j for j in jogadoras if j[3] == nome_time]
        if len(jogas) == 0:
            print("  Nenhuma jogadora cadastrada.")
        else:
            for j in jogas:
                print(f"  - {j[0]} | Camisa {j[1]} | {j[2]}")


# Relatório de Classificação dos times
def Classificacao():
    if len(partidas) == 0:
        print("Nenhuma partida registrada para gerar classificação.")
        return

    pontos = [0]*len(times)

    # calcula pontos a partir das partidas
    for p in partidas:
        i1 = times.index(p[0])
        i2 = times.index(p[2])
        if p[1] > p[3]:
            pontos[i1] += 3
        elif p[1] < p[3]:
            pontos[i2] += 3
        else:
            pontos[i1] += 1
            pontos[i2] += 1

    # gera ranking
    ranking = list(zip(times, pontos))
    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\nCLASSIFICAÇÃO:")
    for pos, (time, pts) in enumerate(ranking, start=1):
        print(f"{pos}º lugar: {time} - {pts} pontos")


# Função para relatórios
def Relatorio():
    while True:
        print("\nRELATÓRIOS\n"
              "1. Jogadoras por time\n"
              "2. Todas as partidas\n"
              "3. Classificação dos times\n"
              "4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            RelatorioJogadorasPorTime()
        elif opcao == "2":
            ListaPartida()
        elif opcao == "3":
            Classificacao()
        elif opcao == "4":
            break
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")

#Função para gerenciar jogadoras
def GerenciaJogadoras():
    while True:
        print("Gerenciamento de Jogadoras")
        print("1. Editar Jogadoras\n"
              "2. Remover Jogadoras\n"
              "3. Voltar")
        opcao = input("Escolha uma das opções: ")
        if opcao == "1":
            EditarJogadoras()
        elif opcao == "2":
            RemoverJogadoras()
        elif opcao == "3":
            break
        else:
            print("Opção inválida")

# Função de editar jogadoras
def EditarJogadoras():
    if len(jogadoras) <= 0:
        print("Nenhuma jogadora cadastrada")
    if len(times) <= 0:
        print("Nenhum Time cadastrado")
    while True:
        print("\nEditar Jogadoras")
        print("\nJogadoras cadastradas:")
        for i, jog in enumerate(jogadoras, start=1):
            print(f"{i}. {jog[0]} | Camisa {jog[1]} | {jog[2]} | {jog[3]}")
        num = Veri_numero("Qual jogadora deseja editar?\n->")
        if num <= 0 or num > len(jogadoras):
            print("Número inválido")
            return
        print("\nO que deseja alterar?"
              "\n1.Nome"
              "\n2.Número da camisa"
              "\n3.Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            novo_nome = input("Insirá novo nome: ")
            jogadoras[num - 1][0] = novo_nome
            print(f"Nome atualizado!"
                  f"\nNovo nome: {novo_nome}")
        elif opcao == "2":
            nova_camisa = input("Insirá novo número de camisa: ")
            jogadoras[num - 1][1] = nova_camisa
            print(f"Número atualizado"
                  f"\nNovo número de camisa: {nova_camisa}")
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

#Função para remover jogadoras
def RemoverJogadoras():
    if len(jogadoras) == 0:
        print("Nenhuma jogadora cadastrada.")
        return

    print("\n--- REMOVER JOGADORA ---")
    print("\nJogadoras cadastradas:")
    for i, jog in enumerate(jogadoras, start=1):
        print(f"{i}. {jog[0]} | Camisa {jog[1]} | {jog[2]} | {jog[3]}")

    num = Veri_numero("\nQual jogadora deseja remover?")

    if num == 0:
        return
    if num <= 0 or num > len(jogadoras):
        print("Número inválido!")
        return

    jogadora = jogadoras[num - 1]
    nome = jogadora[0]
    posicao = jogadora[2]
    time = jogadora[3]

    print(f"\nVocê vai remover: {nome} ({posicao}) do {time}")
    confirma = input("Tem certeza? (s/n): ")

    if confirma.lower() != 's':
        print("Operação cancelada.")
        return
    indice_time = times.index(time)
    if posicao == "Goleira":
        vagas_goleira[indice_time] += 1
    elif posicao == "Defensora":
        vagas_defensora[indice_time] += 1
    elif posicao == "Meio":
        vagas_meio[indice_time] += 1
    elif posicao == "Atacante":
        vagas_atacante[indice_time] += 1

    jogadoras.pop(num - 1)
    print(f"Jogadora {nome} removida com sucesso!")

# Código principal
print("Bem-vindo(a) ao Passa a Bola!\nSistema de organização de campeonatos")
print("-"*40)

while True:
    usuario = input("Você é (1) Admin ou (2) Jogadora? ")

    if usuario == "1":  # Admin
        senha = input("Digite a senha de administrador: ")
        if senha != senha_admin:
            print("Senha incorreta! Programa encerrado.")
            break
        else:
            while True:
                print("\nMENU ADMIN\n"
                      "1. Listar times e jogadoras\n"
                      "2. Gerenciar partidas\n"
                      "3. Gerenciar Jogadoras\n"
                      "4. Relatórios\n"
                      "5. Sair")
                opcao = input("Escolha: ")
                if opcao == "1":
                    ListaTimesComJogadoras()
                elif opcao == "2":
                    GerenciaPartida()
                elif opcao == "3":
                    GerenciaJogadoras()
                elif opcao == "4":
                    Relatorio()
                elif opcao == "5":
                    print("Fim do sistema (Admin)")
                    break
                else:
                    print("Opção inválida!")
            break  # encerra o programa depois que Admin sai

    elif usuario == "2":  # Jogadora
        while True:
            print("\nMENU JOGADORA\n"
                  "1. Fazer inscrição\n"
                  "2. Sair")
            opcao = input("Escolha: ")
            if opcao == "1":
                Cadastrajoga()
            elif opcao == "2":
                print("Fim do sistema (Jogadora)")
                break
            else:
                print("Opção inválida!")

    else:
        print("Opção inválida! Programa encerrado.")
        break
