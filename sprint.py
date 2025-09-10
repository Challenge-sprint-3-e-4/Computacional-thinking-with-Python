#Listas principais usadas no sistema
jogadoras = [] # Armazena jogadoras cadastradas (nome, camisa, posição, time)
times = []  # Armazena os times cadastrados
partidas = [] # Armazena as partidas


# Função para validar se o valor digitado é um número
def Veri_numero(msg):
    num = input(msg) # pede um valor
    while not num.isnumeric(): # enquanto não for número
        print("Só caracteres númericos!")
        num = input(msg) # pede de novo
    return num # retorna o número como string

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
    while True: # fica em loop até escolher 3. para voltar ao menu principal
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
        else: # opção inválida
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar time
def CadastraTime():
    nome = input("Digite o nome do time: ")
    if len(nome) <= 0 or nome.isnumeric(): # valida nome
        print("\nPor favor, insirá o nome do time")
    else: 
        print(f"\nTime:{nome} cadastrado com sucesso!")
        times.append(nome) # adiciona o nome do time na lista de times


# Função para listar times
def ListaTime():
    print(f"\nTimes cadastrados:")
    s = 0
    for time in times: # percorre a lista de times
        s += 1
        print(f"{s}.{time}") # printa cada time numerado
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
        elif opcao == "3": # voltar ao menu principal
            break
        else: # opção inválida
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar jogadora
def Cadastrajoga():
    if len(times) == 0: # verifica se já existe time
        print("Necessario criar time primeiro")
        return
    else:
        print(f"Escolha um time")
        s = 0
        for i in times: # mostra todos os times disponíveis
            s += 1
            print(f"{s}.{i}")
        escolha = Veri_numero(f"Número do time: ") # pede o número do time
        escolha = int(escolha) # converte para inteiro
        if escolha > 0 and escolha <= len(times): # valida escolha
            time = times[escolha - 1] # pega o time selecionado
            print(f"Você escolheu o time:{time}")
            nome = input("Insirá nome da jogadora: ") 
            camisa = Veri_numero("Insirá número da camiseta: ")
            posicao = input("Posição da jogadora: ")
            if nome.isnumeric() or len(nome) <= 0: # valida nome
                print("\nPor favor, insirá o nome da jogadora")
            else:
                print("Jogadora Cadastrada!")
                print(f"Jogadora:{nome}|camisa:{camisa}|posição:{posicao}") 
                jogadoras.append([nome, camisa, posicao, time]) # adiciona jogadora à lista com nome, camisa, posição e time
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")
        return


# Função para listar jogadoras
def ListaJoga():
    if len(times) == 0: # se não há times
        print("Necessario criar time primeiro")
        return
    elif len(jogadoras) == 0: # se não há jogadoras
        print("Necessario cadastrar jogadoras")
        return
    else: 
        print(f"\nJogadoras cadastradas:")
        s = 0
        for i in jogadoras: # percorre todas as jogadoras
            s += 1
            print(f"{s}.nome:{i[0]}|camisa:{i[1]}|posição:{i[2]}|time:{i[3]}") # mostra cada jogadora com suas informações
        return


# Código principal
print("Bem-vindo(a) ao Passa a Bola!\n"
          "Sistema de organização de campeonatos")
print("-" * 40)
while True:
    Mostra_menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1": # gerenciamento de times
        GerenciaTime()
    elif escolha == "2": # gerenciamento de jogadoras
        GereciaJogadora()
    elif escolha == "3": # gerenciamento de partidas
        GerenciaPartida()
    elif escolha == "4": # relatórios
        Relatorio()
    elif escolha == "5": # sair
        print("Fim do sistema")
        break
    else: # opção inválida
        print("OPÇÃO INVÁLIDA! Tente novamente")

