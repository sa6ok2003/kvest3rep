from aiogram import types
from misc import dp,bot
import sqlite3
from .sqlit import reg_user,delite_user,cheack_ban
import asyncio

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID_3 = 941730379 #Бекир


video_qiwi = 'BAACAgIAAxkBAAMIYG14XMsjJiVlyOpWIfbpfaGFhGAAAt0JAAIT9lFK-_QP4YN0GC8eBA'
video1 = 'BAACAgIAAxkBAAMJYG14gy6uCKd1vOZYRvrXP2s0-8IAAoYMAAJHORlK37pSMh2Y68oeBA'
video2 = 'BAACAgIAAxkBAAMKYG14rdNW_8EX3GgFwm8hPi1djEgAAp8KAAJbcShKYgABZ-wn0YeOHgQ'
message_opisabie ="""<b>👋Всем привет👋</b>

На связи Бекир
<i>Специально для Вас, мы дадим на «0» этап несколько этапов из первого квеста.</i> <b>Задания и розыгрыши озвученные в видео недействительны! </b>
<u>Вы говорили что дадите топовый сайт для зароботка❓</u>
Самый топовый заработок на сайтах в интернете – это без всяких сомнений Qcomment!
Конечно вы можете сказать что этот сайт не самый высокооплачиваемый среди всех остальных, но у него есть плюсы которые это перекрывают. К примеру, это система рангов, при грамотном прокачивании аккаунта можно зарабатывать хорошие деньги выполняя простые задания. Также один из множества плюсов что можно зарабатывать не только в рублях но и в долларах. И конечно не могу не отметить что сайт стабильно выводить деньги, без каких либо проблем!
Итак для работы на данном сайте нам потребуются следующие социальные сети:
- Facebook
- Instagram 
- Vkontakte
- Odnoklassniki 
Регистрируемся по этой ссылке:
https://qcomment.ru/rsignup/2825081
<u>Почему реферальная ссылка❓</u>
Мы не пытаемся на вас заработать, только по реферальной ссылке мы сможем проверить информацию для розыгрыша специалеы приза в конце «0» этапа.
<u>Денежный приз❓</u>
Ооо да!
<u>Расскажите подробнее❓</u>
Все что нужно, это зарегистрироваться по нашей ссылке и заработать максимально много денег для себя до начала «1» этапа квеста. Призовых мест 5.
1️⃣ место 500 руб
2️⃣ место 400 руб
3️⃣ место 300 руб
4️⃣ место 200 руб
5️⃣ место 100 руб
То самое чувство когда можешь восстановить потраченные деньги на квесте🤑
<b>Ну что медлишь?</b> Быстрее приступай🚀 и будь в числе победителей✊"""


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(message.chat.id)
    if cheack_ban(message.chat.id) != 0:
        murkap =types.InlineKeyboardMarkup()
        bat1 = types.InlineKeyboardButton(text='ПРОШЕЛ', callback_data='start1')
        murkap.add(bat1)
        await bot.send_message(message.chat.id, """ Привет👋
Пройдите небольшой опрос👇
https://docs.google.com/forms/d/e/1FAIpQLSeNCwg_LfUuQfDNBIVke8arZFlw9vH_G_cGHNB8Q-AgV7sE2g/viewform?usp=sf_link
Эти данные нужны будут для финального розыгрыша❗ """,parse_mode='html',reply_markup=murkap,disable_web_page_preview=True)
    else:
        print('Участник удален')

@dp.callback_query_handler(text = 'start1')
async def cal_start1(call: types.callback_query):
    murkap = types.InlineKeyboardMarkup()
    bat1 = types.InlineKeyboardButton(text='ДАЛЕЕ', callback_data='start2')
    murkap.add(bat1)
    await bot.send_video(chat_id=call.message.chat.id,video=video_qiwi,caption="""🥝Для дальнейшей работы нам потребуется киви кошелек, для его создания нам потребуются паспортные данные России.
📋Краткий план , как создать киви кошелек:
1. Скачиваем приложение (Playmaker/ Appstore)
2. Регистрируемся на любой номер (Не обязательно на Российский)
3. Переходим на сайт Реестр Налогов, и получаем данные паспорта РФ
https://www.reestr-zalogov.ru/search/index
4. Обратно идем в киви кошелёк, и с помощью этих данных повышаем статус киви до основного
📰Более подробная , но немного сложная статья по регистрации киви:
https://telegra.ph/Dobycha-pasportov-dlya-identifikacii-01-26
📹Так же для вас Лена сняла видео , как она верефицирует свой киви кошелек""",reply_markup=murkap)

@dp.callback_query_handler(text = 'start2')
async def cal_start1(call: types.callback_query):

    await bot.send_video(chat_id=call.message.chat.id,video=video1)
    await asyncio.sleep(433)
    await bot.send_video(chat_id=call.message.chat.id, video=video2)
    await asyncio.sleep(513)
    await bot.send_message(chat_id=call.message.chat.id, text=message_opisabie,parse_mode='html')
    await asyncio.sleep(30)
    await bot.send_message(chat_id=call.message.chat.id,text=f'В этой статье скорее всего есть ответ на твой вопрос:\n\n'
                                                             f'https://telegra.ph/Otvety-na-chasto-zadavaemye-voprosy-03-07-3',disable_web_page_preview=True)
    await bot.send_message(chat_id=call.message.chat.id,text="""На этом 🅾️ этап завершен🎉
Первый этап квеста начнётся с набором 500 участников 😉
Участвуй в розыгрыше, я уверен у тебя все получится✊""")

@dp.message_handler(commands=['del'])
async def delite_user2(message: types.Message):
    a = delite_user(message.chat.id)
    if a == 1 :
        await bot.send_message(chat_id= ADMIN_ID_1, text='Удалился юзер из квеста 2')
        await bot.send_message(chat_id=ADMIN_ID_2, text='Удалился юзер из квеста 2')
        await bot.send_message(chat_id=ADMIN_ID_3, text='Удалился юзер из квеста 2')
