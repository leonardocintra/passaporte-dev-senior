from os import system
from app import App

def show(board):
    system('clear')
    print(board)

def cli():
    app = App()