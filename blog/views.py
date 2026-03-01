from django.shortcuts import render
import datetime


def index(request):
    list1 = ['one', 'two', 'three', 'four', 'five']

    context = {'title': 'first data from context in render',
               'text': 'add some text in P teg',
               'today': datetime.datetime.now(),
               'datalist': list1}
    return render(request, "blog/index.html",context)


def contacts(request):
    context = {
        'title': 'Наші контакти',
         'email': 'admin@sport.com',
         'phone': '+380-97-000-234-56',
         'address': 'Київ, Спортирт Світ, 2 '
    }

    return render(request, "blog/contact.html", context)


def hokey(request):
    context = {'title': 'Хокей',
               'teams': ['Сокіл','Red-Bulls','Fin-comand']
               }
    return render(request, 'blog/hokey.html',context)

def basketball(request):
    context = {'title': 'Баскетбол',
               'teams': ['Barny','Baby','Київські-Пси']
               }
    return render(request, 'blog/backetball.html',context)

def football(request):
    context = {'title': 'Футбол',
               'teams': ['Дінамо','Шахтар','Реал']
               }
    return render(request, 'blog/football.html',context)

def toyota(request):
    context = {
        'brand': 'Toyota',
        'models': ['Camry', 'Corolla', 'RAV4', 'Land Cruiser']
    }
    return render(request, 'blog/toyota.html',context)

def honda(request):
    context = {
        'brand': 'Honda',
        'models': ['Civic', 'Accord','CR-V','HR-V','Pilot']
    }
    return render(request, 'blog/honda.html',context)

def renault(request):
    context = {
        'brand': 'Renault',
        'models': ['Logan','Duster','Megane','Clio','Scenic']
    }
    return render(request, 'blog/renault.html',context)

#------------------------------------------
def day_style(request):

    day_num = datetime.datetime.now().weekday()

    days_names = ['Понеділок','Вівторок','Середа','Четвер','Пятниця','Субота','Неділя']

    bg_colors = [
        '#FF5733', # Понеділок - помаранчевий
        '#33FF57', # Вівторок - зелений
        '#3357FF', #  Середа - синій
        '#F333FF',  # Четвер - фіолетовий
        '#FF33A1', # Пятниця - рожевий
        '#F3FF33', # Субота - жовтий
        '#33FFF3', # Неділя - бірюзовий
    ]
    context = {
        'day_name': days_names[day_num],
        'bg_color': bg_colors[day_num],
    }
    return render(request, 'blog/day_style.html',context)

