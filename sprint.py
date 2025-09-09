jogadoras = []
times = []
partidas = []

def Mostra_menu():
    print("Sistema de campeonatos\n"
          "\n"
          "1.Gerenciar Times\n"
          "2.Gerenciar Jogadoras\n"
          "3.Gerenciar Partidas\n"
          "4.Relatórios\n"
          "5.Sair\n")
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