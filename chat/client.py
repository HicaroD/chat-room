import socket, threading

HOST = "127.0.0.1"
PORT = 6060
BUFFER_SIZE = 1024

class Client:
    def __init__(self, nickname: str):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_chat_room()

    def connect_to_chat_room(self):
        self.client.connect((HOST, PORT))

    def send_message(self):
        while 1:
            message = f"[{nickname}] {input()}"
            self.client.send(message.encode("ascii"))

    def receive(self):
        while 1:
            try:
                message = self.client.recv(BUFFER_SIZE).decode("ascii")
                if message == "NICK":
                    self.client.send(nickname.encode("ascii"))
                else:
                    print(message)
            except:
                self.client.close()
                break

    def run(self):
        received_thread = threading.Thread(target=self.receive)
        received_thread.start()

        write_thread = threading.Thread(target=self.send_message)
        write_thread.start()


if __name__ == "__main__":
    nickname = input("Coloque seu nickname: ")
    client = Client(nickname)
    client.run()
