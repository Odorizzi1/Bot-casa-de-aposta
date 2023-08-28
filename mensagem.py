from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pytz

# Define o fuso horário do Brasil (BRT - Horário de Brasília)
fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

# Obtém a hora atual no fuso horário do Brasil
agora_brasil = datetime.now(fuso_horario_brasil)

# Calcula o horário de expiração (3 minutos a partir da hora atual)
horario_expiracao_brasil = agora_brasil + timedelta(minutes=3)
horario_expiracao_str = horario_expiracao_brasil.strftime('%H:%M')

url_mines = "https://greenbets.io/casino/game/1695257/?bta=45274&brand=greenbetsio"
url_cadastro = "https://afiliados.greenbets.io/visit/?bta=45274&brand=greenbetsio"

mensagens = [
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    🟦 ⭐ 🟦 🟦 🟦
    🟦 🟦 🟦 ⭐ 🟦
    ⭐ 🟦 ⭐ 🟦 🟦
    🟦 ⭐ 🟦 🟦 🟦
    🟦 🟦 🟦 🟦 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    ⭐ 🟦 🟦 🟦 ⭐
    🟦 🟦 🟦 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    🟦 ⭐ 🟦 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    🟦 🟦 🟦 🟦 ⭐
    ⭐ 🟦 🟦 🟦 🟦
    ⭐ 🟦 🟦 ⭐ 🟦
    🟦 🟦 🟦 ⭐ 🟦
    🟦 🟦 🟦 🟦 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    🟦 ⭐ 🟦 🟦 🟦
    🟦 ⭐ 🟦 🟦 🟦
    ⭐ 🟦 🟦 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    ⭐ 🟦 🟦 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    🟦 🟦 🟦 🟦 🟦
    🟦 🟦 🟦 ⭐ 🟦
    🟦 ⭐ ⭐ 🟦 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    ⭐ 🟦 🟦 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    🟦 🟦 ⭐ 🟦 🟦
    ⭐ 🟦 🟦 🟦 🟦
    🟦 🟦 🟦 ⭐ 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4 
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    🟦 🟦 ⭐ 🟦 🟦
    🟦 🟦 🟦 ⭐ 🟦
    🟦 🟦 🟦 ⭐ 🟦
    🟦 🟦 🟦 ⭐ 🟦
    🟦 🟦 ⭐ ⭐ 🟦
    """,
    f"""
    💰 Entrada Confirmada 💰
    💣 Minas: 4
    ⏱ Valido até as {horario_expiracao_str}
    🔁 Nº de tentativas: 3

    🔗  [Clique aqui para abrir mines]({url_mines})
    🔗  [Clique aqui para o link de cadastro]({url_cadastro})

    ⭐ 🟦 🟦 🟦 🟦
    🟦 🟦 🟦 🟦 🟦
    🟦 ⭐ 🟦 ⭐ 🟦
    🟦 ⭐ 🟦 ⭐ 🟦
    🟦 🟦 🟦 🟦 🟦
    """,
]