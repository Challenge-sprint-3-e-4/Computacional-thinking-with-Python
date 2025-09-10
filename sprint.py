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
    print("Sistema de campeonatos\n"
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
    if len(nome) == 0 or nome.isnumeric():
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
        break
    else:
        print("Opção inválida!")