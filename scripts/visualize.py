import chess
import chess.svg
from IPython.display import display, clear_output
import time

def play_game(moves):
    board = chess.Board()
    for move in moves:
        clear_output(wait=True)
        display(chess.svg.board(board=board, size=400))
        time.sleep(0.5)  # Adjust the time as per your convenience
        try:
            board.push_san(move)
        except Exception as e:
            print(f"Invalid move: {move}")
            print(e)
            break

# Game moves
game_moves = ['e4', 'Nf6', 'Nf3', 'd5', 'Bb5', 'a6', 'Ba4', 'Nf6', 'O-O', 'Be7', 'Re1', 'b5', 'Bb3', 'd6', 'c3', 'O-O', 'h3', 'Na5', 'Bc2', 'c5', 'd4', 'Qc7', 'Nbd2', 'Bd7', 'Nf1', 'cxd4', 'cxd4', 'Rac8', 'Ne3', 'Nc6', 'd5', 'Nb4', 'Bb1', 'a5', 'a3', 'Na6', 'b4', 'Ra8', 'Bd2', 'Rfc8', 'Bd3', 'Qb7', 'g4', 'g6', 'Nf1', 'axb4', 'axb4', 'Bd8', 'Ng3', 'Nc7', 'Qe2', 'Rxa1', 'Rxa1', 'Ra8', 'Qe1', 'Nfe8', 'Qc1', 'Ng7', 'Rxa8', 'Qxa8', 'Bh6', 'Nce8', 'Qb2', 'Qa4', 'Kg2', 'Bb6', 'Bc2', 'Qa7', 'Bd3', 'Qa4', 'Ne2', 'Nc7', 'Nxe5', 'dxe5', 'Qxe5', 'Nce8', 'Bxg7', 'Qd1', 'Bh6', 'Qxd3', 'Qe7', 'Ng7', 'Ng3', 'Qc2', 'Qf6', 'Nf5', 'Qxb6', 'Nh4+', 'Kh2', 'Nf3+', 'Kg2', 'Nh4+', 'Kh2', 'Nf3+', 'Kg2', 'Nh4+', 'Kh2']

# Play the game
play_game(game_moves)
