from datetime import date


class DateCheck:

    week = {1: "Понедельник", 2: "Вторник",
            3: "Среда", 4: "Четверг",
            5: "Пятница", 6: "Суббота",
            7: "Воскресенье"}

    day = None
    month = None
    year = None
    today_wk_d = None
    future_day = None
    m_dt = None

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.today_wk_d = date(day=day, month=month, year=year).isoweekday()

    @staticmethod
    def date_upd(day, month):

        month_0 = [4, 6, 9, 11]
        month_1 = [1, 3, 5, 7, 8, 10, 12]
        # month_89 = 2
        for i in month_1:
            data = {}
            if month == i:
                if day > 31:
                    day += 7
                    day = day - 31
                    month += 1
                    data.update(day=day, month=month)
                    return data
                else:
                    data.update(day=day, month=month)
                    return data

        for j in month_0:
            data = {}
            if month == j:
                if day >= 1 and day > 30:
                    day = day - 30
                    print(day)
                    data.update(day=day, month=month)
                    print(data)

            return data

    def chk_week(self, week_day):
        if self.today_wk_d >= week_day:
            return True
        else:
            return False

    def set_date(self, inp):
        if self.chk_week(inp):
            data = self.date_upd(self.day, self.month)
            dt = date(day=data["day"], month=data["month"], year=self.year)
            self.future_day = dt.isoweekday()
            self.m_dt = dt
        else:
            dl = inp - self.today_wk_d
            day = self.day + dl
            dt_upd = self.date_upd(day, self.month)
            dt = date(day=dt_upd["day"], month=dt_upd["month"], year=self.year)
            self.future_day = dt.isoweekday()
            self.m_dt = dt

    def get_date(self):
        return self.m_dt.strftime("%Y-%m-%d")
