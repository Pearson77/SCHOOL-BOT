import sqlite3

db = sqlite3.connect("database.db")
cursor = db.cursor()
array = cursor.execute(f"SELECT n2 FROM inf_answers WHERE rowid > '0'").fetchall()
print(array)
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
        array = self.c.execute(f"SELECT * FROM {var_type}_answers, WHERE rowid = '{variant}'").fetchall()
        print(array)
        return self.db.commit(), self.db.close()

    def find_answers_by_number(self, number, var_type):
        array = self.c.execute(f"SELECT '{number}' FROM {var_type}_answers").fetchall()
        print(array)
        return self.db.commit(), self.db.close()

    def find_files_by_request(self, request):
        ...
        return self.db.commit(), self.db.close()

    def find_files_by_number(self, number):
        ...
        return self.db.commit(), self.db.close()
