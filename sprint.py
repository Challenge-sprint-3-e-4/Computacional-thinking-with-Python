import json

# ===== DECLARAÇÃO DE VARIÁVEIS GLOBAIS =====
# Listas principais usadas no sistema
jogadoras = []  # Armazena jogadoras cadastradas (nome, camisa, posição, time)
times = []  # Armazena os times cadastrados
vagas_goleira = []  # Vagas de goleira por time
vagas_defensora = []  # Vagas de defensora por time
vagas_meio = []  # Vagas de meio por time
vagas_atacante = []  # Vagas de atacante por time
partidas = []  # Armazena as partidas

# Padrão de formação do time (quantas jogadoras de cada posição)
PADRAO_GOLEIRA = 1
PADRAO_DEFENSORA = 2
PADRAO_MEIO = 2
PADRAO_ATACANTE = 2

# Senha de admin (usado para autenticação)
senha_admin = "1234"


# ===== FUNÇÕES DE PERSISTÊNCIA DE DADOS =====

# Função para salvar os dados do código em arquivo JSON
def SalvarDados():
    # Cria um dicionário com todas as estruturas de dados do sistema
    dados = {
        'Jogadoras': jogadoras,
        'Times': times,
        'Vagas_goleira': vagas_goleira,
        'Vagas_defensora': vagas_defensora,
        'Vagas_meio': vagas_meio,
        'Vagas_Atacantes': vagas_atacante,
        'Partidas': partidas,
    }
    try:
        # Abre arquivo em modo escrita ('w') com codificação UTF-8
        with open('campeonato.json', 'w', encoding='utf-8') as arquivo:
            # Converte o dicionário em JSON e salva no arquivo
            # indent=2 deixa o JSON formatado e legível
            # ensure_ascii=False permite caracteres especiais (acentos)
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
        print("Dados salvos com sucesso!")
        return True
    except Exception as erro:
        # Captura qualquer erro durante a gravação
        print(f"Erro ao salvar dados: {erro} ")
        return False


# Função para carregar todos os dados do arquivo JSON
def CarregarDados():
    # 'global' permite modificar as variáveis globais dentro da função
    global jogadoras, times, partidas
    global vagas_goleira, vagas_defensora, vagas_meio, vagas_atacante

    try:
        # Abre arquivo em modo leitura ('r') com codificação UTF-8
        with open('campeonato.json', 'r', encoding='utf-8') as arquivo:
            # Lê e converte o JSON de volta para dicionário Python
            dados = json.load(arquivo)

        # Carrega cada estrutura de dados do dicionário
        # .get() retorna lista vazia [] se a chave não existir
        jogadoras = dados.get('Jogadoras', [])
        times = dados.get('Times', [])
        partidas = dados.get('Partidas', [])
        vagas_goleira = dados.get('Vagas_goleira', [])
        vagas_defensora = dados.get('Vagas_defensora', [])
        vagas_meio = dados.get('Vagas_meio', [])
        vagas_atacante = dados.get('Vagas_Atacante', [])

        # Exibe resumo dos dados carregados
        print("✓ Dados carregados com sucesso!")
        print(f"   → {len(jogadoras)} jogadoras")
        print(f"   → {len(times)} times")
        print(f"   → {len(partidas)} partidas")
        return True

    except FileNotFoundError:
        # Arquivo não existe (primeira execução do programa)
        print("Nenhum dado salvo encontrado")
        return False
    except json.JSONDecodeError:
        # Arquivo JSON está mal formatado ou corrompido
        print("Erro: arquivo corrompido!")
        return False
    except Exception as erro:
        # Qualquer outro erro não previsto
        print(f"Erro ao carregar: {erro}")
        return False


# ===== FUNÇÕES AUXILIARES =====

# Função para validar se o valor digitado é um número (retorna inteiro)
def Veri_numero(msg):
    while True:  # Loop infinito até o usuário digitar um número válido
        try:
            # Tenta converter a entrada para inteiro
            num = int(input(msg))
            break  # Se conseguir, sai do loop
        except ValueError:
            # Erro quando o usuário digita texto em vez de número
            print("Somente caracteres númericos")
        except Exception as e:
            # Qualquer outro erro não previsto
            print(e)
    return num  # FALTAVA ESSE RETURN! Sem ele a função não devolve o número


# ===== FUNÇÕES DE GERENCIAMENTO DE TIMES =====

