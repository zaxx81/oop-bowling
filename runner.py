# TEST CASES
from classes.player import Player
from classes.game import Game

players = [Player('Zack', 3), Player('Sabrina', 1)]

new_game = Game(players)
new_game.lets_bowl()