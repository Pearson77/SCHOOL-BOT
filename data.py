import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()
# cursor.execute("""CREATE TABLE inf_answers (
# '1' TEXT,
# '2' TEXT,
# '3' TEXT,
# '4' TEXT,
# '5' TEXT,
# '6' TEXT,
# '7' TEXT,
# '8' TEXT,
# '9' TEXT,
# '10' TEXT,
# '11' TEXT,
# '12' TEXT,
# '13' TEXT,
# '14' TEXT,
# '15' TEXT,
# '16' TEXT,
# '17' TEXT,
# '18' TEXT,
# '19' TEXT,
# '20' TEXT,
# '21' TEXT,
# '22' TEXT,
# '23' TEXT,
# '24' TEXT,
# '25' TEXT,
# '26' TEXT,
# '27' TEXT
# )""")
db.commit()
db.close()


class Data:
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.c = self.db.cursor()

    def find_answers_by_variant(self, variant, var_type):
        array = self.c.execute(f"SELECT * FROM {var_type}_answers WHERE rowid = '{variant}'").fetchall()
        answers = ""
        for i in range(len(array[0])):
            if i != 24:
                answers += f"<b>Задание №{i+1}</b>:<code>\t{array[0][i]}</code>\n"
            else:
                a = "\n"
                answer = array[0][i].split()
                for j in range(len(answer)):
                    if j % 2 == 0:
                        a += f"{answer[j]} — "
                    else:
                        a += f"{answer[j]}\n"
                answers += f"<b>Задание №25</b>: <code>{a}</code>"

        return self.db.commit(), self.db.close(), answers

    def find_answers_by_number(self, number, var_type):
        array = self.c.execute(f"SELECT n{number} FROM {var_type}_answers").fetchall()
        answers = ""
        for i in range(len(array)):
            answers += f"<b>Вариант №{i+1}</b>:<code>\t{array[i][0]}</code>\n"
        return self.db.commit(), self.db.close(), answers

    def find_files_by_request(self, request):
        ...
        return self.db.commit(), self.db.close()

    def find_files_by_number(self, number):
        ...
        return self.db.commit(), self.db.close()
