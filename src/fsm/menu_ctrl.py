from aiogram import types


class MenuCtrl:
    curr_lvl = 1

    async def menu_level(self, msg: types.Message) -> int:
        if msg.text == "Расписание занятий":
            self.curr_lvl += 1
            return self.curr_lvl

        elif msg.text == "Репетиционные Аудитории":
            self.curr_lvl += 1
            return self.curr_lvl

        elif msg.text == "Info" and self.curr_lvl == 1:
            await msg.answer("Какая-то инфа 1")
            return self.curr_lvl

        elif msg.text == "Info" and self.curr_lvl == 2:
            await msg.answer("Какая-то инфа о меню аудиторий")
            return self.curr_lvl

        elif msg.text == "Аудитория А":
            self.curr_lvl += 1
            return self.curr_lvl

        elif msg.text == "Аудитория B":
            self.curr_lvl = 1
            return self.curr_lvl

        elif msg.text == "Назад":
            self.curr_lvl -= 1
            return self.curr_lvl

        elif msg.text == "Вернуться в главное меню":
            self.curr_lvl = 1
            return self.curr_lvl
