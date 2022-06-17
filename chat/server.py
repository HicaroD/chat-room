import socket, threading

HOST = "127.0.0.1"
PORT = 6060
BUFFER_SIZE = 1024

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()

    def run(self):
        connection, address = self.server.accept()
        client = connection.recv(BUFFER_SIZE).decode()
        print(f"{client} is connected!")

        while 1:
            message = connection.recv(BUFFER_SIZE).decode()
            if message:
                print(f"[{client}] {message}")


if __name__ == "__main__":
    server = Server()
    server.run()
