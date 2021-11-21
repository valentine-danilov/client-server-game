import socket
from _thread import *
from player import Player
from state import GameState
import pickle
import random
import uuid

server = "63.35.219.98"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print("Server running at port {}. Waiting for connections...".format(port))

state = GameState()

def client(_connection, _player):
    _connection.send(pickle.dumps(_player))
    reply = []
    while True:
        try:
            data = pickle.loads(_connection.recv(2048))
            state.updatePlayer(data)

            if not data:
                print("Client disconnected")
                break
            else:
                reply = state.getPlayers(_player.getId())
            _connection.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection with client")
    _connection.close()
    state.removePlayer(_player)


def randomPosition():
    return random.randint(0, 500)


def randomSize():
    return random.randint(50, 100)


def randomRgbValue():
    return random.randint(0, 255)


def randomColor():
    return randomRgbValue(), randomRgbValue(), randomRgbValue()


if __name__ == "__main__":
    while True:
        connection, ipAddress = s.accept()
        print("Connected to: {}".format(ipAddress))

        newPlayer = Player(
            uuid.uuid4(),
            randomPosition(), randomPosition(),
            randomSize(), randomSize(),
            randomColor()
        )

        print("New player connected: {}".format(newPlayer.toString()))
        start_new_thread(client, (connection, newPlayer))
        state.addPlayer(newPlayer)

        print("State:")
        for p in state.players:
            print(p.toString())
