from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views import View


def get_menu():
    return """
       <a href='/'>home</a>
       <a href='/datetime'>time</a>
    """

def index(request):
    return HttpResponse(get_menu()+ f"""
         <h1>Hello from my first views function!</h1>
    
    """)

data = [1,2,3,4,5]

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(get_menu()+ f"""
         <h1>Current datetime : {now} </h1>
         <p>Data {data} </p>
    """)

class CurrentDateTime(View):

    def get(self, request):
        now = datetime.datetime.now()
        return HttpResponse(f"""
             <h1>Current datetime : {now} </h1>
             <p>Data {data} </p>
        """)

def citata(request):

    return HttpResponse("""
        <h2>Життя не поле перейти</h2>
    """)

