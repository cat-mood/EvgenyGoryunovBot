from aiogram import Router
from aiogram import types
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.types import FSInputFile
from aiogram import Bot
from keyboards import start

router = Router()

Master_id = 413784019

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = start.start_kb()
    await message.answer_photo(FSInputFile("/bot/assets/евген.jpeg"),
    caption="Добрый день, данный бот помогает записаться на прием к <b>Евгению Горюнову</b> -  врачу травматологу-ортопеду МНОЦ МГУ им. М.В.Ломоносова\n\
    /appointment - записаться на прием\n\
    /view - просмотреть свою запись\n\
    /cancel - отменить запись\n\
    /archive - просмотреть прошлые записи\n\
    /message - написать Евгению лично", reply_markup=kb)

@router.message(Command("message"))
async def cmd_mes(message: Message):
    await message.answer("Напишите ваш вопрос ниже.\
 Как только ответ будет получен, он сразу же появится у вас в этом чате", reply_markup=types.ReplyKeyboardRemove())
