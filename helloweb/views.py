from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import datetime

def get_menu():
    return """
        <a href='/'> home </a>
        <a href='/datetime'>time</a>
    """


def index(request):
    return HttpResponse(get_menu()+""""
          <h1>Hello from my first views function ! </h1>
          """)

data = [1,2,3]

def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(get_menu() + f"""
           <h1>Current datetime : {now}</h1>
           <p>Data : {data}</p>
    """)

class CurrentDateTime(View):

        def get(self,request):
            now = datetime.datetime.now()
            return HttpResponse( get_menu() + f"""
                   <h1>Current datetime : {now}</h1>
                   <p>Data : {data}</p>
            """)

def citata(request):
    now = datetime.datetime.now()
    return HttpResponse( get_menu() + f"""
                <h1>Те що зломало тебе сьогодні , може стати твоєю силою завтра .</h1>
            """)

