from collections import UserDict
import re


def validate_number(func):
    """
    Wrapper function.
    Validates a phone number which must consist of 10 digits
    :param func:
    :return wrapper:
    """
    def inner(*args, **kwargs):
        """
        Handles exception 'ValueError' if the phone number does not consist of 10 digits.
        :param args:
        :param kwargs:
        :return None:
        """
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Phone number must be 10 digits long")

    return inner


class Field:
    """
    Base class for record fields.
    """

    def __init__(self, value: str):
        """
        Initializes a Field object with a given value.
        :param value:
        """
        self.value = value

    def __str__(self):
        """
        Returns the string representation of the field value.
        :return str(self.value):
        """
        return str(self.value)


class Name(Field):
    """
    Class to store contact names. Mandatory field.
    """
    def __init__(self, value: str):
        super().__init__(value)
        self.name = value


class Phone(Field):
    """
    Class to store phone numbers. Validates the phone number using
    validate_phone_number function for thr required format (10 digits).
    """
    def __init__(self, value: str):
        """
        Initializes a Phone object with a given value.
        :param value:
        """
        super().__init__(value)
        self.phone = self.validate_phone_number()

    def validate_phone_number(self):
        """
        Validates the required format (10 digits) of the phone number.
        :return: Raises 'ValueError' if the phone number format is invalid.
        """
        if re.findall(r'^\d{10}$', str(self.value.replace('+38', ''))):
            return self.value
        else:
            raise ValueError("Phone number must be 10 digits long")


class Record:
    """
    Class to store contact information including name and phone numbers.
    """
    def __init__(self, name: str):
        """
        Initializes a Record object with a given name.
        :param name:
        """
        self.name = Name(name.lower())
        self.phones = []

    @validate_number
    def add_phone(self, phone: str):
        """
        Adds a phone number to the contact.
        :param phone:
        :return None:
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone_number: str):
        """
        Removes a phone number from the contact.
        :param phone_number:
        :return None:
        """
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)

    @validate_number
    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        """
        Edits a phone number in the phone list.
        :param old_phone_number:
        :param new_phone_number:
        :return None:
        """
        for p in self.phones:
            if p.value == old_phone_number:
                p.value = Phone(str(new_phone_number))

    def find_phone(self, phone_number: str):
        """
        Searches for a specific phone number in the contact.
        :param phone_number:
        :return phone_number if found, None otherwise:
        """
        for p in self.phones:
            if p.value == phone_number:
                return phone_number

    def __str__(self):
        """
        Returns the string representation of the contact information.
        :return contact string representation:
        """
        return f"Contact name: {self.name.value.title()}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """
    Class to manage and store records in an address book.
    """
    def add_record(self, user: Record):
        """
        Adds a record to the address book.
        :param user:
        :return None:
        """
        self.data[user.name.value] = user

    def find(self, name: str):
        """
        Finds a record in the address book by name.
        :param name:
        :return returns the string representation of the contact information:
        """
        return self.data.get(name.lower())

    def delete(self, name: str):
        """
        Deletes a record from the address book by name.
        :param name:
        :return None:
        """
        if name.lower() in self.data:
            del self.data[name.lower()]
