// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const chatDisplay = document.getElementById('chat-display');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const matchInfoDiv = document.getElementById('match-info');

    // --- Função para adicionar mensagens na exibição do chat ---
    function addMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender); // sender = 'user', 'bot', or 'fan'
        
        const span = document.createElement('span'); // Envolve o texto em um span para melhor estilo
        span.textContent = text;
        messageDiv.appendChild(span);
        
        chatDisplay.appendChild(messageDiv);
        chatDisplay.scrollTop = chatDisplay.scrollHeight; // Rolagem automática para o fim
    }

    // --- Função para enviar mensagem do usuário e obter resposta do bot ---
    async function sendMessage() {
        const messageText = userInput.value.trim();
        if (messageText === '') return;

        addMessage(messageText, 'user');
        userInput.value = ''; // Limpa o campo de entrada

        try {
            // Exibir indicador de pensamento (opcional)
            // addMessage("...", 'bot-typing'); 

            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: messageText }),
            });

            // Remover indicador de pensamento (se usado)
            // const typingIndicator = chatDisplay.querySelector('.bot-typing');
            // if (typingIndicator) chatDisplay.removeChild(typingIndicator);

            if (!response.ok) {
                throw new Error(`Erro HTTP! status: ${response.status}`);
            }

            const data = await response.json();
            addMessage(data.response, 'bot');

        } catch (error) {
            console.error("Erro ao enviar a mensagem:", error);
            addMessage("Opa! Algo deu errado. Por favor, tente novamente.", 'bot');
        }
    }

    // --- Função para buscar e exibir atualizações da partida ---
    async function fetchMatchUpdate() {
        try {
            const response = await fetch('/match_update');
            if (!response.ok) {
                throw new Error(`Erro HTTP! status: ${response.status}`);
            }
            const data = await response.json();
            
            // Formatar exibição da atualização da partida
            let matchHTML = `<p><strong>Status:</strong> ${data.status}</p>`;
            if (data.live) {
                matchHTML = `<p><strong class="live">🔴 AO VIVO vs ${data.opponent}</strong> no mapa ${data.map}</p>
                             <p><strong>Placar:</strong> ${data.score} (Rodada ${data.round})</p>`;
                 if (data.top_player) {
                     const tp = data.top_player;
                     matchHTML += `<p><strong>Melhor Jogador:</strong> ${tp.name} (${tp.kills}K, ${tp.adr} ADR)</p>`;
                 }
            } else if (data.score !== 'N/A' && data.score.includes('WIN')) {
                 matchHTML = `<p><strong class="final">🏆 PLACAR FINAL vs ${data.opponent}</strong> no mapa ${data.map}</p>
                              <p><strong>Resultado:</strong> ${data.score}</p>`;
                  if (data.top_player) {
                     const tp = data.top_player;
                     matchHTML += `<p><strong>MVP:</strong> ${tp.name} (${tp.kills}K, ${tp.adr} ADR)</p>`;
                 }
            }
            // Adicione estilo específico se necessário, ex: baseado no placar ou status
            matchInfoDiv.innerHTML = matchHTML;

        } catch (error) {
            console.error("Erro ao buscar atualização da partida:", error);
            matchInfoDiv.textContent = "Não foi possível carregar o status da partida.";
        }
    }

    // --- Função para buscar e exibir mensagens simuladas de fãs ---
    async function fetchFanMessage() {
        // Só exibe mensagens de fãs se uma partida estiver 'ao vivo' ou empolgante
        // Esta lógica pode ser amarrada ao estado real da partida
        // Para simplificar, será mostrado aleatoriamente às vezes
        if (Math.random() < 0.6) { // Ajuste a probabilidade conforme necessário
            try {
                const response = await fetch('/fan_message');
                 if (!response.ok) {
                    throw new Error(`Erro HTTP! status: ${response.status}`);
                }
                const data = await response.json();
                addMessage(data.message, 'fan');

            } catch (error) {
                console.error("Erro ao buscar mensagem de fã:", error);
                // Não exibir erro no chat nesse caso, apenas registrar
            }
        }
    }

    // --- Listeners de Evento ---
    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // --- Carregamento Inicial e Atualizações Periódicas ---
    fetchMatchUpdate(); // Busca inicial
    // Atualizações periódicas (ajuste os intervalos se necessário)
    setInterval(fetchMatchUpdate, 10000); // Verifica status da partida a cada 10 segundos
    setInterval(fetchFanMessage, 7000);   // Verifica nova mensagem de fã a cada 7 segundos

});
