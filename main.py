import logging
import config as cf
from aiogram import Bot, Dispatcher, executor, types
subs_list = [1,2,3,4,5,6,7,8,9,10,12,11,13]
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
                    subs_list.append()
                return await bot.send_message(message.chat.id, f"Осталось {len(subs_list)} подписок")
        else:
            return await bot.send_message(message.chat.id, "Введите другое числовое значение, так как такого количества подписок нет")



@dp.message_handler( commands = ['add'])
async def send_welcom(message: types.message):
    print(message.chat.id)
    args = message.get_args()
    if message.chat.id != 1099292405:
        return await bot.send_message(message.chat.id, "Сейчас {len(subs_list)} подписок. Сколько вы хотите добавить?")
    if not args:
        return await bot.send_message(message.chat.id, f"Вы добавили подписки. Сейчас подписок {len(subs_list)} ")
    else:
        if args.isdigit():
            args = int(args)
            for i in range(args):
                #print(i)
                subs_list.append(i)
            return await bot.send_message(message.chat.id, f"Вы добавили подписки. Осталось {len(subs_list)} подписок")
        else:
            return await bot.send_message(message.chat.id, "Вы превысили лимит, введите число меньше")



@dp.message_handler( commands = ['start'])
async def send_welcom(message: types.message):
   return await bot.send_message(message.chat.id, "Бот включён")

@dp.message_handler( commands = ['stop'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Анонимный Чат выключен")

@dp.message_handler( commands = ['s'])
async def send_welcom(message: types.message):
    return await bot.send_message(message.chat.id, "Найден человек, чтобы найти нового человека: /next"
                        " чтобы выйти в главное меню: /stop" "Купить подписку /buy")

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

