# Listas principais usadas no sistema
jogadoras = [] # Armazena jogadoras cadastradas (nome, camisa, posição, time)
times = []     # Armazena os times cadastrados
partidas = []  # Armazena as partidas


# Função para validar se o valor digitado é um número (retorna inteiro)
def Veri_numero(msg):
    num = input(msg) # pede um valor
    while not num.isnumeric(): # enquanto não for número
        print("Só caracteres numéricos!")
        num = input(msg) # pede de novo
    return int(num)  # já retorna inteiro


# Função que mostra o menu principal
def Mostra_menu():
    print("\nSISTEMA DE CAMPEONATOS\n"
          "\n"
          "1.Gerenciar Times\n"
          "2.Gerenciar Jogadoras\n"
          "3.Gerenciar Partidas\n"
          "4.Relatórios\n"
          "5.Sair\n")
    return


# Função para gerenciar times
def GerenciaTime():
    while True: # fica em loop até escolher 3. para voltar ao menu principa
        print("\nGERENCIAMENTO DE TIMES\n"
              "1.Cadastrar novo time\n"
              "2.Listar times\n"
              "3.Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == "1": # cadastrar time
            CadastraTime()
        elif opcao == "2": # listar times
            ListaTime()
        elif opcao == "3": # voltar ao menu principal
            break
        else:  # opção inválida
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar time
def CadastraTime(): 
    nome = input("Digite o nome do time: ").strip()
    if not nome or nome.isnumeric(): # valida nome
        print("\nPor favor, insirá um nome válido para o time")
    else: 
        print(f"\nTime: {nome} cadastrado com sucesso!")
        times.append(nome) # adiciona o nome do time na lista de times


# Função para listar times
def ListaTime():
    print(f"\nTimes cadastrados:")
    for i, time in enumerate(times, start=1):  # percorre a lista de times
        print(f"{i}. {time}")  # printa cada time numerado
    return


# Função para gerenciar jogadoras
def GereciaJogadora():
    while True: # fica em loop até escolher voltar
        print("\nGERENCIAMENTO DE JOGADORAS\n"
              "1.Cadastrar jogadoras\n"
              "2.Listar Jogadoras\n"
              "3.Voltar para o menu principal")
        opcao = input("Escolha uma das opções: ")
        if opcao == "1": # cadastrar jogadora
            Cadastrajoga()
        elif opcao == "2": # listar jogadoras
            ListaJoga()
        elif opcao == "3":  # voltar ao menu principal
            break
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar jogadora
def Cadastrajoga():
    if len(times) == 0: # verifica se já existe time
        print("Necessário criar time primeiro")
        return
    else:
        print("Escolha um time")
        ListaTime()
        escolha = Veri_numero("Número do time: ")  # pede o número do time
        if escolha > 0 and escolha <= len(times):  # valida escolha
            time = times[escolha - 1] # pega o time selecionado
            print(f"Você escolheu o time: {time}")
            nome = input("Insirá nome da jogadora: ").strip()
            camisa = Veri_numero("Insirá número da camiseta: ")
            posicao = input("Posição da jogadora: ").strip()
            if not nome or nome.isnumeric():
                print("\nPor favor, insirá um nome válido para a jogadora")
            else:
                print("Jogadora Cadastrada!")
                print(f"Jogadora:{nome} | camisa:{camisa} | posição:{posicao}")
                jogadoras.append([nome, camisa, posicao, time])
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")
        return


# Função para listar jogadoras
def ListaJoga():
    if len(times) == 0:  # se não há times
        print("Necessário criar time primeiro")
        return
    elif len(jogadoras) == 0:  # se não há jogadoras
        print("Necessário cadastrar jogadoras")
        return
    else: 
        print(f"\nJogadoras cadastradas:")
        for i, j in enumerate(jogadoras, start=1): # percorre todas as jogadoras
            print(f"{i}. nome:{j[0]} | camisa:{j[1]} | posição:{j[2]} | time:{j[3]}") # mostra cada jogadora com suas informações
        return


# Função para gerenciar partidas
def GerenciaPartida(): # fica em loop até escolher 3. para voltar ao menu principa
    while True:
        print("\nGERENCIAMENTO DE PARTIDAS\n"
              "1. Cadastrar nova partida\n"
              "2. Listar partidas\n"
              "3. Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == "1": # cadastrar time
            CadastraPartida()
        elif opcao == "2": # listar times
            ListaPartida()
        elif opcao == "3": # voltar ao menu principal
            break
        else:  # opção inválida
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

    partidas.append({"time1": time1, "gols1": gols1, "time2": time2, "gols2": gols2})
    print(f"Partida registrada: {time1} {gols1} x {gols2} {time2}")


# Função para listar partidas
def ListaPartida():
    if len(partidas) == 0:
        print("Nenhuma partida registrada ainda.")
        return
    print("\nPartidas registradas:")
    for i, p in enumerate(partidas, start=1):
        print(f"{i}. {p['time1']} {p['gols1']} x {p['gols2']} {p['time2']}")

# Função para relatórios
# Função para relatórios
def Relatorio():
    while True:
        print("\nRELATÓRIOS\n"
              "1. Jogadoras por time\n"
              "2. Todas as partidas\n"
              "3. Classificação dos times\n"
              "4. Voltar ao menu principal")
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


# Relatório de jogadoras por time
def RelatorioJogadorasPorTime():
    if len(times) == 0:
        print("Nenhum time cadastrado.")
        return
    for time in times:
        print(f"\nTime: {time}")
        jogas = [j for j in jogadoras if j[3] == time]
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
    
    pontos = {time: 0 for time in times}

    # calcula pontos a partir das partidas
    for p in partidas:
        if p["gols1"] > p["gols2"]:
            pontos[p["time1"]] += 3
        elif p["gols1"] < p["gols2"]:
            pontos[p["time2"]] += 3
        else:
            pontos[p["time1"]] += 1
            pontos[p["time2"]] += 1
    
    print("\nCLASSIFICAÇÃO:")

    # transforma em lista de tuplas (time, pontos)
    tabela = list(pontos.items())

    # ordena manualmente (do maior para o menor)
    for i in range(len(tabela)):
        for j in range(i + 1, len(tabela)):
            if tabela[j][1] > tabela[i][1]:  # compara pontos
                tabela[i], tabela[j] = tabela[j], tabela[i]

    pos = 1
    for time, pts in tabela:
        print(f"{pos}º lugar: {time} - {pts} pontos")
        pos += 1


# Código principal
print("Bem-vindo(a) ao Passa a Bola!\n"
          "Sistema de organização de campeonatos")
print("-" * 40)
while True:
    Mostra_menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        GerenciaTime()
    elif escolha == "2":
        GereciaJogadora()
    elif escolha == "3":
        GerenciaPartida()
    elif escolha == "4":
        Relatorio()
    elif escolha == "5":
        print("Fim do sistema")
        break
    else:
        print("OPÇÃO INVÁLIDA! Tente novamente")
