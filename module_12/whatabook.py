import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user="root",
passwd="BlueDemon1234!@#",
db="whatabook")

class WhatABookApp:
    def __init__(self):
        self.connection = mysql.connector.connect("whatabook.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Create tables if not exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                email TEXT,
                first_name TEXT,
                last_name TEXT
            )
        ''')
        # Similar creation for books, wishlist, locations tables

    def show_menu(self):
        print("Menu:")
        print("1. View Books")
        print("2. View Store Locations")
        print("3. My Account")
        print("4. Exit Program")

    def show_books(self):
        # Fetch and display books from the database
        pass

    def show_locations(self):
        # Fetch and display store locations from the database
        pass

    def validate_user(self):
        # Prompt user for user_id and validate it against the database
        pass

    def show_account_menu(self):
        print("Account Menu:")
        print("1. Wishlist")
        print("2. Add Book")
        print("3. Main Menu")

    def show_wishlist(self, user_id):
        # Display user's wishlist
        pass

    def show_books_to_add(self, user_id):
        # Display available books that the user can add to their wishlist
        pass

    def add_book_to_wishlist(self, user_id, book_id):
        # Add the selected book to the user's wishlist in the database
        pass

    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_books()
            elif choice == '2':
                self.show_locations()
            elif choice == '3':
                user_id = self.validate_user()
                if user_id:
                    self.show_account_menu()
                    account_choice = input("Enter your choice: ")
                    if account_choice == '1':
                        self.show_wishlist(user_id)
                    elif account_choice == '2':
                        self.show_books_to_add(user_id)
                        book_id = input("Enter the book_id to add: ")
                        self.add_book_to_wishlist(user_id, book_id)
                    elif account_choice == '3':
                        continue
                    else:
                        print("Invalid choice.")
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = WhatABookApp()
    app.run()
