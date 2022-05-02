import sqlite3


class BaseOperations:
    """The class connects to the database and is responsible for manipulating it"""
    __arithmetic_expression = ''

    def __init__(self):
        """On instantiation, connects the database and creates a cursor"""
        self.conn = sqlite3.connect('base_operation.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def generate_operation(self, number_1, sign, number_2):
        """Generates a mathematical expression for all characters except squaring and square root"""
        self.__arithmetic_expression += f'{number_1} {sign} {number_2} = '

    def result_operation(self, result):
        """Adds an expression and a value to the database"""
        self.__arithmetic_expression += f'{result}'
        self.add_operation_in_table()

    def generate_sqr_mul_in_table(self, number, sign):
        """Generates a mathematical expression for squaring and taking the square root"""
        if sign == '\u00B2':
            self.__arithmetic_expression = f'({number})\u00B2 = '
        else:
            self.__arithmetic_expression = f'\u221A({number}) = '

    def read_table(self):
        """Returns arithmetic expressions from a table in a database"""
        self.cursor.execute('''SELECT operation FROM base_operation''')
        return [operation[0] for operation in self.cursor.fetchall()]

    def add_operation_in_table(self):
        """Adds an expression to the database and clears the expression"""
        self.cursor.execute('''INSERT INTO base_operation(operation) VALUES (?)''', (self.__arithmetic_expression,))
        self.conn.commit()
        self.__arithmetic_expression = ''

    def drop_table(self):
        """Deletes a table in a database"""
        self.cursor.execute('''DROP TABLE base_operation''')

    def clean_table(self):
        """Clears a table in the database"""
        self.cursor.execute('''DELETE FROM base_operation''')
        self.conn.commit()

    def create_table(self):
        """Creates a table in the database to store arithmetic operations"""
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS base_operation(id INTEGER PRIMARY KEY AUTOINCREMENT, operation TEXT)''')
