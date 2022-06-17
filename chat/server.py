import socket, threading

HOST = "127.0.0.1"
PORT = 6060
BUFFER_SIZE = 1024

class Server:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.configure_server()
        self.clients = self.nicknames = []

    def configure_server(self):
        self.server.bind((HOST, PORT))
        self.server.listen()

    def broadcast_client_message(self, message: str):
        for client in self.clients:
            client.send(message)

    def handle(self, client):
        while 1:
            try:
                message = client.recv(BUFFER_SIZE)
                self.broadcast_client_message(message)
            except:
                break

    def receive(self):
        while 1:
            client, address = self.server.accept()
            client.send("NICK".encode("ascii"))
            nickname = client.recv(BUFFER_SIZE)

            client_handler = threading.Thread(target=self.handle, args=(client,))
            client_handler.start()

if __name__ == "__main__":
    server = Server()
    server.receive()
