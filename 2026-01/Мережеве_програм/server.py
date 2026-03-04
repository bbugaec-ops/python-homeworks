import socket

#HOST = 'localhost'
HOST = '127.0.0.1'
PORT = 8080

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print("Sync server started, waiting for client.....")


    conn, addr = server.accept()
    print(f"Connected by {addr}")

    data = conn.recv(1024)
    if not data:
        print("No data received")
    else:
        message = data.decode()
        print("client says:",message)
        conn.sendall(b"Hello from server")

    conn.close()
    server.close()
    print("Server stopped")

if __name__ == '__main__':
    main()
