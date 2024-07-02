import mysql.connector
from mysql.connector import Error
import re
import sys

class LibraryManagementSystem:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                database='library_management'
            )
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
        except Error as e:
            print("Error while connecting to MySQL", e)
            sys.exit(1)

    def add_new_book(self, title, author, isbn):
        query = "INSERT INTO books (title, author, isbn, availability) VALUES (%s, %s, %s, %s)"
        values = (title, author, isbn, True)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Book added successfully.")

    def add_new_user(self, name, email):
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("User added successfully.")

    def borrow_book(self, user_id, book_id, borrow_date):
        query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
        values = (user_id, book_id, borrow_date)
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Book borrowed successfully.")

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System with Database Integration!")
            print("****\nMain Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Go back")
            choice = input("Enter your choice: ")
            if choice == '1':
                title = input("Enter the title of the book: ")
                author = input("Enter the author of the book: ")
                isbn = input("Enter the ISBN of the book: ")
                self.add_new_book(title, author, isbn)
            if choice == '2':
                user_id = input("Enter the user ID: ")
                book_id = input("Enter the book ID: ")
                borrow_date = input("Enter the borrow date (YYYY-MM-DD): ")
                self.borrow_book(user_id, book_id, borrow_date)
            if choice == '3':
                book_id = input("Enter the book ID: ")
                query = "DELETE FROM borrowed_books WHERE book_id = %s"
                values = (book_id,)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Book returned successfully.")
            if choice == '4':
                title = input("Enter the title of the book: ")
                query = "SELECT * FROM books WHERE title = %s"
                values = (title,)
                self.cursor.execute(query, values)
                record = self.cursor.fetchone()
                print("Book details:")
                print(record)
            if choice == '5':
                query = "SELECT * FROM books"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                print("All books in the library:")
                for record in records:
                    print(record)
            if choice == '6':
                break
    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Go back")
            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter the name of the user: ")
                email = input("Enter the email of the user: ")
                self.add_new_user(name, email)
            if choice == '2':
                user_id = input("Enter the user ID: ")
                query = "SELECT * FROM users WHERE id = %s"
                values = (user_id,)
                self.cursor.execute(query, values)
                record = self.cursor.fetchone()
                print("User details:")
                print(record)
            if choice == '3':
                query = "SELECT * FROM users"
                self.cursor.execute(query)
                records = self.cursor.fetchall()
                print("All users in the library:")
                for record in records:
                    print(record)
            if choice == '4':
                break



if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.main_menu()