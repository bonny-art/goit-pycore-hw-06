"""
This module provides functions to manage a dictionary of contacts where each contact
is represented by a name and a phone number.

Functions:
- add_contact(args: list[str], contacts: Dict[str, str]) -> str:
  Adds a new contact with the given name and phone number to the contacts dictionary.

- change_contact(args: list[str], contacts: Dict[str, str]) -> str:
  Updates the phone number of an existing contact in the contacts dictionary.

- show_phone(args: list[str], contacts: Dict[str, str]) -> str:
  Retrieves the phone number of a contact from the contacts dictionary.

- show_all(contacts: Dict[str, str]) -> Union[str, Dict[str, str]]:
  Retrieves all contacts stored in the contacts dictionary.

Usage:
This module can be imported and used in other Python scripts to manage a collection
of contacts. Each function handles specific operations related to adding, updating,
and retrieving contact information.
"""
from typing import Dict, Union
from input_error import input_error

@input_error
def add_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Add a new contact with the given name and phone number to the contacts dictionary.

    Parameters:
    args (list[str]): List of arguments containing name and phone number.
    contacts (Dict[str, str]): Dictionary containing contacts where keys are names and
    values are phone numbers.

    Returns:
    str: Success or error message indicating whether the contact was added successfully
    or if it already exists.
    """

    name, phone = args

    if name in contacts:
        return f"Contact {name} is already in contacts."

    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Update the phone number of an existing contact in the contacts dictionary.

    Parameters:
    args (list[str]): List of arguments containing name and new phone number.
    contacts (Dict[str, str]): Dictionary containing contacts where keys are
    names and values are phone numbers.

    Returns:
    str: Success or error message indicating whether the contact was updated
    successfully, already has the same number, or if it was not found.
    """
    name, phone = args

    if contacts[name] == phone:
        return f"Contact {name} already has this phone number."

    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: list[str], contacts: Dict[str, str]) -> str:
    """
    Retrieve the phone number of a contact from the contacts dictionary.

    Parameters:
    args (list[str]): List of arguments containing the name of the contact.
    contacts (Dict[str, str]): Dictionary containing contacts where keys are
    names and values are phone numbers.

    Returns:
    str: Phone number of the contact if found, otherwise a message indicating
    the contact was not found.
    """
    if len(args) > 1:
        return "Give me only name."

    name = args[0]
    return contacts[name]

@input_error
def show_all(contacts: Dict[str, str]) -> Union[str, Dict[str, str]]:
    """
    Retrieve all contacts stored in the contacts dictionary.

    Parameters:
    contacts (Dict[str, str]): Dictionary containing contacts where keys
    are names and values are phone numbers.

    Returns:
    Union[str, Dict[str, str]]: A string indicating no contacts
    if the dictionary is empty, otherwise returns the contacts dictionary.
    """
    if not contacts:
        return "No contacts."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

if __name__ == "__main__":
    print()

    contacts_list = {}

    # Test show_all
    # Should show all contacts
    print(show_all(contacts_list))
    print()

    # Test add_contact
    print('Test add_contact >>>')
    # Should add contact successfully
    print(add_contact(["John", "123456789"], contacts_list))
    # Should indicate contact already exists
    print(add_contact(["John", "987654321"], contacts_list))
    # Should indicate invalid arguments
    print(add_contact(["John"], contacts_list))
    # Should indicate invalid arguments
    print(add_contact([], contacts_list))
    print()

    # Test change_contact
    print('Test change_contact >>>')
    # Should update contact successfully
    print(change_contact(["John", "987654321"], contacts_list))
    # Indicates that contact already has this phone number
    print(change_contact(["John", "987654321"], contacts_list))
    # Should indicate contact not found
    print(change_contact(["Mary", "456789123"], contacts_list))
    # Should indicate invalid arguments
    print(change_contact(["John"], contacts_list))
    # Should indicate invalid arguments
    print(change_contact([], contacts_list))
    print()

    # Test show_phone
    print('Test show_phone >>>')
    # Should show phone number for John
    print(show_phone(["John"], contacts_list))
    # Should indicate contact not found
    print(show_phone(["Mary"], contacts_list))
    # Should indicate invalid arguments
    print(show_phone(["John", "Mary"], contacts_list))
    # Should indicate invalid arguments
    print(show_phone([], contacts_list))
    print()

    # Test show_all
    # Should show all contacts
    print(show_all(contacts_list))
    print()
