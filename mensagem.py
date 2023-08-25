from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# Calcule o horário de expiração (3 minutos a partir da hora atual)
agora = datetime.now()
horario_expiracao = agora + timedelta(minutes=3)
horario_expiracao_str = horario_expiracao.strftime('%H:%M')

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