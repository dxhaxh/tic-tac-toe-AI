# tic-tac-toe-AI   
This is a interactive tic tac toe game with an ai player that plays as the O's.
To play, run the tictactoe.py file. Once the game window opens, you can change the difficulty of the ai by pressing the '0' key on your keyboard, this makes the ai become a random ai. To change the ai back to it's original setting press '1' on your keyboard. If you want to play vs another human, press 'g' on your keyboard for player vs player mode. You can then press 'g' again to toggle back to ai. At any time during the game, you can press 'r' to restart the game. Note that pressing 'r' reverts back to the original settings of the game that means if you press 'r' you will play vs an ai on the original setting.   
# UNBEATABLE AI   
The ai in this game is unbeatable. The ai uses the minimax algorithm to find it's next best move. Because tic tac toe is not a huge game(like chess), the state space is pretty small. This allows us to scan through the whole state space space without the need for a heuristic function, since scanning through the whole state space is possible in a relatively short amount of time. Once we reach a terminal case(case where game over) in our search, we check the result. As mentioned, we can search thorugh the entire state space and can find the best move for any position. This is different when compared to a game like chess, since in chess the state space is much too large and we cannot reach every terminal case during our search(that would take too much time). So for games like chess we require a heuristic function, which estimates how good a certain position of the board is for each player without the game being over necessairly. The search in the state space for the next move would then go up until some limited depth(in order to not take too long) and would use the heuristic function to estimate which state 15 moves down the line, for example, would be best for the ai player. It would then chose the move which leads it to that best possible state. But because in tic tac toe the state space is small, we do not need this heuristic function and can scan through the whole state space without issue.