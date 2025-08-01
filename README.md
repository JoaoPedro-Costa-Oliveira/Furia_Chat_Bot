# Furia Chat Bot 🐾

<p align="center">
  <img src="https://i.imgur.com/your-gif-url.gif" alt="Demonstração do Furia Chat Bot em ação" width="700"/>
  <br/>
  <strong>Um hub interativo para fãs da FURIA, com chatbot, tracker de partidas "ao vivo" e mais!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Flask-black.svg" alt="Flask Framework">
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange.svg" alt="Frontend">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

## 🎯 Visão Geral do Projeto

O **Furia Chat Bot** é uma aplicação web criada como um tributo à equipe de e-sports FURIA. O objetivo é centralizar em um único lugar todas as informações que um torcedor apaixonado precisa, de forma interativa e dinâmica. A plataforma conta com um chatbot para responder perguntas, um tracker de partidas com atualizações "ao vivo", e um feed de conteúdo exclusivo, simulando a experiência de acompanhar a equipe em tempo real.

Este projeto foi desenvolvido utilizando **Python** com o microframework **Flask** no backend, e **HTML, CSS e JavaScript** no frontend para criar uma experiência de usuário fluida e reativa.

---

## ✨ Funcionalidades Principais

* **Chatbot Interativo:** Converse com o Fuira para obter informações instantâneas sobre:
    * Placar e status da partida atual.
    * Últimas notícias e vídeos de highlights.
    * Agenda de próximos jogos e eventos.
    * Elenco de jogadores (`lineup`) e suas funções.
    * Curiosidades e fatos sobre a equipe.

* **Tracker de Partida "Ao Vivo":** Uma seção da página que é atualizada dinamicamente para mostrar o status da partida atual, incluindo placar, mapa, round e o jogador destaque, criando uma imersão completa.

* **Feed de Conteúdo Centralizado:** Acesse facilmente as últimas notícias, os clipes de melhores jogadas e a agenda da equipe, tudo consolidado em um só lugar pelo chatbot.

* **Simulação de Chat de Fãs:** Para aumentar a atmosfera de dia de jogo, um pequeno feed exibe mensagens aleatórias de torcedores, simulando um chat de transmissão ao vivo.

---

## 🛠️ Stack de Tecnologias

| Área | Tecnologia | Descrição |
| :--- | :--- | :--- |
| **Backend** | `Python` | Linguagem principal para toda a lógica do servidor. |
| | `Flask` | Microframework web para criar a aplicação e servir a página principal. |
| **Frontend** | `HTML5` | Estruturação do conteúdo da página. |
| | `CSS3` | Estilização para criar um design limpo e responsivo. |
| | `JavaScript` | Responsável pela interatividade. |

---

## 🧠 Arquitetura e Lógica

A aplicação segue uma arquitetura cliente-servidor clássica:

1.  **Frontend (Cliente):** O `index.html`, estilizado com CSS, utiliza JavaScript para capturar as ações do usuário (como enviar uma mensagem no chat) e para fazer requisições periódicas ao backend.
2.  **Comunicação (API):** O JavaScript utiliza a **Fetch API** para fazer chamadas assíncronas aos endpoints do Flask, enviando dados (mensagens do usuário) e recebendo atualizações (respostas do bot, status da partida).
3.  **Backend (Servidor):** O **Flask** expõe vários endpoints:
    * `/`: Serve a página principal (`index.html`).
    * `/chat`: Recebe uma mensagem do usuário via `POST`, processa a intenção com base em palavras-chave e retorna a resposta do bot.
    * `/match_update`: Um endpoint `GET` que fornece o estado mais recente da partida simulada.
    * `/fan_message`: Um endpoint `GET` que retorna uma mensagem aleatória de torcedor.

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para ter o Fuira Chat Bot rodando na sua máquina.

**Pré-requisitos:**
* Python 3.8+
* Git

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/JoaoPedro-Costa-Oliveira/Furia_Chat_Bot.git](https://github.com/JoaoPedro-Costa-Oliveira/Furia_Chat_Bot.git)
    cd Furia_Chat_Bot
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # No Windows:
    venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    *(Este projeto usa apenas Flask, mas é uma boa prática ter um `requirements.txt`)*
    ```bash
    pip install Flask
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e vá para `http://localhost:5000`.

---

## 💡 Possíveis Melhorias

Este projeto tem uma base sólida e pode ser expandido de várias formas:

-   [ ] **Integração com uma API Real:** Substituir os dados simulados por uma API de e-sports real (como PandaScore, HLTV API) para obter dados de partidas em tempo real.
-   [ ] **Chatbot mais Inteligente:** Implementar uma biblioteca de NLP (Processamento de Linguagem Natural) como o spaCy ou mesmo conectar a um modelo de linguagem para um diálogo mais fluido.
-   [ ] **WebSockets:** Utilizar WebSockets para que as atualizações da partida e do chat de fãs sejam enviadas do servidor para o cliente em tempo real, sem a necessidade de o cliente ficar perguntando a cada segundo.
-   [ ] **Banco de Dados:** Adicionar um banco de dados (como SQLite ou PostgreSQL) para armazenar histórico de partidas, notícias ou até mesmo perfis de usuário.

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.