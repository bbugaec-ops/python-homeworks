import pickle

filename = 'users.pickle'

def save_data(data):
    with open(filename,'wb') as f:
        pickle.dump(data,f)
    #  change from master    
        

def load_data():
    try:
        with open(filename,'rb') as f:
            return pickle.loads(f)
    except FileNotFoundError:
        return {}
        # change for task 10

def add_user(users):
    login = input("Введіть логін :")
    if login in users:
        print("Такий логін вже є :")
        return
    password = input("Пароль:")
    users[login] = password
    save_data(users)
    print("Користувача додано :")

def remove_user(users):
    login = input("Логін для видалення :")
    if login in users:
        del users[login]
        save_data(users)
        print("Користувача видалено ")
    else:
        print("Такого нема :")

def find_user(users):
    login = input("Логін для пошуку :")
    if login in users:
        print("Пароль:",users[login])
    else:
        print("Не знайдено:")

def edit_user(users):
    login = input("Логін для заміни користувача :")
    if login in users:
        new_pass = input("Новий пароль :")
        users[login] = new_pass
        save_data(users)
        print("Пароль змінено :")
    else:
        print("Не знайдено:")

users = load_data()

while TypeError:
    print("\n.Додати")
    print("2.Видалити")
    print("3.Знайти")
    print("4.Змінити пароль")
    print("0.Вихід")

    choice = input("Ваш вибір")
    # task 10 edit

    if choice == '1':
        add_user(users)
    elif choice == '2':
        remove_user(users)
    elif choice == '3':
        find_user(users)
    elif choice == '4':
        edit_user(users)
    elif choice == '0':
        break
    else:
        print("Невірний вибір :")

