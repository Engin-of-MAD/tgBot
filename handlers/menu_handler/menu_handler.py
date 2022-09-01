# обработчики кнопок меню
from main import dp
from keyboards.menu_kb.menu_kb import menu_sch_aud, menu_sch_les, main_menu
from fsm.menu_fsm import MenuCtrl


from aiogram.dispatcher import FSMContext
from aiogram import types


async def menu_level(item: str) -> int:
    lvl_menu = 1
    if item == "Расписание занятий":
        lvl_menu += 1
        await MenuCtrl.menu_sch.set()
        return lvl_menu

    elif item == "Репетиционные Аудитории":
        lvl_menu += 1
        await MenuCtrl.menu_aud.set()
        return lvl_menu

    elif item == "Info" and lvl_menu == 1:
        await MenuCtrl.menu_info.set()
        return lvl_menu


##########################################################################
# Вызов меню


@dp.message_handler(state=MenuCtrl.menu_switch)
async def menu_sw(msg: types.Message, state: FSMContext):
    await msg.answer("Пожалуйста выберете пункт меню", reply_markup=await main_menu())
    cur_lvl = await menu_level(msg.text)
    await state.update_data(lvl_menu=cur_lvl)


############################################################################
# First level menu


@dp.message_handler(state=MenuCtrl.menu_sch)
async def sch_l_menu(msg: types.Message, state: FSMContext):
    kb = await menu_sch_les()
    await msg.answer("Пожалуйста выберите нужный тип занятий", reply_markup=kb)
    data = await state.get_data()
    await msg.answer(f"Текущий уровень меню: {data['lvl_menu']}")


@dp.message_handler(state=MenuCtrl.menu_aud)
async def aud_menu(msg: types.Message):
    kb = await menu_sch_aud()
    await msg.answer("Пожалуйста выберите нужную аудиторию", reply_markup=kb)
