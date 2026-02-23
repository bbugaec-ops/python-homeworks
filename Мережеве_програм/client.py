import socket

HOST = '127.0.0.1'
PORT = 8080

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Conected to the server")

    client.send(b"Hello from client ")

    responce = client.recv(1024)
    print(f"Server responce : {responce.decode()}")
    client.close()
    print("Client close")


if __name__ == '__main__':
    main()
