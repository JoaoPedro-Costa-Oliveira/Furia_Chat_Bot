# app.py
import random
import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Dados Simulados ---

# Match Data (Replace with real-time source/API if available)
# For demo purposes, we'll cycle through a few states
match_states = [
    {
        "live": True,
        "opponent": "NAVI",
        "map": "Mirage",
        "score": "FURIA 5 - 8 NAVI",
        "round": 14,
        "top_player": {"name": "KSCERATO", "kills": 12, "adr": 95.2},
        "status": "Live - First Half"
    },
    {
        "live": True,
        "opponent": "NAVI",
        "map": "Mirage",
        "score": "FURIA 12 - 10 NAVI",
        "round": 23,
        "top_player": {"name": "yuurih", "kills": 19, "adr": 101.5},
        "status": "Live - Second Half"
    },
    {
        "live": True,
        "opponent": "NAVI",
        "map": "Mirage",
        "score": "FURIA 16 - 13 NAVI",
        "round": 29,
        "top_player": {"name": "KSCERATO", "kills": 25, "adr": 98.0},
        "status": "Match Point FURIA!"
    },
     {
        "live": False,
        "opponent": "NAVI",
        "map": "Mirage",
        "score": "FURIA 16 - 14 NAVI",
        "round": 30,
        "top_player": {"name": "KSCERATO", "kills": 26, "adr": 97.1},
        "status": "FINAL SCORE - FURIA WINS!"
    },
    {
        "live": False,
        "opponent": "G2",
        "map": "TBD",
        "score": "N/A",
        "round": 0,
        "top_player": None,
        "status": "No live match currently. Next match vs G2 tomorrow at 16:00 BRT."
    }
]
current_match_state_index = 0

# Fan Chat Simulation
fan_messages = [
    "VAMOOOO FURIA!!! ⚫🟣", "Que isso KSCERATO?! Joga demais!", "ACE DO YUURIH!",
    "BORA PANTERAS!", "CLUTCH TIME!", "NT NT guys", "art é o capitas!",
    "GANHAMO ESSA ROUND!", "Acredita!! 🙏", "Que bala!", "🔥🔥🔥",
    "Esse mapa é nosso!", "Proximo é OVERPASS!", "#DIADEFURIA", "⚫🟣⚫🟣"
]

# Exclusive Content
exclusive_content = {
    "news": [
        "FURIA se classifica para o próximo Major!",
        "Confira a última entrevista com o guerri.",
        "Nova camisa da FURIA lançada! Link: [link da loja]"
    ],
    "highlights": [
        "KSCERATO clutch 1v4 contra a NAVI: [link do vídeo]",
        "Spray insano do Yuurih: [link do vídeo]",
        "Melhores jogadas agressivas do Art com AWP: [link do vídeo]"
    ],
    "próximo jogo": [
        "Próxima Partida: FURIA vs G2 - Amanhã às 16:00 BRT",
        "Próximo Torneio: IEM Cologne - Início em 25 de julho"
    ],
    "curiosidades": [
        "A FURIA foi fundada em 2017.",
        "KSCERATO é conhecido por sua consistência incrível.",
        "arT é famoso por seu estilo de jogo agressivo e W-key.",
        "O mascote da equipe é uma Pantera.",
        "A FURIA também tem times em outros jogos como LoL e Valorant."
    ],
    "players": [
        {"name": "arT", "role": "IGL/AWPer"},
        {"name": "yuurih", "role": "Rifler (Lurker)"},
        {"name": "KSCERATO", "role": "Rifler (Entry)"},
        {"name": "FalleN", "role": "AWPer"},
        {"name": "chelo", "role": "Rifler (Entry/Suporte)"},  # Papéis fictícios
        {"name": "guerri", "role": "Técnico"}
    ]
}

# --- Helper Functions ---

def get_current_match_update():
    global current_match_state_index
    # Cycle through states for demo purposes
    state = match_states[current_match_state_index]
    current_match_state_index = (current_match_state_index + 1) % len(match_states)
    return state

def get_random_fan_message():
    return random.choice(fan_messages)

def process_user_message(message):
    """Handles user input and generates chatbot response."""
    msg_lower = message.lower()
    response = "Desculpe, não entendi. Tente perguntar sobre 'placar', 'partida', 'news', 'highlights', 'jogadores', 'eventos' ou 'curiosidades'."

    if any(keyword in msg_lower for keyword in ["hi", "hello", "hey", "oi", "e aí"]):
        response = random.choice(["E aí! Preparado para a FURIA? ⚫🟣", "Olá! #DIADEFURIA", "Fala aí! Pergunte algo sobre a FURIA!"])

    elif any(keyword in msg_lower for keyword in ["score", "match", "live", "game", "jogo", "partida"]):
        match_data = get_current_match_update() # Get *latest* state when asked
        if match_data.get("live"):
             response = (f"🔴 AO VIVO vs {match_data['opponent']} no mapa {match_data['map']}!\n"
                        f"Placar: {match_data['score']} (Round {match_data['round']})\n"
                        f"Status: {match_data['status']}")
             if match_data.get("top_player"):
                 tp = match_data['top_player']
                 response += f"\nMVP: {tp['name']} ({tp['kills']}K, {tp['adr']} ADR)"
        else:
             response = f"⚫🟣 Status: {match_data['status']}"

    elif "news" in msg_lower:
        response = "📰 Ultimas Notícias:\n- " + "\n- ".join(exclusive_content["news"])

    elif any(keyword in msg_lower for keyword in ["destaques", "clipes", "vídeos", "highlights"]):
        response = "🎬 Highlights Recente:\n- " + "\n- ".join(exclusive_content["highlights"])

    elif any(keyword in msg_lower for keyword in ["evento", "agenda", "próximo jogo", "schedule", "upcoming"]):
        response = "📅 Próximos Eventos:\n- " + "\n- ".join(exclusive_content["events"])

    elif any(keyword in msg_lower for keyword in ["facts", "fatos", "curiosidades"]):
        response = f"💡 Curiosidade: {random.choice(exclusive_content['facts'])}"

    elif any(keyword in msg_lower for keyword in ["jogadores", "time", "equipe", "players", "lineup"]):
        player_list = [f"{p['name']} ({p['role']})" for p in exclusive_content["players"]]
        response = "👥 Time FURIA CS:GO :\n- " + "\n- ".join(player_list)

    elif any(keyword in msg_lower for keyword in ["thanks", "obrigado", "ty", "valeu"]):
        response = random.choice(["De nada!", "Sem problemas!", "Tamo junto! ⚫🟣"])

    elif "bye" in msg_lower:
        response = "Até logo! VAMO FURIA!"

    return response

# --- API Endpoints ---

@app.route('/')
def index():
    """Serves the main landing page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handles incoming chat messages."""
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Nenhuma mensagem recebida"}), 400

    bot_response = process_user_message(user_message)
    return jsonify({"response": bot_response})

@app.route('/match_update', methods=['GET'])
def match_update():
    """Provides the current simulated match state."""
    # In a real app, this would fetch live data
    # For demo, we just return the current simulated state
    # Note: Using get_current_match_update() here makes it cycle on every poll
    # A better simulation might hold state longer or use a background thread
    state = match_states[current_match_state_index] # Return current without advancing
    return jsonify(state)

@app.route('/fan_message', methods=['GET'])
def fan_message():
    """Provides a random simulated fan message."""
    return jsonify({"message": get_random_fan_message()})

# --- Run the App ---
if __name__ == '__main__':
    # Note: Use a proper WSGI server like Gunicorn or Waitress for production
    app.run(debug=True, host='0.0.0.0', port=5000) # Make accessible on local network