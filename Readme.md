# Task_1
# Simple Contact Manager

This project is a simple assistant bot for managing your contact list via the command line. You can add, change, and retrieve phone numbers of your contacts.

## Usage

1. **Add a contact:**
   ```bash
   add <name> <phone number>
   ```
   Example:
   ```bash
   add John Doe 123-456-7890
   ```

2. **Change a contact:**
   ```bash
   change <name> <new phone number>
   ```
   Example:
   ```bash
   change John Doe 987-654-3210
   ```

3. **Get a phone number:**
   ```bash
   phone <name>
   ```
   Example:
   ```bash
   phone John Doe
   ```

4. **Get all phone numbers:**
   ```bash
   all
   ```

5. **Exit the program:**
   ```bash
   close
   ```
   Or
   ```bash
   exit
   ```

6. **Help:**
   ```bash
   help
   ```

## Dependencies

- Python 3.x

## How to Run

```bash
python task_1.py
```

__________
__________
__________


# Task_2
# Address Book

This Python script implements an address book using OOP.
That allows users to store contact information, including names and phone numbers.

## Usage

Here is a simple step by step description of the code.

1. **Import the Required Libraries**

    ```python
    from collections import UserDict
    import re
    ```

2. **Define Validator Function**

    The `validate_number` function is a decorator used to validate phone numbers and ensure they consist of 10 digits.

3. **Classes**

    - **Field**

        - Base class for record fields.
        
    - **Name**

        - Class to store contact names. A mandatory field.
        
    - **Phone**

        - Class to store phone numbers. Validates the phone number using the `validate_phone_number` function for the required format (10 digits).
        
    - **Record**

        - Class to store contact information including name and phone numbers. Allows addition, removal, editing, and retrieval of phone numbers associated with a contact.
        
    - **AddressBook**

        - Class to manage and store records in an address book. It supports adding, finding, and deleting records based on the contact's name.

## Classes and Methods Overview

- **Field**

    - `__init__(self, value: str)`: Initializes a Field object with a given value.
    
    - `__str__(self)`: Returns the string representation of the field value.

- **Name**

    - Inherits from `Field`.
    
    - `__init__(self, value: str)`: Initializes a Name object with a given value.

- **Phone**

    - Inherits from `Field`.
    
    - `__init__(self, value: str)`: Initializes a Phone object with a given value.
    
    - `validate_phone_number(self)`: Validates the required format (10 digits) of the phone number.

- **Record**

    - `__init__(self, name: str)`: Initializes a Record object with a given name.
    
    - `add_phone(self, phone: str)`: Adds a phone number to the contact.
    
    - `remove_phone(self, phone_number: str)`: Removes a phone number from the contact.
    
    - `edit_phone(self, old_phone_number: str, new_phone_number: str)`: Edits a phone number in the phone list.
    
    - `find_phone(self, phone_number: str)`: Searches for a specific phone number in the contact.
    
    - `__str__(self)`: Returns the string representation of the contact information.

- **AddressBook**

    - Inherits from `UserDict`.
    
    - `add_record(self, user: Record)`: Adds a record to the address book.
    
    - `find(self, name: str)`: Finds a record in the address book by name.
    
    - `delete(self, name: str)`: Deletes a record from the address book by name.

## Example Usage

```python
# Create a new address book
my_address_book = AddressBook()

# Create a new record
new_contact = Record("John Doe")

# Add a phone number to the contact
new_contact.add_phone("1234567890")

# Add the record to the address book
my_address_book.add_record(new_contact)

# Find and display a contact
found_contact = my_address_book.find("John Doe")
if found_contact:
    print(found_contact)
else:
    print("Contact not found")

# Delete a contact
my_address_book.delete("John Doe")
```
---
GitHub: [BalakaMd](https://github.com/BalakaMd)
