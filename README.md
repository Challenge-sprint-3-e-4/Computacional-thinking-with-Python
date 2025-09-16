# Projeto Acadêmico FIAP - Challenge 2025 - Sprint 3-4
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


# 📌 Passa a Bola – Sistema de Organização de Campeonatos

Este projeto é um sistema simples em **Python** para organizar campeonatos de futebol entre jogadoras.
Ele permite **cadastrar jogadoras**, **gerenciar times automaticamente**, **registrar partidas** e **gerar relatórios de classificação**.

---

## ⚙️ Funcionalidades

* **Cadastro de jogadoras**

  * Inscrição com nome, número da camisa e posição.
  * Posições válidas: **Goleira**, **Defensora**, **Meio** e **Atacante**.
  * Alocação automática em um time existente ou criação de um novo time caso necessário.

* **Gerenciamento de times**

  * Criação automática de times (`Time 1`, `Time 2`, ...).
  * Controle de vagas por posição conforme a formação padrão:

    * 1 Goleira
    * 2 Defensoras
    * 2 Meio-campistas
    * 2 Atacantes

* **Gerenciamento de partidas**

  * Registro de partidas entre dois times.
  * Armazenamento de resultados (gols de cada equipe).
  * Listagem de todas as partidas registradas.

* **Relatórios**

  * Listar jogadoras por time.
  * Exibir todas as partidas jogadas.
  * Classificação dos times com pontuação (Vitória = 3 pontos, Empate = 1 ponto).

* **Perfis de acesso**

  * **Admin**

    * Listar times e jogadoras.
    * Gerenciar partidas.
    * Acessar relatórios.
  * **Jogadora**

    * Fazer inscrição em um time.

---

## 🛠️ Estrutura de Dados

O sistema utiliza listas principais para armazenar as informações:

* `jogadoras` → lista com dados das jogadoras (`nome, camisa, posição, time`).
* `times` → lista de times cadastrados.
* `vagas_goleira`, `vagas_defensora`, `vagas_meio`, `vagas_atacante` → vagas disponíveis por posição em cada time.
* `partidas` → lista com partidas registradas (`time1, gols1, time2, gols2`).

---

## 🔐 Acesso de Admin

* Senha padrão: **`1234`**
* Menus disponíveis:

  1. Listar times e jogadoras
  2. Gerenciar partidas
  3. Relatórios
  4. Sair

---

## 📋 Fluxo do Programa

1. Ao iniciar, o sistema pergunta:

   * **(1) Admin** ou **(2) Jogadora**
2. Dependendo da escolha:

   * Admin → acesso ao menu de gerenciamento.
   * Jogadora → acesso ao menu de inscrição.
3. Todas as operações são feitas via **input no terminal**.

---

## ▶️ Execução

Para rodar o programa, basta executar o arquivo Python:

```bash
python passa_a_bola.py
```

---

## 🚀 Possíveis Melhorias

* Salvar dados em arquivo (CSV/JSON) para não perder informações ao fechar o programa.
* Interface gráfica ou versão web.
* Estatísticas detalhadas (artilheira, saldo de gols, etc).
* Opção de edição/exclusão de jogadoras e partidas.

---

📌 **Resumo:**
Este projeto é uma ótima base para um sistema de campeonatos, permitindo gerenciar times, jogadoras e partidas de maneira simples e direta via terminal.

