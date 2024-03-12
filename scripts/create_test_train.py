import torch # we use PyTorch: https://pytorch.org
import argparse

def dataset(file_path):
    """
    Function to load and split the data into training and validation sets.

    Args:
        file_path (str): Path to the file containing the dataset.

    Returns:
        tuple: A tuple containing train_data and val_data.
    """
    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()
    # Split the data into train and validation sets
    n = int(0.9 * len(text))  # First 90% will be train, rest val
    train_data = text[:n]
    val_data = text[n:]

    return "".join(train_data), "".join(val_data)



# Function to save data to a file
def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)



def custom_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # Split the data into train and validation sets
    n = int(0.05 * len(text))  # First 90% will be train, rest val
    list1 = []
    n = 20
    text = text.splitlines()
    c = len(text)
    print(c)
    f = int(c / n)
    for i in range(n):
        train_data = text[i*f:(i+1)*f]
        list1.append(train_data)
    for e,l in enumerate(list1):
        file_path=f"D:/git/scripture_gpt/data/chess/{e}_chess_game_black_moves_only.txt"
        save_data(file_path, "\n".join(l))










def restructure_game_for_alternating_perspective(game_data):
    """Restructures a single game's data for alternating perspective."""
    parts = game_data.split("###")
    moves_part = parts[1].strip() if len(parts) > 1 else ""
    moves = moves_part.split(" ")
    
    structured_moves = []
    for move in moves:
        if move.startswith("W"):
            structured_moves.append(f"White: {move[2:]}")
        elif move.startswith("B"):
            structured_moves.append(f"Black: {move[2:]}")
    return structured_moves

def save_games_to_file(games_data, file_path):
    """Saves the restructured games data to a text file."""
    c = 0
    with open(file_path, "w") as file:
        for game_data in games_data:
            c = c + 1
            if c == 5:
                break
            structured_game = restructure_game_for_alternating_perspective(game_data)
            for move in structured_game:
                file.write(move + "\n")
            file.write("\n")  # Separate games with a newline

def format_data_for_ml(games_data):
    """Formats chess game data into a specific Input/Output format for ML model training."""
    formatted_data = []
    c = 0
    for game_data in games_data:
        parts = game_data.split("###")
        moves_part = parts[1].strip() if len(parts) > 1 else ""
        moves = moves_part.split(" ")[1:]  # Skip the game metadata, start with actual moves
        
        for i in range(len(moves)):
            input_sequence = " - ".join(moves[:i])
            output_move = moves[i][2:] if i < len(moves) else ""
            formatted_data.append((input_sequence, output_move))
        formatted_data.append(("new_game","new_game"))

    return formatted_data

def save_formatted_data_to_file(formatted_data, file_path):
    """Saves the formatted Input/Output data to a text file."""
    with open(file_path, "w") as file:
        idx = 0
        for (input_sequence, output_move) in formatted_data:
            idx+=1
            if input_sequence == "new_game":
                idx = 0
                file.write(f"Starting new game \n\n")
            if input_sequence and input_sequence != "new_game":  # To avoid writing an empty input for the first move
                file.write(f"Input {idx}: {input_sequence}\n")
            if output_move and output_move != "new_game":
                file.write(f"Output {idx}: {output_move}\n")


def format_in_other_way(formatted_data_):
    """Formats chess game data into a specific Input/Output format for ML model training."""
    formatted_data = []
    c = 0
    for game_data in formatted_data_[5:]:
        parts = game_data.split("###")
        moves_part = parts[1].strip() if len(parts) > 1 else ""
        moves = moves_part.split(" ")  # Skip the game metadata, start with actual moves
        
        for i in range(len(moves)):
            if "B" in moves[i].split(".")[0]:
                input_sequence = " - ".join(moves[:i])
                output_move = moves[i][1:] if i < len(moves) else ""
                formatted_data.append((input_sequence, output_move))
        formatted_data.append(("new_game","new_game"))
    return formatted_data

# file_path="D:/git/scripture_gpt/data/chess/0.txt"
output_path = "D:/git/scripture_gpt/data/chess/0_formatted_only_for_black_moves.txt"
# with open(file_path, 'r', encoding='utf-8') as file:
#     text = file.read()
# text = text.splitlines()

# formatted_data_for_ml = format_in_other_way(text)
# save_formatted_data_to_file(formatted_data_for_ml, output_path)

# custom_data(output_path)
# file_path="D:/git/scripture_gpt/data/chess/0_chess_black.txt"
# train, test = dataset(file_path)

# save_data(f"D:/git/scripture_gpt/data/chess/1_chess_game_structured_train.txt", train)
# save_data(f"D:/git/scripture_gpt/data/chess/1_chess_game_structured_test.txt", test)


# with open(file_path, 'r', encoding='utf-8') as file:
#     text = file.read()
# text = text.splitlines()
# file_path = f"D:/git/scripture_gpt/data/chess/chess_games_structured.txt"


# # Process the games data and format it for ML
# formatted_data_for_ml = format_data_for_ml(text)


# # Save the formatted data to the specified file
# save_formatted_data_to_file(formatted_data_for_ml, file_path)






# if __name__ == "__main__":
    # custom_data(f"D:/chess_dataset/archive/all_with_filtered_anotations_since1998.txt")
    # parser = argparse.ArgumentParser(description="Main script")
    # parser.add_argument("--input_file_path", type=str, help="Path to the input file for processing", required=True)
    # parser.add_argument("--output_train_file_path", type=str, help="Path to save the processed output", required=True)
    # parser.add_argument("--output_test_file_path", type=str, help="Path to save the processed output", required=True)
    # args = parser.parse_args()

    # train, test = dataset(args.input_file_path)
    
    # save_data(args.output_train_file_path, train)
    # save_data(args.output_test_file_path, test)
    # n = 15
    # input_file_path = f"D:/git/scripture_gpt/data/chess"
    # for i in range(n):
    #     train, test = dataset(f"{input_file_path}/{i}.txt")
    
    #     save_data(f"{input_file_path}/{i}_train.txt", train)
    #     save_data(f"{input_file_path}/{i}_test.txt", test)

