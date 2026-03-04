
def print_zir(n):
    if n == 0:
        return
    if n < 0:
        return
    if n > 0:
        print('*',end='  ')      #   end= - буде писати в рядку , не стовчик
        print_zir(n -1)

start = int(input("Введіть число  :"))
if start < 0:
    print("Введіть не від'ємне число ")      #   це написав на всякий случай , бо якщо - n < 0 - то сюди не дойде
else:
    print_zir(start)
print('-----')






