import pandas as pd
import chess
    
file_path = f"D:/chess_dataset/archive/all_with_filtered_anotations/all_with_filtered_anotations_since1998.txt"

# f = open(file_path, "r")

df = pd.read_csv(f"{file_path}", skiprows=4)
print(df)
df = df.iloc[:].reset_index()
# smaller.head()
df[['id', 'date', 'result', 'welo' ,'belo', 'len', 'date_c', 'resu_c', 'welo_c', 'belo_c', 'edate_c', 'setup', 'fen', 'resu2_c', 'oyrange', 'bad_len']] = df['index'].str.split(' ', expand=True).iloc[:,:-1]
df['moves'] = df.iloc[:,1]
df = df.iloc[:,2:].set_index('id')

a = df.copy()

a['moves'] = a.moves.str.replace('[WB]\d+?\.', '')
a.sort_values('date', ascending=False)
currupt_games = 0
for idx in range(len(a)):
    game = a["moves"][idx]
    if type(game) == 'str':
        game = game.split(" ")
    else:
        continue
    board = chess.Board()
    for move in game:
        try:
            move = board.parse_san(move.split(".")[1])
            board.push_san(move)
        except:
            currupt_games = currupt_games + 1
            print(f"move is not legal with game number {idx}")
            print("next game")
            break


print(f"number of currupt games {currupt_games}")


