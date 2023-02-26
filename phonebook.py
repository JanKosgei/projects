#Phonebook App

# Dictionary to store contacts
contacts = {}

#To add contact
def add_contact(name, number):
  # Check whether contact already exists
  if name in contacts:
    print(f"{name} already exists.")
  else:
    contacts[str(name)] = number
    print(f"{name} is added.")

#To delete contact
def delete_contact(name):
  # Check whether contact exists
  if name in contacts:
    del contacts[name]
    print(f"{name} is deleted.")
  else:
    print(f"{name} does not exist.")

#To check whether contact exists
def search_contact(name):
  # Check if contact exists
  if name in contacts:
    print(f"{name}: {contacts[name]}")
  else:
    print(f"{name} does not exist.")

#To print the entire phonebook
def print_all_contacts():
  for name, number in contacts.items():
    print(f"{name}: {number}")


while True:
  print("="*10)
  print("Phonebook App")
  print("="*10)
  print("1. Add Contact")
  print("2. Delete Contact")
  print("3. Search Contact")
  print("4. Print All Contacts")
  print("0. Exit")
  print("="*10)
  choice = input("Enter your choice: ")

  if choice == '1':
    name = input("Enter contact name: ")
    number =int(input("Enter phone number: "))
    add_contact(name, number)
  elif choice == '2':
    name = input("Enter contact name: ")
    delete_contact(name)
  elif choice == '3':
    name = input("Enter contact name: ")
    search_contact(name)
  elif choice == '4':
    print_all_contacts()
  elif choice == '0':
    break
  else:
    print("Invalid choice.")