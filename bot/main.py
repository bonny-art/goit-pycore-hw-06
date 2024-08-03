"""
This module contains the main function for running an assistant bot to manage contacts.

It interacts with the user via command-line input to add, update, display contacts, and more.

Functions:
- main(): Main function to run the assistant bot.
"""
import handlers

from parse_input import parse_input



def main():
    """
    Runs the assistant bot for managing contacts.

    The function continuously prompts the user for commands and processes them accordingly:
    - 'close' or 'exit' to exit the program
    - 'hello' to greet the user
    - 'add' to add a contact
    - 'change' to update a contact
    - 'phone' to display a contact's phone number
    - 'all' to display all contacts

    Uses handlers from the 'handlers' module for contact management.

    Returns:
    None
    """
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input:
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(handlers.add_contact(args, contacts))

        elif command == "change":
            print(handlers.change_contact(args, contacts))

        elif command == "phone":
            print(handlers.show_phone(args, contacts))

        elif command == "all":
            print(handlers.show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
