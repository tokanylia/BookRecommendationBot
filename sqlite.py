import sqlite3


class SQLite:
    def __init__(self, database):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_entry_tbr(self, user_id, isbn):
        with self.connection:
            entry = self.cursor.execute("INSERT INTO books (user, code, status) VALUES (?, ?, ?)",
                                        (user_id, isbn, "TBR"))
            print("TBR entry created")
            return entry

    def create_entry_read(self, user_id, isbn):
        with self.connection:
            entry = self.cursor.execute("INSERT INTO books (user, code, status) VALUES (?, ?, ?)",
                                        (user_id, isbn, "Read"))
            print("`Read` entry created")
            return entry

    def create_entry_rating(self, user_id, isbn, rating):
        with self.connection:
            entry = self.cursor.execute("INSERT INTO books (user, code, rating) VALUES (?, ?, ?)",
                                        (user_id, isbn, rating))
            print("`Rate` entry created")
            return entry

    def update_status_rating(self, user_id, isbn, rating):
        with self.connection:
            entry = self.cursor.execute("UPDATE books SET rating = ? WHERE user = ? AND code = ?",
                                        (rating, user_id, isbn))
            print("`Rate` entry created")
            return entry

    def update_status_tbr(self, user_id, isbn):
        with self.connection:
            entry = self.cursor.execute("UPDATE books SET status = ? WHERE user = ? AND code = ?",
                                        ("TBR", user_id, isbn))
            print("Status was updated to TBR")
            return entry

    def update_status_read(self, user_id, isbn):
        with self.connection:
            entry = self.cursor.execute("UPDATE books SET status = ? WHERE user = ? AND code = ?",
                                        ("Read", user_id, isbn))
            print("Status was updated to Read")
            return entry

    def select_status(self, user_id, isbn):
        with self.connection:
            print("Started selecting status.")
            entry = self.cursor.execute("SELECT status FROM books WHERE user = ? AND code = ?", (user_id, isbn))
            print("Finished.")
            return entry

    def select_rating(self, user_id, isbn):
        with self.connection:
            print("Started selecting ratings.")
            entry = self.cursor.execute("SELECT rating FROM books WHERE user = ? AND code = ?", (user_id, isbn))
            print("Finished.")
            return entry

    def select_tbr(self, user_id):
        with self.connection:
            print("Started selecting TBR books.")
            entry = self.cursor.execute("SELECT code FROM books WHERE user = ? AND status = ?", (user_id, "TBR"))
            print("Finished.")
            return entry

    def select_read(self, user_id):
        with self.connection:
            print("Started selecting TBR books.")
            entry = self.cursor.execute("SELECT code FROM books WHERE user = ? AND status = ?", (user_id, "Read"))
            print("Finished.")
            return entry

    def entry_exists(self, user_id, isbn):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM books WHERE user = ? AND code = ?", (user_id, isbn)).fetchall()
            print("Entry existence checked: ")
            print(bool(len(result)))
            return bool(len(result))

    def tbr_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM books WHERE user = ? AND status = ?", (user_id, "TBR")).fetchall()
            print("Entry existence checked: ")
            print(bool(len(result)))
            return bool(len(result))

    def read_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM books WHERE user = ? AND status = ?", (user_id, "Read")).fetchall()
            print("Entry existence checked: ")
            print(bool(len(result)))
            return bool(len(result))

    def rating_exists(self, user_id, isbn):
        with self.connection:
            result = self.cursor.execute("SELECT rating FROM books WHERE user = ? AND code = ?",
                                         (user_id, isbn)).fetchall()
            print("Rating existence checked: ")
            print(bool(len(result)))
            return bool(len(result))

    def status_exists(self, user_id, isbn):
        with self.connection:
            result = self.cursor.execute("SELECT status FROM books WHERE user = ? AND code = ?",
                                         (user_id, isbn)).fetchall()
            print("Entry existence checked: ")
            print(bool(len(result)))
            return bool(len(result))

    def delete_entry(self, user_id, isbn):
        with self.connection:
            entry = self.cursor.execute("DELETE FROM books WHERE user = ? AND code = ?", (user_id, isbn))
            print("A book has been deleted")
            return entry

    def close(self):
        self.connection.close()
