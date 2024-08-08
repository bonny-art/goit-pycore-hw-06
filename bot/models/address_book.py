"""
This module provides the AddressBook class, which is used to manage a collection of contact records.

Classes:
- AddressBook: A class that extends UserDict to manage a collection of contact records.
It supports adding, finding, and deleting contacts.

Imports:
- UserDict from collections: A dictionary-like class that allows extension and customization.
- Record from .record: A class representing a contact record, which includes contact name
and phone numbers.

Usage:
- The AddressBook class provides methods to add new contact records, find existing records
by name, and delete records by name.
- Each record in the address book is identified by the contact's name, which is used as
the key in the underlying dictionary.

Example:
    address_book = AddressBook()
    record = Record("John Doe")
    address_book.add_record(record)
    found_record = address_book.find("John Doe")
    address_book.delete("John Doe")
"""

from collections import UserDict

from .record import Record

class AddressBook(UserDict):
    """
    AddressBook is a collection of contact records that allows adding,
    finding, and deleting contacts.

    Methods:
        add_record(record: Record) -> None:
            Adds a new record to the address book.

        find(name: str) -> Record | None:
            Finds and returns a record by the contact's name.

        delete(name: str) -> None:
            Deletes a record from the address book by the contact's name.
    """

    def add_record(self, record: Record) -> None:
        """
        Adds a new record to the address book.

        Args:
            record (Record): The record to be added.
        """
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        """
        Finds and returns a record by the contact's name.

        Args:
            name (str): The name of the contact to find.

        Returns:
            Record | None: The found record or None if not found.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> None:
        """
        Deletes a record from the address book by the contact's name.

        Args:
            name (str): The name of the contact to delete.
        """
        if name in self.data:
            del self.data[name]

    def __str__(self) -> str:
        """
        Returns a string representation of all records in the address book.

        Returns:
            str: A string representing all records in the address book.
        """
        return "\n".join(str(record) for record in self.data.values())
