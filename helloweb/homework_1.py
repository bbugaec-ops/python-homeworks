from django.http import HttpResponse

def get_menu():
    return """
    <div style="background-color: #f8f9fa; padding: 15px; border-bottom: 2px solid #ddd; text-align: center; font-family: sans-serif;">
        <a href="/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Головна</a> |
        <a href="/news/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Новини</a> |
        <a href="/management/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Голови</a> |
        <a href="/facts/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Факти</a> |
        <a href="/contacts/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Контакти</a> |
        <a href="/history/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Історія</a> |
        <a href="/history/people/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Мешканці</a> |
        <a href="/history/photos/" style="margin: 10px; text-decoration: none; color: blue; font-weight: bold;">Фото</a>
    </div>
    <hr>
    """



def home(request):
    return HttpResponse(get_menu() + "<h1>Головна сторінка міста</h1>")


def news(request):
    return HttpResponse(get_menu() + """
        <h1>Новини міста</h1>
        <p><b>Сьогодні:</b> У Романові розпочато благоустрій парків і ДОРІГ.</p>
    """)

def management(request):
    return HttpResponse(get_menu() + """
        <h1>Керівництво міста</h1>
        <p><b>Голова громади:</b> Кондратюк Віктор Сергійович</p>
    """)

def facts(request):
    return HttpResponse(get_menu() + """
        <h1>Факти про місто</h1>
        <ul>
            <li>Романів заснований у 1471 році.</li>
            <li>Місто славиться своєю історією і природою.</li>
            <li>А ще дорогами кожен рік і владою , яка переживає за народ:</li>
        </ul>
    """)

def contacts(request):
    return HttpResponse(get_menu() + """
        <h1>Контактні телефони міських служб</h1>
        <ul>
            <li><b>Поліція:</b> 102</li>
            <li><b>Швидка:</b> 103</li>
            <li><b>Пожежна:</b> 101</li>
        </ul>
    """)

def history(request):
    return HttpResponse(get_menu() + "<h1>Історія Романова</h1><p>Романів заснований у 1471 році як замок-фортеця.</p>")


def history_people(request):
    return HttpResponse(get_menu() + "<h1>Відомі мешканці:</h1><p>У Нашому місті жили та працювали видатні люди свого часу.</p>")


def history_photos(request):
    html_code = get_menu() + """
    <div style="text-align: center; font-family: sans-serif;">
        <h1>Історичні малюнки Романова</h1>
        <p>Палац графів Ільїнських:</p>

        <img src="/static/images/palace.jpg" width="1200" style="border: 3px solid #333; border-radius: 10px;">

        <p><i>Це фото завантажено з твого комп'ютера (Bodya Production)</i></p>
    </div>
    """
    return HttpResponse(html_code)