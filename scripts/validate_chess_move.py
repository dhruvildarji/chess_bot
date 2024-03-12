import chess

board_game = "W1.d4 B1.d5 W2.c4 B2.e6 W3.Nc3 B3.Nf6 W4.cxd5 B4.exd5 W5.Bg5 B5.Be7 W6.e3 B6.Ne4 W7.Bxe7 B7.Nxc3 W8.Bxd8 B8.Nxd1 W9.Bxc7 B9.Nxb2 W10.Rb1 B10.Nc4 W11.Bxc4 B11.dxc4 W12.Ne2 B12.O-O W13.Nc3 B13.b6 W14.d5 B14.Na6 W15.Bd6 B15.Rd8 W16.Ba3 B16.Bb7 W17.e4 B17.f6 W18.Ke2 B18.Nc7 W19.Rhd1 B19.Ba6 W20.Ke3 B20.Kf7 W21.g4 B21.g5 W22.h4 B22.h6 W23.Rh1 B23.Re8 W24.f3 B24.Bb7 W25.hxg5 B25.fxg5 W26.d6 B26.Nd5+ W27.Nxd5 B27.Bxd5 W28.Rxh6 B28.c3 W29.d7 B29.Re6 W30.Rh7+ B30.Kg8 W31.Rbh1 B31.Bc6 W32.Rh8+ B32.Kf7 W33.Rxa8 B33.Bxd7 W34.Rh7+ "

def process_game(board_game):
    moves = board_game.split(" ")
    for move in moves:
        move.split(".")[1]




# Initialize a chess board
board = chess.Board()

# Define a move in UCI format (from square to square)
move_uci = "d2d3"

# Create a move object from UCI notation
move = chess.Move.from_uci(move_uci)

# Check if the move is legal
if move in board.legal_moves:
    # Make the move on the board
    print("Move made:", board.san(move))
    board.push(move)
    # Print the move in Standard Algebraic Notation (SAN)

else:
    print("Illegal move:", move_uci)
