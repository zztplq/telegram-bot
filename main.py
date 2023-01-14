import logging
import config as cf
from aiogram import Bot, Dispatcher, executor, types
subs_list = [1,2,3,4,5,6,7,8,9, 10,12,11,13,14,15,16,17,28,18,19,20,21,22,23,24,25,26,27]
# Configure logging
logging.basicConfig(level = logging.INFO)
bot = Bot(token = cf.token)
dp = Dispatcher(bot)

HELP_MESSAGE =  """
<b>/help</b> - <em>помощь с командами</em>
<b>/buy</b> - <em>купить подписку</em>
<b>/start</b> - <em>Начать работу бота</em>
<b>/next</b> - <em>Найти человека</em>
<b>/stop</b> - <em>Остановить поиск/чат с ботом</em>
"""

@dp.message_handler( commands = ['buy'])
async def send_bay_command(message: types.message):
    args = message.get_args()
    if len(subs_list) == 0:
        return await bot.send_message(message.chat.id, "К сожалению на данный момент подписок не осталось, зайдите попозже")
    if not args:
        return await bot.send_message(message.chat.id, f"Сейчас есть подписки, вы можете ее подарить либо купить себе, подписок осталось {len(subs_list)}, чтобы купить подписки напишите /buy (числовые значения подписок)")
    else:
        if args.isdigit():
            args = int(args)
            if args > len(subs_list):
                return await bot.send_message(message.chat.id, "Вы ввели неккоректное или выбрали число больше чем есть подписок, смените ваше числовое значение")
            else:
                for i in range(args):
                    #print(i)
                    subs_list.pop()
                return await bot.send_message(message.chat.id, f"Осталось {len(subs_list)} подписок")
        else:
            return await bot.send_message(message.chat.id, "Введите другое числовое значение, так как такого количества подписок нет")





@dp.message_handler( commands = ['start'])
async def send_welcom(message: types.message):
   return await bot.send_message(message.chat.id, "Бот включён")

@dp.message_handler( commands = ['stop'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Анонимный Чат выключен")

@dp.message_handler( commands = ['s'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Найден человек, чтобы найти нового человека: /next"
                        " чтобы выйти в главное меню: /stop")

@dp.message_handler( commands = ['stop'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Анонимный Чат выключен")

@dp.message_handler( commands = ['next'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Найден человек, чтобы найти нового человека: /next"
                        " чтобы выйти в главное меню: /stop")

@dp.message_handler( commands = ['help'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, HELP_MESSAGE, "HTML")

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates = True)

