class GameState:
    def __init__(self):
        self.players = []

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def getPlayer(self, _id):
        for p in self.players:
            if p.getId() == _id:
                return p

    def updatePlayer(self, _player):
        player = self.getPlayer(_player.getId())
        player.x = _player.x
        player.y = _player.y
        player.rect = _player.rect

    def getPlayers(self, currentPlayerId):
        players = []
        for p in self.players:
            if p.getId() != currentPlayerId:
                players.append(p)
        return players

    def toString(self):
        _str = "["
        for p in self.players:
            _str += p.toString() + ",\n"
        return _str + "]"
