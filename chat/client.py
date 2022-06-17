import socket, threading

HOST = "127.0.0.1"
PORT = 6060
BUFFER_SIZE = 1024

class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        self.nickname = "Unknown user"

    def run(self):
        nickname = input("Qual o seu nickname? ")

        if not self.nickname.isspace():
            self.nickname = nickname

        self.client.send(self.nickname.encode())
        # self.nickname = self.client.recv(BUFFER_SIZE).decode()
        print(f"{self.nickname} entrou no chat!")

        while 1:
            # received_message = self.client.recv(BUFFER_SIZE).decode()
            # print(f"[{self.nickname}] {received_message}")
            # self.client.send(message.encode())
            message = input(f"[{self.nickname}] ")
            print(f"CURRENT MESSAGE -> {message}")
            self.client.send(message.encode())


if __name__ == "__main__":
    client = Client()
    client.run()
