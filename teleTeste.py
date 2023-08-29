import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from mensagem import mensagens
from datetime import datetime, timedelta
import pytz

TOKEN = '5888380144:AAGiRkqcBRRntx28Od7m82g3SsFkBCRGw7c'
chat_id = '-1001938444650'

# Inicialização do bot e do dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_messages():
    for mensagem in mensagens:
        agora = datetime.now(pytz.timezone('America/Sao_Paulo'))  # Ajustado para o fuso horário de São Paulo
        horario_expiracao = agora + timedelta(minutes=3)
        horario_expiracao_str = horario_expiracao.strftime('%H:%M')
        url_cadastro = "https://greenbets.io/casino/game/1695257/?bta=45274&brand=greenbetsio"
        url_mines = "https://afiliados.greenbets.io/visit/?bta=45274&brand=greenbetsio"
        
        mensagem_formatada = mensagem.format(horario_expiracao_str=horario_expiracao_str, 
                                             url_mines=url_mines, 
                                             url_cadastro=url_cadastro)

        # Enviar a mensagem
        await bot.send_message(chat_id, mensagem_formatada, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
        
        print(horario_expiracao)
        print(mensagem_formatada)
        print(horario_expiracao_str)

        await asyncio.sleep(420)  # Pausa assíncrona de 10 segundos

# Roda a função principal
asyncio.run(send_messages())
