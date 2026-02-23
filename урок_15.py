
def add_contact(name, phone):
    try:
        with open('contacts.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name}: {phone}\n")
        print("New contact added!")
    except Exception as ex:
        print("Error with writing !", ex)


def show_contacts():
    try:
        with open('contacts.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            if not data:
                print("Empty data!")
            else:
                print("----------- All contacts -------------")
                for count in range(1, len(data) + 1):
                    print(f"{count}. {data[count - 1]}")
    except FileNotFoundError:
        print("File noe found !")


def find_contact(name):
    try:
        with open("contacts.txt", 'r', encoding='utf-8') as f:
            for line in f:
                if line.lower().startswith(name.lower()):
                    print("Find:", line.strip())
                    return
            print("Not found !")
    except FileNotFoundError:
        print("File not found !")


def del_contact(name):
    try:
        with open("contacts.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        new_lines = []
        found = False
        for line in lines:
            if not line.lower().startswith(name.lower()):
                new_lines.append(line)
            else:
                found = True
        if not found:
            print("Contact not found for delete !")
        with open("contacts.txt", 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print("Contact delete !")
    except FileNotFoundError:
        print("File not found !")


import csv


def export_to_csv(txt_file="contacts.txt", csv_file="contacts.csv"):
    try:
        contacts = []

        with open(txt_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    name, phone = line.split(":")
                    contacts.append([name.strip(), phone.strip()])
        with open(csv_file, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(['name', 'phone'])
            writer.writerows(contacts)
        print(f"Export finish!")
    except FileNotFoundError:
        print("File not found !")
    except Exception as ex:
        print(ex)


def menu():
    while True:
        print("------------ Contact book ----------------")
        print("1. Add new ")
        print("2. Show all ")
        print("3. Exit ")

        choice = input("Enter num - ")
        if choice == '1':
            name = input("Name: ")
            phone = input("Phone - ")
            add_contact(name, phone)
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            break
        elif choice == '4':
            name = input("Name: ")
            find_contact(name)
        elif choice == '5':
            name = input("Name for del: ")
            del_contact(name)
        elif choice == '6':
            export_to_csv()
        else:
            print("Error menu choice !")


menu()