# Função para criar um novo time automaticamente
def CriarTimeAutomatico():
    # Gera nome sequencial: "Time 1", "Time 2", etc.
    nome = f"Time {len(times) + 1}"

    # Adiciona o time na lista principal
    times.append(nome)

    # Inicializa as vagas de cada posição seguindo o padrão definido
    vagas_goleira.append(PADRAO_GOLEIRA)
    vagas_defensora.append(PADRAO_DEFENSORA)
    vagas_meio.append(PADRAO_MEIO)
    vagas_atacante.append(PADRAO_ATACANTE)

    print(f"\nNovo {nome} criado automaticamente!")

    # Retorna o índice do time recém-criado
    return len(times) - 1


# ===== FUNÇÕES DE GERENCIAMENTO DE JOGADORAS =====

# Função para inscrever jogadora
def Cadastrajoga():
    print("\n--- INSCRIÇÃO DE JOGADORA ---")

    # Coleta dados básicos da jogadora
    nome = input("Insirá nome da jogadora: ")
    camisa = Veri_numero("Insirá número da camiseta: ")

    # Loop para garantir posição válida
    while True:
        print("Posições disponíveis: Goleira, Defensora, Meio, Atacante")
        posicao = input("Posição da jogadora: ")
        # Verifica se a posição digitada é válida
        if posicao in ["Goleira", "Defensora", "Meio", "Atacante"]:
            break  # Sai do loop se a posição for válida
        print("Posição inválida! Tente novamente.")

    # Tenta alocar jogadora em um time existente que tenha vaga
    alocada = False  # Flag para controlar se conseguiu alocar

    # Percorre todos os times existentes
    for i in range(len(times)):
        # Verifica se há vaga para a posição escolhida no time atual
        if posicao == "Goleira" and vagas_goleira[i] > 0:
            vagas_goleira[i] -= 1  # Reduz uma vaga
            jogadoras.append([nome, camisa, posicao, times[i]])  # Adiciona jogadora
            print(f"Jogadora {nome} inscrita no {times[i]}!")
            alocada = True
            break  # Sai do loop, já alocou
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
        i = CriarTimeAutomatico()  # Cria time e retorna seu índice

        # Reduz a vaga correspondente no novo time
        if posicao == "Goleira":
            vagas_goleira[i] -= 1
        elif posicao == "Defensora":
            vagas_defensora[i] -= 1
        elif posicao == "Meio":
            vagas_meio[i] -= 1
        elif posicao == "Atacante":
            vagas_atacante[i] -= 1

        # Adiciona a jogadora no novo time
        jogadoras.append([nome, camisa, posicao, times[i]])
        print(f"Jogadora {nome} inscrita no {times[i]}!")


# ===== FUNÇÕES DE LISTAGEM =====

# Função para listar times de forma simples (apenas nomes)
def ListaTime():
    print(f"\nTimes cadastrados:")
    # enumerate() retorna índice e valor, start=1 começa a contagem em 1
    for i, time in enumerate(times, start=1):
        print(f"{i}. {time}")


# Função para listar times com suas jogadoras e vagas restantes
def ListaTimesComJogadoras():
    if not times:  # Se a lista de times estiver vazia
        print("Nenhum time formado ainda.")
        return

    # Percorre cada time usando índice (para acessar as vagas)
    for i, nome_time in enumerate(times):
        # Mostra o time e suas vagas disponíveis
        print(
            f"\n{nome_time} - Vagas restantes: G:{vagas_goleira[i]} D:{vagas_defensora[i]} M:{vagas_meio[i]} A:{vagas_atacante[i]}")

        # List comprehension: filtra jogadoras que pertencem a este time
        # j é cada jogadora, j[3] é o time dela
        jogas = [j for j in jogadoras if j[3] == nome_time]

        if jogas:  # Se encontrou jogadoras
            for j in jogas:
                # j[0]=nome, j[1]=camisa, j[2]=posição
                print(f"  - {j[0]} | Camisa {j[1]} | {j[2]}")
        else:
            print("  Nenhuma jogadora ainda.")


# ===== FUNÇÕES DE GERENCIAMENTO DE PARTIDAS =====

