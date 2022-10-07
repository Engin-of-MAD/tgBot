from aiogram import types


async def adm_start(message: types.Message):
    await message.answer(text="Добро пожаловать")


async def adm_help(msg: types.Message):
    list_cmd = f"Список команд:\n" \
               f"/stat - вывод статистики\n" \
               f"/upload - выгрузка базы данных\n" \
               f"/format - формат базы данных\n"
    await msg.answer(list_cmd)
