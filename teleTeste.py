import asyncio
from telegram import Bot
from mensagem import mensagens
import sys

# Obtendo os argumentos da linha de comando
argumentos = sys.argv

# O primeiro argumento (sys.argv[0]) é o nome do próprio script
# Os argumentos fornecidos começam a partir do índice 1
arg1 = 10 
if len(argumentos) > 1:
    arg1 = argumentos[1]

# Substitua 'SEU_TOKEN_AQUI' pelo token do seu bot
TOKEN = '5888380144:AAGiRkqcBRRntx28Od7m82g3SsFkBCRGw7c'

# Substitua 'ID_DO_CHAT_AQUI' pelo ID de chat do usuário ou grupo que receberá as mensagens
chat_id = '-1001938444650'
time = 60 * float(arg1)

# Função para enviar mensagens automaticamente
async def enviar_mensagem():
    bot = Bot(token=TOKEN)
    
    while True:
        try:
            for mensagem in mensagens:
                await bot.send_message(chat_id, mensagem, parse_mode='MarkdownV2', disable_web_page_preview=True)
                print('Mensagem enviada com sucesso.')

                # Espere 10 segundos antes de enviar a próxima mensagem
                await asyncio.sleep(time)
        except Exception as e:
            print(f'Erro ao enviar a mensagem: {str(e)}')
            await asyncio.sleep(time)

# Inicie o envio de mensagens automáticas
if __name__ == "__main__":
    asyncio.run(enviar_mensagem())
