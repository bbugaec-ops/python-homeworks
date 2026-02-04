"""  РІВЕНЬ 2 (рекомендований)
Завдання
Додати команду:

/users → показати список підключених

Додати команду:

/exit → коректний вихід з чату

Сервер:

не розсилає команди як повідомлення

Підказка
перевіряти message.startswith("/")

окремо обробляти команди """


import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = {}
lock = threading.Lock()

def broadcast(message, exclude=None):
    data = (message + "\n").encode("utf-8")
    with lock:
        for sock in list(clients.keys()):
            if sock is exclude:
                continue
            try:
                sock.sendall(data)
            except OSError:
                sock.close()
                clients.pop(sock, None)

def handle_client(sock, addr):
    try:
        sock.sendall("Введи своє ім'я: ".encode("utf-8"))
        name = sock.recv(1024).decode("utf-8", errors="replace").strip()
        if not name:
            name = f"{addr[0]}:{addr[1]}"

        with lock:
            clients[sock] = name

        broadcast(f" {name} приєднався(лась) до чату", exclude=sock)
        sock.sendall(" Ти в чаті. Команди: /users, /exit\n".encode("utf-8"))

        while True:
            data = sock.recv(1024)
            if not data:
                break

            message = data.decode("utf-8", errors="replace").strip()
            if not message:
                continue


            if message.startswith("/"):

                if message == "/users":
                    with lock:
                        user_list = ", ".join(clients.values())
                    sock.sendall(
                        f" Підключені: {user_list}\n".encode("utf-8")
                    )


                elif message == "/exit":
                    sock.sendall(" До зустрічі!\n".encode("utf-8"))
                    break

                else:
                    sock.sendall(
                        "Невідома команда\n".encode("utf-8")
                    )
                continue


            broadcast(f"{name}: {message}", exclude=sock)

    except OSError:
        pass
    finally:
        with lock:
            left_name = clients.pop(sock, None)
        try:
            sock.close()
        except OSError:
            pass
        if left_name:
            broadcast(f" {left_name} вийшов(ла) з чату")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(20)

    print(f" Chat server запущено на {HOST}:{PORT}")

    while True:
        client_sock, addr = server.accept()
        threading.Thread(
            target=handle_client,
            args=(client_sock, addr),
            daemon=True
        ).start()

if __name__ == "__main__":
    main()
