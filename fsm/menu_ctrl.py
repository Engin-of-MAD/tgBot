from .menu_fsm import MenuCtrl


async def menu_level(item: str, lvl_menu=1) -> int:
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
