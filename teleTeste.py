import asyncio
from telegram import Bot
from mensagem import obter_mensagens
from datetime import datetime, timedelta
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import pytz
import time

TOKEN = '5888380144:AAGiRkqcBRRntx28Od7m82g3SsFkBCRGw7c'

# Substitua 'ID_DO_CHAT_AQUI' pelo ID de chat do usuário ou grupo que receberá as mensagens
chat_id = '-1001938444650'
intervalo_entre_mensagens = 360  # Altere para o valor desejado

async def enviar_mensagens():
    bot = Bot(token=TOKEN)

    while True:  # Um loop infinito para enviar mensagens continuamente
        try:
            fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')
            agora_brasil = datetime.now(fuso_horario_brasil)

            # Calcula o horário de expiração (3 minutos a partir da hora atual)
            horario_expiracao_brasil = agora_brasil + timedelta(minutes=3)
            horario_expiracao_str = horario_expiracao_brasil.strftime('%H:%M')
            print(horario_expiracao_str)  # Adicione esta linha

            mensagens = obter_mensagens()  # Chame a função sem passar horario_expiracao_str como argumento

            for mensagem_original in mensagens:
                mensagem_atualizada = mensagem_original.format(horario_expiracao_str=horario_expiracao_str)
                await bot.send_message(chat_id, mensagem_atualizada, parse_mode='MarkdownV2', disable_web_page_preview=True)
                print('Mensagem enviada com sucesso.')
                await asyncio.sleep(intervalo_entre_mensagens)  # Aguarda o intervalo antes de enviar a próxima mensagem
        except Exception as e:
            print(f'Erro ao enviar a mensagem: {str(e)}')

if __name__ == "__main__":
    asyncio.run(enviar_mensagens())
