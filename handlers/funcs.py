from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer_photo(FSInputFile("/bot/assets/евген.jpeg"),
    caption="Добрый день, данный бот помогает записаться на прием к <b>Евгению Горюнову</b> -  врачу травматологу-ортопеду МНОЦ МГУ им. М.В.Ломоносова\n\
    /appointment - записаться на прием\n\
    /view - просмотреть свою запись\n\
    /cancel - отменить запись\n\
    /archive - просмотреть прошлые записи\n\
    /message - написать Евгению лично"
    )
    await message.delete()

