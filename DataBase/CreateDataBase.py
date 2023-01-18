import sqlite3 as sl

class CreateDataBase:
    def __init__(self, name: str) -> None:
        self.con = sl.connect(name + '.db')
        self.cur = self.con.cursor()

    # Values is a list of tuple that the first element is Name and the second is Type.
    def addTable(self, name: str, values: list) -> None:
        comand = 'CREATE TABLE ['+ name +'] ('
        for value in values:
            comand += value[0] + ' ' + value[1] + ','
        comand += ');'

    # Close the cursor.
    def removeCursos(self) -> None:
        self.cur.close