# Função para gerenciar partidas (menu com subopções)
def GerenciaPartida():
    while True:  # Loop do menu até escolher voltar
        print("\nGERENCIAMENTO DE PARTIDAS\n"
              "1. Cadastrar nova Partida\n"
              "2. Listar Partidas\n"
              "3. Editar Partidas\n"
              "4. Remover Partidas\n"
              "5. Voltar para o menu principal")
        opcao = input("Escolha uma opção: ")

        # Chama a função correspondente à opção escolhida
        if opcao == "1":
            CadastraPartida()
        elif opcao == "2":
            ListaPartida()
        elif opcao == "3":
            EditarPertida()
        elif opcao == "4":
            RemoverPartida()
        elif opcao == "5":
            break  # Sai do loop e retorna ao menu anterior
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para cadastrar partida
def CadastraPartida():
    # Verifica se há pelo menos 2 times para realizar uma partida
    if len(times) < 2:
        print("É necessário ter pelo menos 2 times cadastrados.")
        return

    print("\nTimes disponíveis:")
    ListaTime()  # Mostra lista de times

    # Solicita escolha dos dois times
    t1 = Veri_numero("Digite o número do 1º time: ")
    t2 = Veri_numero("Digite o número do 2º time: ")

    # Valida se as escolhas são válidas
    # - números devem estar entre 1 e len(times)
    # - times devem ser diferentes (t1 != t2)
    if t1 <= 0 or t1 > len(times) or t2 <= 0 or t2 > len(times) or t1 == t2:
        print("Escolha inválida de times!")
        return

    # Converte número escolhido para nome do time (índice começa em 0)
    time1 = times[t1 - 1]
    time2 = times[t2 - 1]

    # Solicita os gols de cada time
    gols1 = Veri_numero(f"Gols do {time1}: ")
    gols2 = Veri_numero(f"Gols do {time2}: ")

    # Adiciona partida na lista: [time1, gols1, time2, gols2]
    partidas.append([time1, gols1, time2, gols2])
    print(f"Partida registrada: {time1} {gols1} x {gols2} {time2}")


# Função para listar partidas
def ListaPartida():
    if len(partidas) == 0:
        print("Nenhuma partida registrada ainda.")
        return

    print("\nPartidas registradas:")
    # enumerate com start=1 para numerar as partidas a partir de 1
    for i, p in enumerate(partidas, start=1):
        # p[0]=time1, p[1]=gols1, p[2]=time2, p[3]=gols2
        print(f"{i}. {p[0]} {p[1]} x {p[3]} {p[2]}")


# Função de editar partidas
def EditarPertida():
    if len(partidas) <= 0:
        print("Nenhuma partida cadastrada")
        return

    print("Editar Partidas")
    ListaPartida()  # Mostra lista de partidas

    num = Veri_numero("\nQual partida deseja editar?\n->")

    # Valida se o número está dentro do intervalo válido
    if num <= 0 or num > len(partidas):
        print("Número inválido")
        return

    # Acessa a partida escolhida (índice = num - 1)
    partida = partidas[num - 1]
    print(f"\nPartida atual: {partida[0]} {partida[1]} x {partida[3]} {partida[2]}")

    print("\nDigite os novos placares:")
    novo_gols1 = Veri_numero(f"Gols do {partida[0]}: ")
    novo_gols2 = Veri_numero(f"Gols do {partida[2]}: ")

    # Atualiza os gols na lista de partidas
    partidas[num - 1][1] = novo_gols1  # Atualiza gols do time 1
    partidas[num - 1][3] = novo_gols2  # Atualiza gols do time 2

    print(f"Partida atualizada: {partida[0]} {novo_gols1} x {novo_gols2} {partida[2]}")


# Função para remover partidas
def RemoverPartida():
    if len(partidas) == 0:
        print("Nenhma partida cadastrada")
        return

    print("Remover Partida")
    ListaPartida()  # Mostra lista de partidas

    num = Veri_numero("\nQual partida você deseja cancelar?\n->")

    # Valida o número escolhido
    if num <= 0 or num > len(partidas):
        print("Número inválido")
        return

    # Acessa a partida escolhida
    partida = partidas[num - 1]
    print(f"\nVocê irá cancelar: {partida[0]} {partida[1]} x {partida[3]} {partida[2]}")

    # Pede confirmação antes de remover
    confirmar = input("Tem certeza? (s/n)\n->")
    if confirmar == "s":
        partidas.pop(num - 1)  # Remove a partida da lista
        print("Partida Cancelada!")
    else:
        print("Opção cancelada")


# ===== FUNÇÕES DE RELATÓRIOS =====

