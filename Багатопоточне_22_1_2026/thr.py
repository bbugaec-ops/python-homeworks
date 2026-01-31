import threading
import time

def sum(a,b):
    print(a+b)
    time.sleep(3)

# print(threading.main_thread())
# threading.main_thread().setName("New name")   #  нове імя потоку
# print(threading.main_thread())

#print(threading.active_count()) #   показує скільки потоків зараз виконується , тут з верху

#print(threading.current_thread())    #    видає головний потік


t = threading.Thread(target=sum, args=(3,5))
t.start()

print(threading.enumerate())    #   Пише всі потоки які виконуються


t.join()

#print("Поток виповнився вдало !")

