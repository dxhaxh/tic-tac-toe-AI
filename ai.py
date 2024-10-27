import random
import copy

class AI:
    def __init__(self, level=1, player=1):
        self.level = level
        self.player = player

    def eval(self, mainBoard):
        if self.level==0:
            #make a random choice
            return random.choice(mainBoard.getEmptySquares())
        #otherwise we use minimax to find choice
        eval, move = self.minimax(mainBoard, False)
        print(f'ai has chosen to mark square in pos {move} with an eval of {eval}')
        return move

    def minimax(self, board, maximizing):
        #minimax will return a tuple (evaluation, bestMove)
        #check terminal cases(which are our base cases)
        terminalEval = board.finalState()
        if terminalEval!=0 or board.isFull():
            return (terminalEval, None)

        if maximizing:
            maxEval = -100
            bestMove = None
            emptySquares = board.getEmptySquares()
            for row, col in emptySquares:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(row, col, (self.player + 1)%2)
                eval= self.minimax(tempBoard, False)[0]
                if eval > maxEval:
                    maxEval = eval
                    bestMove = (row, col)
            return (maxEval, bestMove)
        else:
            minEval = 100
            bestMove = None
            emptySquares = board.getEmptySquares()
            for row, col in emptySquares:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(row, col, self.player)
                eval= self.minimax(tempBoard, True)[0]
                if eval < minEval:
                    minEval = eval
                    bestMove = (row, col)
            return (minEval, bestMove)
                
        