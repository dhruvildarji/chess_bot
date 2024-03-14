from flask import Flask, jsonify, request, render_template
from play_game import chess_game  # Adjust the import path as necessary
import chess
import chess.svg
from IPython.display import display, clear_output
from load_model import get_llm_out, run_llm, extract_result

app = Flask(__name__)

model = "xyz" 

# Initialize your chess game globally
game = chess_game() #parse this model in chess_game as input like chess_game(model)

@app.route('/')
def index():
    # Reset the game when loading the page
    global game
    game = chess_game()
    return render_template('index.html')

@app.route('/initial_board')
def initial_board():
    board_svg = game.get_board_svg()
    message = "It's your turn!"
    return jsonify({"board_svg": board_svg, "message":message})

@app.route('/make_move', methods=['POST'])
def make_move():
    data = request.json
    user_move = data.get('move', '')
    if game.turn:
        game.move_number = game.move_number + 1
        game.create_input_for_llm(user_move)
        print(f"game input {game.update_input}")
        # Process user move
        if game.update_board(user_move):
            board_svg = game.get_board_svg()
            game.turn = False  # Switch turn to LLM
            message = "It's the LLM's turn."
            return jsonify({"success": True, "board_svg": board_svg, "message": message, "isLLMmove": True})
        else:
            board_svg = game.get_board_svg()
            message = "Invalid move. Try again."
            return jsonify({"success": False, "board_svg": board_svg, "message": message})
    else:
        # Process LLM move
        output_text = run_llm(game.update_input, game.model)
        game.LLM_in = extract_result(output_text)
        if game.update_board(game.LLM_in):
            game.update_input_from_llm()
            game.turn = True  # Switch turn back to user
            board_svg = game.get_board_svg()
            message = "It's your turn!"
            return jsonify({"success": True, "board_svg": board_svg, "llm_move": game.LLM_in, "message": message})
        else:
            if not game.fixing_result_llm(output_text):
                return jsonify({"success": False, "error": "LLM failed to make a valid move"})
            game.update_input_from_llm()
            game.turn = True  # Switch turn back to user
            board_svg = game.get_board_svg()
            message = "It's your turn!"
            return jsonify({"success": True, "board_svg": board_svg, "llm_move": game.LLM_in, "message": message})

if __name__ == '__main__':
    app.run(debug=True)
