import sqlite3
import random
from typing import List, Optional

class Storage:
    def __init__(self, db_path: str = 'quotes.db'):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS quotes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    quote TEXT NOT NULL
                )
            ''')
            conn.commit()

    def add_quote(self, quote: str):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO quotes (quote) VALUES (?)', (quote,))
            conn.commit()

    def get_all_quotes(self) -> List[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT quote FROM quotes')
            quotes = [row[0] for row in cursor.fetchall()]
        return quotes

    def get_random_quote(self) -> Optional[str]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT quote FROM quotes')
            quotes = [row[0] for row in cursor.fetchall()]
            if quotes:
                return random.choice(quotes)
            return None