# Relatório de jogadoras por time
def RelatorioJogadorasPorTime():
    if len(times) == 0:
        print("Nenhum time cadastrado.")
        return

    # Percorre cada time
    for i, nome_time in enumerate(times):
        print(f"\nTime: {nome_time}")

        # List comprehension: filtra jogadoras do time atual
        jogas = [j for j in jogadoras if j[3] == nome_time]

        if len(jogas) == 0:
            print("  Nenhuma jogadora cadastrada.")
        else:
            for j in jogas:
                print(f"  - {j[0]} | Camisa {j[1]} | {j[2]}")


# Relatório de Classificação dos times (baseado em pontos)
def Classificacao():
    if len(partidas) == 0:
        print("Nenhuma partida registrada para gerar classificação.")
        return

    # Cria lista de pontos (inicialmente todos com 0)
    # Cada posição corresponde a um time
    pontos = [0] * len(times)

    # Calcula pontos a partir das partidas
    for p in partidas:
        # Encontra os índices dos times na lista 'times'
        i1 = times.index(p[0])  # Índice do time 1
        i2 = times.index(p[2])  # Índice do time 2

        # Sistema de pontuação: vitória = 3 pontos, empate = 1 ponto
        if p[1] > p[3]:  # Time 1 venceu
            pontos[i1] += 3
        elif p[1] < p[3]:  # Time 2 venceu
            pontos[i2] += 3
        else:  # Empate
            pontos[i1] += 1
            pontos[i2] += 1

    # Gera ranking combinando times com seus pontos
    # zip() agrupa elementos de duas listas: [(time1, pontos1), (time2, pontos2), ...]
    ranking = list(zip(times, pontos))

    # Ordena o ranking por pontos (x[1]) em ordem decrescente
    # lambda x: x[1] significa "usar o segundo elemento (pontos) para ordenar"
    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\nCLASSIFICAÇÃO:")
    # enumerate com start=1 para posições começarem em 1º, 2º, etc.
    for pos, (time, pts) in enumerate(ranking, start=1):
        print(f"{pos}º lugar: {time} - {pts} pontos")


# Função para relatórios (menu)
def Relatorio():
    while True:  # Loop do menu até escolher voltar
        print("\nRELATÓRIOS\n"
              "1. Jogadoras por time\n"
              "2. Todas as partidas\n"
              "3. Classificação dos times\n"
              "4. Voltar")
        opcao = input("Escolha uma opção: ")

        # Chama a função correspondente
        if opcao == "1":
            RelatorioJogadorasPorTime()
        elif opcao == "2":
            ListaPartida()
        elif opcao == "3":
            Classificacao()
        elif opcao == "4":
            break  # Volta ao menu anterior
        else:
            print("OPÇÃO INVÁLIDA! Tente novamente")


# Função para gerenciar jogadoras (menu)
def GerenciaJogadoras():
    while True:  # Loop do menu
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
            break  # Volta ao menu anterior
        else:
            print("Opção inválida")


