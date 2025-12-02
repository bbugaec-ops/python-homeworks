from os import write

file_name = 'main5.txt'  #   короткий запис

# file = open(file_name,'w')
# file.write('some text')
# file.close()
# try:
#     file = open(file_name, 'r')
#     file.write('some text\n')
# except:
#     print("cant open file ")
# finally:
#     file.close()
#
# file = open(file_name, 'r')
# info = file.read()
# print(info)
# file.close()

# my_list = ['line1\n','line2\n','line3\n']
#
# file = open(file_name,'w')
# file.writelines(my_list)
# file.close()
#
# file = open(file_name)
# file.seek(6)
# print(file.tell())
# data1 = file.read(6)
# print(file.tell())
# data2 = file.read(6)
# print(file.tell())
# print(data1, data2)
# file.close()
#
# print()
#
# with open(file_name,'r') as file:
#      print(file.read())
# try:
#     with open('main.txt','r') as outFile, open('main.txt','w') as inFile:
#         data = outFile.read()
#         inFile.write(data.lower())
# except (FileNotFoundError, FileExistsError) as ex:
#     print(ex)

def add_contact(name, phone):
    try:
        with open('contacts.txt','a',encoding='utf-8') as f:
            f.write(f"{name}: {phone}\n")
        print('New contact added !')
    except Exception as ex:
        print("Error with writing !",ex)

def show_contacts():
    try:
        with open('contacts.txt','r',encoding='utf-8') as f:
            data = f.readlines()
            if not data:
                print("Empty data")
            else:
                print("----------All contacts------------")
                for count in range(1,len(data)+1):
                    print(f"{count}. {data[count-1]}")

    except FileNotFoundError:
        print("File noe found !")


def find_contact(name):
    try:
        with open('contacts.txt','r',encoding='utf-8') as f:
            for line in f:
                if line.lower().startswith(name.lower()):
                    print("Find:",line.strip())
                    return
            print("Not found")
    except FileNotFoundError:
        print("File not found !")


# import  csv
#
# def export_csv(txt_file = "contacts.txt",csv_file = "contacts.csv"):
#     try:
#         contacts = []
#
#         with open(txt_file,"r",encoding="utf-8") as f:
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     name, phone = line.split(":")
#                     contacts.append([name.strip(),phone.strip()])
#         with open(csv_file,'w',encoding="utf-8") as f:
#             writer = csv.writer(f)
#             writer.writerow(['name','phone'])
#             writer.writerows(contacts)
#         print(f"Export finish")
#     except FileNotFoundError:
#         print("File not found")
#     except Exception as ex:
#         print(ex)



def menu():
    while True:
        print("------------------Contact book---------------")
        print("1. Add new")
        print("2.Show all")
        print("3.Exit")

        choice = input("Enter num -")
        if choice == '1':
            name = input("Name")
            phone = input("Phone")
            add_contact(name,phone)
        elif choice == '2':
            show_contacts()
        elif choice == '3':
            break
        elif choice == '4':
            name = input("Name")
            find_contact(name)
        else:
            print("Error menu choice")

menu()


