from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pytz




mensagens = [
    """
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
    """
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
    """
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
    """
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
    """
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
    """
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
    """
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
    """
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