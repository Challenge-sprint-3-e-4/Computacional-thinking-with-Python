# Projeto Acadêmico FIAP - Challenge 2025 - Sprint 3
**Parceria com o Passa Bola**

Este é um *projeto acadêmico FIAP*, desenvolvio como parte do *challenge 2025*, focado em *auxiliar o Passa Bola na organização e gerenciamento de seus campeonatos*. O sistema integra funções, condições, listas e loops.

---

# Integrantes:

- João Vitor Parizotto Rocha | RM: 562719
- Giovana Bernardino Carnevali | RM: 566196
- Alexandre Freitas Silva | RM: 566278
- Felipe Rodrigues Gomes Ribeiro | RM: 562482
- Artur Distrutti Santos | RM: 561319

---

# ⚽ Passa a Bola – Sistema de Organização de Campeonatos

Sistema desenvolvido em **Python** para gerenciar campeonatos esportivos, permitindo **cadastrar jogadoras**, **gerenciar times**, **registrar partidas** e **gerar relatórios automáticos**.
Agora com **salvamento automático em JSON** e menus separados para **Admin** e **Jogadora**.

---

## 🧠 Visão Geral

O **Passa a Bola** é um sistema de console simples, mas completo, para organizar campeonatos.
Permite:

* Cadastro e alocação automática de jogadoras em times.
* Criação automática de times conforme necessidade.
* Controle de vagas por posição.
* Registro, edição e remoção de partidas.
* Relatórios detalhados (classificação, jogadoras, partidas).
* Salvamento automático em arquivo JSON.

---

## 📂 Estrutura de Dados

| Estrutura                                                          | Tipo    | Descrição                                         |
| ------------------------------------------------------------------ | ------- | ------------------------------------------------- |
| `jogadoras`                                                        | list    | Cada item é `[nome, camisa, posição, time]`       |
| `times`                                                            | list    | Lista com nomes dos times criados automaticamente |
| `partidas`                                                         | list    | Cada item é `[time1, gols1, time2, gols2]`        |
| `vagas_goleira`, `vagas_defensora`, `vagas_meio`, `vagas_atacante` | list    | Controlam vagas restantes em cada time            |
| `campeonato.json`                                                  | arquivo | Armazena permanentemente todas as informações     |

---

## 💾 Persistência de Dados

O sistema salva e carrega dados automaticamente usando o arquivo **`campeonato.json`**:

* **SalvarDados()** → Exporta todas as listas para o JSON.
* **CarregarDados()** → Recarrega os dados na inicialização.

```bash
# Arquivo JSON gerado (exemplo)
{
  "Jogadoras": [["Ana", 10, "Atacante", "Time 1"]],
  "Times": ["Time 1"],
  "Partidas": [["Time 1", 3, "Time 2", 2]],
  ...
}
```

---

## ⚙️ Funcionalidades

### 👥 Jogadoras

* Cadastrar jogadoras com nome, número e posição.
* Alocação automática em times com vagas disponíveis.
* Criação automática de novos times quando necessário.
* Edição e remoção de jogadoras (modo Admin).
* Retorno de vagas ao time quando jogadora é removida.

### 🏟️ Times

* Criação automática sequencial (“Time 1”, “Time 2”, ...).
* Controle automático de vagas:

  | Posição   | Vagas por Time |
  | --------- | -------------- |
  | Goleira   | 1              |
  | Defensora | 2              |
  | Meio      | 2              |
  | Atacante  | 2              |

### ⚔️ Partidas

* Registro de partidas entre times existentes.
* Edição e cancelamento de partidas.
* Exibição completa do histórico de jogos.

### 📊 Relatórios

* Jogadoras por time.
* Lista de todas as partidas.
* Classificação dos times com pontuação:

  * Vitória → 3 pontos
  * Empate → 1 ponto

---

## 🔐 Perfis de Acesso

### 👨‍💼 Admin

Acesso com senha padrão: **`1234`**

**Menu do Admin:**

1. Listar times e jogadoras
2. Gerenciar partidas
3. Gerenciar jogadoras
4. Relatórios
5. Sair (salva automaticamente)

**Funções disponíveis:**

* Visualizar times e jogadoras.
* Cadastrar, editar e remover partidas.
* Editar e excluir jogadoras.
* Gerar relatórios de desempenho.

---

### 👩 Jogadora

Acesso sem senha.
Permite apenas **inscrição em times**.

**Menu da Jogadora:**

1. Fazer inscrição
2. Sair

---

## 🧾 Relatórios Disponíveis

| Relatório          | Descrição                                |
| ------------------ | ---------------------------------------- |
| Jogadoras por Time | Lista jogadoras agrupadas por seus times |
| Todas as Partidas  | Exibe todas as partidas registradas      |
| Classificação      | Mostra ranking dos times por pontuação   |

---

## ▶️ Execução

1. Certifique-se de ter o **Python 3.8+** instalado.
2. Salve o código como `passa_a_bola.py`.
3. Execute no terminal:

```bash
python passa_a_bola.py
```

4. Escolha seu perfil:

   * **Admin** → Acesso total.
   * **Jogadora** → Apenas inscrição.
   * **Sair** → Encerra o programa.

---

## 🧩 Estrutura do Projeto

```
📁 Passa_a_Bola/
 ├── passa_a_bola.py
 ├── campeonato.json        # Gerado automaticamente
 └── README.md              # (este arquivo)
```

---

## 💡 Melhorias Futuras

* ✅ Persistência implementada via JSON
* ⏳ Próximas ideias:

  * Interface gráfica (Tkinter ou web)
  * Estatísticas detalhadas (artilheira, saldo de gols)
  * Exportação de relatórios em PDF/CSV
  * Login individual por jogadora

---

📌 **Resumo:**
Este projeto é uma ótima base para um sistema de campeonatos, permitindo gerenciar times, jogadoras e partidas de maneira simples e direta via terminal.

