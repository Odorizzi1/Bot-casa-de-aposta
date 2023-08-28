import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from mensagem import obter_mensagens
from datetime import datetime, timedelta
import pytz

TOKEN = '5888380144:AAGiRkqcBRRntx28Od7m82g3SsFkBCRGw7c'
chat_id = '-1001938444650'
intervalo_entre_mensagens = 400  # Em segundos

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    await enviar_mensagens()

async def enviar_mensagens():
    while True:
        try:
            # Obtém o fuso horário brasileiro
            fuso_horario_brasil = pytz.timezone('America/Sao_Paulo')

            # Obtém o horário atual com fuso horário brasileiro
            agora_brasil = datetime.now(fuso_horario_brasil)
            print(agora_brasil, "--")

            # Calcula o horário de expiração, 3 minutos após o horário atual
            horario_expiracao_brasil = agora_brasil + timedelta(minutes=3)
            horario_expiracao_str = horario_expiracao_brasil.strftime('%H:%M')
            print(f"Hora de Expiração: {horario_expiracao_str}")

            # Obtém uma mensagem usando o horário de expiração
            mensagens = obter_mensagens(horario_expiracao_str)

            # Se houver mensagens, pegue a primeira e envie
            if mensagens:
                mensagem_atualizada = mensagens[0].format(horario_expiracao_str=horario_expiracao_str)
                await bot.send_message(chat_id, mensagem_atualizada, parse_mode=ParseMode.MARKDOWN_V2, disable_web_page_preview=True)
                print('Mensagem enviada com sucesso.')

                # Aguarda um intervalo antes da próxima mensagem
                await asyncio.sleep(intervalo_entre_mensagens)

        except Exception as e:
            print(f'Erro ao enviar a mensagem: {str(e)}')
            await asyncio.sleep(10)  # Em caso de erro, aguarde 10 segundos antes de tentar novamente

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