# Função de editar jogadoras
def EditarJogadoras():
    # Verifica se há jogadoras cadastradas
    if len(jogadoras) <= 0:
        print("Nenhuma jogadora cadastrada")
    if len(times) <= 0:
        print("Nenhum Time cadastrado")

    while True:  # Loop para permitir múltiplas edições
        print("\nEditar Jogadoras")
        print("\nJogadoras cadastradas:")

        # Lista todas as jogadoras numeradas
        for i, jog in enumerate(jogadoras, start=1):
            print(f"{i}. {jog[0]} | Camisa {jog[1]} | {jog[2]} | {jog[3]}")

        num = Veri_numero("Qual jogadora deseja editar?\n->")

        # Valida o número
        if num <= 0 or num > len(jogadoras):
            print("Número inválido")
            return

        # Menu de opções de edição
        print("\nO que deseja alterar?"
              "\n1.Nome"
              "\n2.Número da camisa"
              "\n3.Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_nome = input("Insirá novo nome: ")
            # Atualiza o nome na posição [0] da jogadora
            jogadoras[num - 1][0] = novo_nome
            print(f"Nome atualizado!"
                  f"\nNovo nome: {novo_nome}")
        elif opcao == "2":
            nova_camisa = input("Insirá novo número de camisa: ")
            # Atualiza a camisa na posição [1] da jogadora
            jogadoras[num - 1][1] = nova_camisa
            print(f"Número atualizado"
                  f"\nNovo número de camisa: {nova_camisa}")
        elif opcao == "3":
            break  # Volta ao menu anterior
        else:
            print("Opção inválida!")


# Função para remover jogadoras
def RemoverJogadoras():
    if len(jogadoras) == 0:
        print("Nenhuma jogadora cadastrada.")
        return

    print("\n--- REMOVER JOGADORA ---")
    print("\nJogadoras cadastradas:")

    # Lista todas as jogadoras
    for i, jog in enumerate(jogadoras, start=1):
        print(f"{i}. {jog[0]} | Camisa {jog[1]} | {jog[2]} | {jog[3]}")

    num = Veri_numero("\nQual jogadora deseja remover?")

    if num == 0:
        return

    # Valida o número
    if num <= 0 or num > len(jogadoras):
        print("Número inválido!")
        return

    # Pega os dados da jogadora que será removida
    jogadora = jogadoras[num - 1]
    nome = jogadora[0]
    posicao = jogadora[2]
    time = jogadora[3]

    print(f"\nVocê vai remover: {nome} ({posicao}) do {time}")
    confirma = input("Tem certeza? (s/n): ")

    if confirma.lower() != 's':
        print("Operação cancelada.")
        return

    # Encontra o índice do time na lista de times
    indice_time = times.index(time)

    # Devolve a vaga para o time (incrementa contador de vagas)
    if posicao == "Goleira":
        vagas_goleira[indice_time] += 1
    elif posicao == "Defensora":
        vagas_defensora[indice_time] += 1
    elif posicao == "Meio":
        vagas_meio[indice_time] += 1
    elif posicao == "Atacante":
        vagas_atacante[indice_time] += 1

    # Remove a jogadora da lista
    jogadoras.pop(num - 1)
    print(f"Jogadora {nome} removida com sucesso!")


# ===== CÓDIGO PRINCIPAL =====

# Mensagem de boas-vindas
print("Bem-vindo(a) ao Passa a Bola!\nSistema de organização de campeonatos")
print("-" * 40)

# Tenta carregar dados salvos anteriormente
print("\n Carregando dados salvos...")
CarregarDados()
print()

# Loop principal do programa
while True:
    try:
        # Menu principal: escolher tipo de usuário
        usuario = int(input("Você é (1) Admin, (2) Jogadora ou (3) Sair?\n-> "))

        if usuario == 1:  # Modo Admin
            # --- Loop de autenticação ---
            while True:
                try:
                    senha = input("Digite a senha de administrador: ")

                    if senha != senha_admin:
                        raise ValueError("Senha incorreta!")  # Força exceção

                    print("Login realizado com sucesso!")
                    break  # Sai do loop de senha se acertar

                except ValueError as erro:
                    print("erro", erro)
                    print("Tente novamente.\n")

            # --- Se chegou aqui, senha está correta: abre MENU ADMIN ---
            while True:
                print("\nMENU ADMIN\n"
                      "1. Listar times e jogadoras\n"
                      "2. Gerenciar partidas\n"
                      "3. Gerenciar Jogadoras\n"
                      "4. Relatórios\n"
                      "5. Sair")
                opcao = input("Escolha: ")

                # Executa ação conforme opção escolhida
                if opcao == "1":
                    ListaTimesComJogadoras()
                elif opcao == "2":
                    GerenciaPartida()
                elif opcao == "3":
                    GerenciaJogadoras()
                elif opcao == "4":
                    Relatorio()
                elif opcao == "5":
                    # Salva dados antes de sair
                    print("\n Salvando dados...")
                    SalvarDados()
                    print("Saindo do menu Admin... voltando ao menu principal.")
                    break  # Encerra menu Admin, volta ao menu principal
                else:
                    print("Opção inválida!")

        elif usuario == 2:  # Modo Jogadora
            while True:
                print("\nMENU JOGADORA\n"
                      "1. Fazer inscrição\n"
                      "2. Sair")
                opcao = input("Escolha: ")

                if opcao == "1":
                    Cadastrajoga()
                elif opcao == "2":
                    print("Saindo do menu Jogadora... voltando ao menu principal.")
                    break  # Encerra menu Jogadora, volta ao menu principal
                else:
                    print("Opção inválida!")

        elif usuario == 3:  # Sair do sistema
            print("Programa encerrado pelo usuário.")
            break  # Esse break encerra o programa inteiro

        else:
            print("Opção inválida! Escolha apenas 1, 2 ou 3.\n")

    except ValueError:
        # Erro quando usuário digita texto em vez de número no menu principal
        print("Entrada inválida! Digite apenas números (1, 2 ou 3).\n")