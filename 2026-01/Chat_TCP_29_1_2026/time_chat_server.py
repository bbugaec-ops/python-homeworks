import socket              # TCP
import threading                 # потоки - паралельна робота
import sys                #  акуратний текст

HOST = "127.0.0.1"
PORT = 5000

def reader(sock):
    try:
        while True:
            data = sock.recv(4096)            # максимум байтів за раз 4096
            if not data:
                print("\n Сервер закрив з'єднання.")
                break
            sys.stdout.write(data.decode("utf-8", errors="replace"))
            sys.stdout.flush()
    except OSError:
        pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    threading.Thread(target=reader, args=(sock,), daemon=True).start()

    try:
        while True:
            text = input()
            sock.sendall((text + "\n").encode("utf-8"))
            if text.strip().lower() == "/exit":
                break
    finally:
        sock.close()

if __name__ == "__main__":
    main()
