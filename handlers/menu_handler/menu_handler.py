# обработчики кнопок меню
from main import dp
from keyboards.menu_kb.menu_kb import MyKb
from fsm.menu_fsm import Menu
from fsm.menu_ctrl import MenuCtrl
from keyboards.inline_kb.sch_menu import sch_menu
from keyboards.inline_kb.aud_menu import aud_menu_kb

from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram import types

mn_c = MenuCtrl()
kb = MyKb()

##########################################################################
# Вызов меню


@dp.message_handler(state=Menu.menu_switch)
async def menu_sw(msg: types.Message, state: FSMContext):
    await state.finish()
    await mn_c.menu_level(msg)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")
    await msg.answer("Пожалуйста выберете пункт меню", reply_markup=await MyKb().main_menu())


############################################################################
# First level menu


@dp.message_handler(Text("Расписание занятий"))
async def sch_l_menu(msg: types.Message):
    await mn_c.menu_level(msg)
    await msg.answer("Пожалуйста выберите нужный тип занятий", reply_markup=await MyKb().menu_sch_les())
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")


@dp.message_handler(Text("Репетиционные Аудитории"))
async def aud_menu(msg: types.Message):
    await mn_c.menu_level(msg)
    await msg.answer("Пожалуйста выберите нужную аудиторию", reply_markup=await MyKb().menu_sch_aud())
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")


@dp.message_handler(Text("Info"))
async def main_menu_info(msg: types.Message):
    await mn_c.menu_level(msg)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")


######################################################################################
# Второй уровень меню

# Меню аудиторий


@dp.message_handler(Text("Аудитория А"))
async def aud_a(msg: types.Message):
    await mn_c.menu_level(msg)
    mykb = await aud_menu_kb()
    await msg.answer("Пожалуйста выберете время занятия Аудитория A", reply_markup=mykb)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")


@dp.message_handler(Text("Аудитория B"))
async def aud_a(msg: types.Message):
    mykb = await aud_menu_kb()
    await msg.answer("Пожалуйста выберете время занятия, Аудитория B", reply_markup=mykb)
    await mn_c.menu_level(msg)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")


@dp.message_handler(Text("Назад"))
async def btn_back(msg: types.Message):
    await mn_c.menu_level(msg)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")
    await msg.answer(text='Пожалуйста выберете пункт меню', reply_markup=await MyKb().main_menu())


# Расписание Занятий


@dp.message_handler(Text("Индивидуальные Занятия"))
async def per_les(msg: types.Message):
    await msg.answer(text="Пожалуйста выберете время персональных занятий занятий")


@dp.message_handler(Text("Групповые Занятия"))
async def grp_les(msg: types.Message):
    mykb = await sch_menu()
    await msg.answer(text="Пожалуйста выберете время групповых занятий занятий", reply_markup=mykb)


@dp.message_handler(Text("Вернуться в главное меню"))
async def back_to_main(msg: types.Message):
    await mn_c.menu_level(msg)
    await msg.answer(f"Текущий уровень меню: {mn_c.curr_lvl}")
    await msg.answer("Пожалуйста выберете пункт меню", reply_markup=await MyKb().main_menu())
