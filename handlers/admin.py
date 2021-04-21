from aiogram import types
from misc import dp, bot
import sqlite3
from aiogram.dispatcher import FSMContext
from .sqlit import stata_user,delite_user
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID_3 = 941730379 #Бекир

ADMIN_ID =[ADMIN_ID_1,ADMIN_ID_2,ADMIN_ID_3]

class reg(StatesGroup):
    name = State()
    fname = State()
    yname = State()
    step1 = State()

@dp.message_handler(commands=['admin'])
async def admin_ka(message: types.Message):
    id = message.from_user.id
    if id in ADMIN_ID:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Трафик', callback_data='list_members')
        bat_b = types.InlineKeyboardButton(text='Рассылка', callback_data='write_message')
        bat_c = types.InlineKeyboardButton(text='Удалить пользователя', callback_data='del_user')
        markup.add(bat_a, bat_b)
        markup.add(bat_c)
        await bot.send_message(message.chat.id,'Выбери что хочешь сделать:',reply_markup=markup)



@dp.callback_query_handler(text='del_user')
async def delit_user(call: types.callback_query):
    await bot.send_message(chat_id=call.message.chat.id,text='Перешли мне сообщение человека, которого нужно удалить')
    await reg.step1.set()


@dp.message_handler(state=reg.step1,content_types='text')
async def rassilka (message:types.Message,state: FSMContext):
    if message.forward_from == None:
        await bot.send_message(chat_id=message.chat.id, text='У этого пользователя включена приватность, удаление невозможно')
    else:
        a = delite_user(message.from_user.id)
        if a == 1:
            await bot.send_message(chat_id=message.chat.id, text='Удаление пидараса завершено')
        else:
            await bot.send_message(chat_id=message.chat.id, text='Не нашел этого чела в базе')

    await state.finish()


@dp.callback_query_handler(text='list_members')
async def admin_1(call: types.callback_query):
    status = stata_user()
    await bot.send_message(call.message.chat.id, f'Всего пользователей: {status}')



@dp.callback_query_handler(text='write_message')
async def rassilkas (call:types.callback_query,state: FSMContext):
    murkap = types.InlineKeyboardMarkup()
    bat0 = types.InlineKeyboardButton(text='ОТМЕНА',callback_data='otemena')
    murkap.add(bat0)
    await bot.send_message(call.message.chat.id,'Напиши через сколько минут нужно сделать рассылку\n'
                                                'Например:\n\n'
                                                '0 - Рассылка будет выполненна сразу\n\n'
                                                '60 - Через час\n\n'
                                                '1440 - Через день',reply_markup=murkap)
    await reg.name.set()


@dp.message_handler(state=reg.name,content_types='text')
async def rassilka (message:types.Message,state: FSMContext):
    try:
        a = int(message.text)
        await state.update_data(key=a)
        murkap = types.InlineKeyboardMarkup()
        bat0 = types.InlineKeyboardButton(text='ОТМЕНА',callback_data='otemena')
        murkap.add(bat0)
        await bot.send_message(message.chat.id,f'Перешли мне уже готовый пост и я разошлю его всем юзерам через {a} минут',reply_markup=murkap)
        await reg.fname.set()
    except:
        a = await bot.send_message(chat_id=message.chat.id,text='Ты ввел не число!\n\n'
                                                                'Вводи количество минут через которое нужно сделать рассылку')
        await asyncio.sleep(15)
        await bot.delete_message(chat_id=message.chat.id,message_id=a.message_id)

@dp.message_handler(state=reg.fname,content_types=['text','photo','video','video_note'])
async def fname_step(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data = int(data['key'])*60
    await bot.send_message(chat_id=message.chat.id,text=f'Сделаю рассылку через {data/60} Минут')
    await asyncio.sleep(data)
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    await state.finish()
    users = sql.execute("SELECT id FROM user_time").fetchall()
    bad = 0
    good = 0
    await bot.send_message(message.chat.id,
                           f"<b>Всего пользователей: <code>{len(users)}</code></b>\n\n<b>Расслыка начата!</b>",
                           parse_mode="html")
    for i in users:
        await asyncio.sleep(1)
        try:
            await message.copy_to(i[0])
            good += 1
        except:
            bad += 1

    await bot.send_message(
        message.chat.id,
        "<u>Рассылка окончена\n\n</u>"
        f"<b>Всего пользователей:</b> <code>{len(users)}</code>\n"
        f"<b>Отправлено:</b> <code>{good}</code>\n"
        f"<b>Не удалось отправить:</b> <code>{bad}</code>",
        parse_mode="html"
    )

@dp.callback_query_handler(state=reg.name,text='otemena')
async def rassilka_otmena (call:types.callback_query,state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id,chat_id=call.message.chat.id)

@dp.callback_query_handler(state=reg.fname,text='otemena')
async def rassilka_otmena (call:types.callback_query,state: FSMContext):
    await state.finish()
    await bot.delete_message(message_id=call.message.message_id,chat_id=call.message.chat.id)