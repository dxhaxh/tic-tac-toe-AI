import pygame
import sys
from const import *
import numpy as np

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUNDCOLOR)


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))

    def markSquare(self, row, col, player):
        self.squares[row][col] = player

    def emptySquare(self, row, col):
        return self.squares[row][col]==0
    
    


class Game:
    def __init__(self):
        self.board = Board()
        self.curPlayer=1
        self.drawLines()

    def drawLines(self):
        #vertical lines
        pygame.draw.line(screen, LINECOLOUR, (SQUARESIZE, 0), (SQUARESIZE, HEIGHT), LINEWIDTH)
        pygame.draw.line(screen, LINECOLOUR, (WIDTH-SQUARESIZE, 0), (WIDTH-SQUARESIZE, HEIGHT), LINEWIDTH)

        #horizontal lines
        pygame.draw.line(screen, LINECOLOUR, (0, SQUARESIZE), (WIDTH, SQUARESIZE), LINEWIDTH)
        pygame.draw.line(screen, LINECOLOUR, (0, HEIGHT-SQUARESIZE), (WIDTH, HEIGHT-SQUARESIZE), LINEWIDTH)

    def changePlayer(self):
        self.curPlayer = self.curPlayer%2 + 1

    def drawShape(self, row, col):
        if self.curPlayer == 1:
            #draw X, done with an acending and descending line
            #descending line
            startDesc = (col*SQUARESIZE + SQUARESIZE//4, row*SQUARESIZE + SQUARESIZE//4)
            endDesc = (col*SQUARESIZE + 3*SQUARESIZE//4, row*SQUARESIZE + 3*SQUARESIZE//4)
            pygame.draw.line(screen, XCOLOUR, startDesc, endDesc, XWIDTH)
            #ascending line
            startAsc = (col*SQUARESIZE + SQUARESIZE//4, row*SQUARESIZE + 3*SQUARESIZE//4)
            endAsc = (col*SQUARESIZE + 3*SQUARESIZE//4, row*SQUARESIZE + SQUARESIZE//4)
            pygame.draw.line(screen, XCOLOUR, startAsc, endAsc, XWIDTH)
        else:
            #draw O
            center = (col * SQUARESIZE + SQUARESIZE//2, row * SQUARESIZE + SQUARESIZE // 2)
            pygame.draw.circle(screen, CIRCLECOLOUR, center, CIRCLERADIUS, CIRCLEWIDTH)

def main():
    
    game = Game()
    board = game.board
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQUARESIZE
                col = event.pos[0] // SQUARESIZE
                if board.emptySquare(row, col):
                    board.markSquare(row, col, game.curPlayer)
                    game.drawShape(row, col)
                    game.changePlayer()
                print(board.squares)

            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main()