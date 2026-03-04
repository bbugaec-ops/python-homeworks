import threading
import time
from queue import Queue


class FileWorker(threading.Thread):
    def __init__(self,name,queue):
        super().__init__()
        self.name = name
        self.queue = queue


    def run(self):
        time.sleep(0.1)
        result = len(self.name)
        self.queue.put((self.name, result))


result = {}
threads = []

files = ['qwerty','asd','game','python']
queue = Queue()

for f in files:
    t = FileWorker(f, queue)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

while not queue.empty():
    key, vale = queue.get()
    result[key] = vale


print(result)

counter = 0

def increments():
    global counter
    for i in range(10000):
        counter += 1

threads = [threading.Thread(target=increments),
           threading.Thread(target=increments),
           threading.Thread(target=increments)]

for t in threads:
    t.start()

for t in threads:
    t.join()



print(counter)
