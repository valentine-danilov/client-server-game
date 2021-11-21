import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "63.35.219.98"
        self.port = 5555
        self.address = (self.server, self.port)
        self.player = self.connect()

    def getPlayer(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.address)
            state = pickle.loads(self.client.recv(2048))
            print("Connected with id {}".format(state.getId()))
            return state
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            gameState = pickle.loads(self.client.recv(2048*64))
            return gameState
        except socket.error as e:
            print(e)

