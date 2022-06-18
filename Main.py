from Game import Game
from Player import Player
from Dealer import Dealer

newPlayer = Player()
newDealer = Dealer()
newGame = Game(newPlayer, newDealer)
newGame.startGame()
