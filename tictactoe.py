import pygame
import sys
from const import *
from ai import AI

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUNDCOLOR)


class Board:
    def __init__(self):
        self.squares = [[-100 for j in range(0, COLS)] for i in range(0, ROWS)]
        #self.emptySquares = self.squares
        self.markedSquares = 0

    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        self.markedSquares+=1

    def emptySquare(self, row, col):
        return self.squares[row][col]==-100
    
    def isFull(self):
        return self.markedSquares == ROWS*COLS
    
    def isEmpty(self):
        return self.markedSquares == 0
    
    def getEmptySquares(self):
        emptySquares = []
        for row in range(0, ROWS):
            for col in range(0, COLS):
                if self.emptySquare(row, col):
                    emptySquares.append((row, col))
        return emptySquares
    
    def finalState(self, show=False):
        #returns 0 if there is no win
        #returns -1 if player 1 wins
        #returns 1 if player 0 wins
        #this will be used by our ai for the minimax algorithm
        i=0
        for row in self.squares:
            s=sum(row)
            if s==0: #player 0 wins
                if show:
                    iPos = (SQUARESIZE//2, i*SQUARESIZE + SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, i*SQUARESIZE + SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return 1
            if s==COLS:
                if show:
                    iPos = (SQUARESIZE//2, i*SQUARESIZE + SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, i*SQUARESIZE + SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return -1
            i+=1
        
        i=0
        for col in range(0, COLS): #vertical wins
            tot = 0
            for row in range(0, ROWS):
                tot+=self.squares[row][col]
            if tot==0:
                if show:
                    iPos = (i*SQUARESIZE + SQUARESIZE//2, SQUARESIZE//2)
                    fPos = (i*SQUARESIZE + SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return 1
            if tot==ROWS:
                if show:
                    iPos = (i*SQUARESIZE + SQUARESIZE//2, SQUARESIZE//2)
                    fPos = (i*SQUARESIZE + SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return -1
            i+=1
           
        if COLS==ROWS: #diag wins only possible on square board
            tot=0
            for i in range(0, COLS):
                tot+=self.squares[i][i]
            if tot==0:
                if show:
                    iPos = (SQUARESIZE//2, SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return 1
            if tot==COLS:
                if show:
                    iPos = (SQUARESIZE//2, SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return -1
            
            tot=0
            for i in range(0, COLS):
                tot+=self.squares[ROWS-1-i][i]
            if tot==0:
                if show:
                    iPos = (SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return 1
            if tot==COLS:
                if show:
                    iPos = (SQUARESIZE//2, HEIGHT - SQUARESIZE//2)
                    fPos = (WIDTH - SQUARESIZE//2, SQUARESIZE//2)
                    pygame.draw.line(screen, WINCOLOUR, iPos, fPos, LINEWIDTH)
                return -1
            
        return 0

class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.gameMode = 'ai'
        self.running = True
        self.curPlayer=0
        self.drawLines()

    def drawLines(self):
        screen.fill(BACKGROUNDCOLOR)
        #vertical lines
        pygame.draw.line(screen, LINECOLOUR, (SQUARESIZE, 0), (SQUARESIZE, HEIGHT), LINEWIDTH)
        pygame.draw.line(screen, LINECOLOUR, (WIDTH-SQUARESIZE, 0), (WIDTH-SQUARESIZE, HEIGHT), LINEWIDTH)

        #horizontal lines
        pygame.draw.line(screen, LINECOLOUR, (0, SQUARESIZE), (WIDTH, SQUARESIZE), LINEWIDTH)
        pygame.draw.line(screen, LINECOLOUR, (0, HEIGHT-SQUARESIZE), (WIDTH, HEIGHT-SQUARESIZE), LINEWIDTH)

    def changePlayer(self):
        self.curPlayer = (self.curPlayer + 1)%2

    def drawShape(self, row, col):
        if self.curPlayer == 0:
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

    def changeGameMode(self):
        if self.gameMode=='player':
            self.gameMode='ai'
        else:
            self.gameMode='player'

    def reset(self):
        self.__init__()

    def isOver(self):
        return self.board.finalState(show=True)!=0 or self.board.isFull()  #call finalState first to draw line if last move fills board

def main():
    
    game = Game()
    board = game.board
    
    while True:

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // SQUARESIZE
                col = event.pos[0] // SQUARESIZE
                if board.emptySquare(row, col) and game.running:
                    board.markSquare(row, col, game.curPlayer)
                    game.drawShape(row, col)
                    game.changePlayer()
                    if game.isOver():
                        game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.changeGameMode()
                if event.key == pygame.K_0:
                    game.ai.level = 0
                if event.key == pygame.K_1:
                    game.ai.level = 1
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board

            if game.gameMode=='ai' and game.curPlayer==game.ai.player and board.markedSquares<ROWS*COLS and game.running:
                pygame.display.update()
                row, col = game.ai.eval(board)
                board.markSquare(row, col, game.curPlayer)
                game.drawShape(row, col)
                game.changePlayer()
                if game.isOver():
                        game.running = False

            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main()