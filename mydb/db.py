import pymysql.cursors


class MyDB:
    db = None

    def __init__(self):
        self.db = pymysql.connect(database="users",
                                  host="localhost",
                                  password="qwerty123F!",
                                  user="root")

    def gen_p_col(self, p: list):
        s = str()
        for i in p:
            s = s + i + ", "
        s = s[:-2]
        return s

    def gen_p_val(self, p: list):
        s = str()
        for i in p:
            s = s + f"\"{i}\"" + ", "
        s = s[:-2]
        return s

    async def ger_from_stud(self, **kwargs):
        curr = self.db.cursor()
        colum: list = list()
        value: list = list()
        for key in kwargs:
            value.append(kwargs[key])
            colum.append(key)
        col = self.gen_p_col(colum)
        val = self.gen_p_val(value)

    async def insert_to_stud(self, **kwargs):
        curr = self.db.cursor()
        colums: list = list()
        values: list = list()
        for key in kwargs:
            values.append(kwargs[key])
            colums.append(key)
        col = self.gen_p_col(colums)
        val = self.gen_p_val(values)
        curr.execute(f"INSERT students({col}) VALUES({val})")
        self.db.commit()
