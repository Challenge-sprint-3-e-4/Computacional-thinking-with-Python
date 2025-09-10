jogadoras = []
times = []
partidas = []


def Veri_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Só caracteres númericos!")
        num = input(msg)
    return num

def Mostra_menu():
    print("\nSISTEMA DE CAMPEONATOS\n"
          "\n"
          "1.Gerenciar Times\n"
          "2.Gerenciar Jogadoras\n"
          "3.Gerenciar Partidas\n"
          "4.Relatórios\n"
          "5.Sair\n")
    return

def GerenciaTime():
    while True:
        print("\nGERENCIAMENTO DE TIMES\n"
              "1.Cadastrar novo time\n"
              "2.Listar times\n"
              "3.Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            CadastraTime()
        elif opcao == "2":
            ListaTime()
        elif opcao == "3":
            break
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")

def CadastraTime():
    nome = input("Digite o nome do time: ")
    if len(nome) <= 0 or nome.isnumeric():
        print("\nPor favor, insirá o nome do time")
    else:
        print(f"\nTime:{nome} cadastrado com sucesso!")
        times.append(nome)

def ListaTime():
    print(f"\nTimes cadastrados:")
    s = 0
    for time in times:
        s += 1
        print(f"{s}.{time}")
    return

def GereciaJogadora():
    while True:
        print("\nGERENCIAMENTO DE JOGADORAS\n"
              "1.Cadastrar jogadoras\n"
              "2.Listar Jogadoras\n"
              "3.Voltar para o menu principal")
        opcao = input("Escolha uma das opções: ")
        if opcao == "1":
            Cadastrajoga()
        elif opcao == "2":
            ListaJoga()
        elif opcao == "3":
            break
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")


def Cadastrajoga():
    if len(times) == 0:
        print("Necessario criar time primeiro")
        return
    else:
        print(f"Escolha um time")
        s = 0
        for i in times:
            s += 1
            print(f"{s}.{i}")
        escolha = int(input(f"Número do time: "))
        if escolha > 0 and escolha <= len(times):
            time = times[escolha - 1]
            print(f"Você escolheu o time:{time}")
            nome = input("Insirá nome da jogadora: ")
            camisa = Veri_numero("Insirá número da camiseta: ")
            posicao = input("Posição da jogadora: ")
            if nome.isnumeric() or len(nome) <= 0:
                print("\nPor favor, insirá o nome da jogadora")
            else:
                print("Jogadora Cadastrada!")
                print(f"Jogadora:{nome}|camisa:{camisa}|posição:{posicao}")
                jogadoras.append([nome, camisa, posicao, time])
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")
        return  

def ListaJoga():
    if len(times) == 0:
        print("Necessario criar time primeiro")
        return
    else:
        print(f"\nJogadoras cadastradas:")
        s = 0
        for i in jogadoras:
            s += 1
            print(f"{s}.{i[0]},{i[1]},{i[2]},{i[3]}")
        return



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

