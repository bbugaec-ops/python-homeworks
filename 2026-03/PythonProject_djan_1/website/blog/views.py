from django.shortcuts import render

def index(request):
    context = {'title': 'First data from context in render',
               'text': 'add some'}
    return render(request, 'blog/index.html')
