from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pytz

def obter_mensagens(horario_expiracao_str):
    url_cadastro = "https://greenbets.io/casino/game/1695257/?bta=45274&brand=greenbetsio"
    url_mines = "https://afiliados.greenbets.io/visit/?bta=45274&brand=greenbetsio"

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

    return mensagens
