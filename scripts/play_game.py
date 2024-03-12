import chess
import chess.svg
from IPython.display import display, clear_output
import time
from load_model import get_llm_out, run_llm, extract_result

class chess_game:
    def __init__(self,model="chess_big_data_simple"):
        self.model = model
        self.board = chess.Board()
        self.user_in = None
        self.LLM_in = None
        self.update_input = ""
        self.turn = True # False means its LLM True means user 
        self.move_number = 0    # Number of moves have happened so far

    def update_display(self):
        display(chess.svg.board(board=self.board, size=400))

    def get_user_input(self):
        # Get user input for the next move
        self.user_in = input("Enter your move (or type 'exit' to end): ").strip()        
        self.create_input_for_llm()

    def create_input_for_llm(self):

        self.update_input = f"{self.update_input}{self.move_number}. {self.user_in}"
    
    def update_input_from_llm(self):

         self.update_input = f"{self.update_input} {self.LLM_in} "


    def update_board(self, move_san):
        try:
            # Attempt to parse the SAN (Standard Algebraic Notation) move
            move = self.board.parse_san(move_san)
            
            # If successful and the move is legal, apply it to the board
            if move in self.board.legal_moves:
                self.board.push(move)
                self.turn = not self.turn
                print(f"Move '{move_san}' made successfully.")
                return True
            else:
                # This branch is technically redundant because parse_san() will fail for illegal moves,
                # but it's included for clarity and completeness.
                print(f"Move '{move_san}' is illegal.")
                return False
        except ValueError as e:
            # The move was not legal or not in the right format
            print(f"Invalid move: {move_san}. Error: {str(e)}")
            return False

        
    def fixing_result_llm(self, output_text):
        trial = 2
        succeed = True
        while not self.update_board(self.LLM_in):
            trial+=1
            if trial == 10:
                succeed = False
                break
            self.LLM_in = extract_result(output_text,trial)
        if succeed:
            print(f"it got succedded in {trial} trials")
        else:
            print("LLM gave up...")
        return succeed
            
    def play_game(self):
        while True:
            # self.update_display()
            if self.turn:
                print("User's Turn")
                self.move_number += 1
                self.get_user_input()
                if self.user_in == "exit":
                    print("Resigning....")
                    break
                if not self.update_board(self.user_in):
                    continue
            else:
                print("LLM's Turn")
                output_text = run_llm(self.update_input, self.model)
                self.LLM_in = extract_result(output_text)
                if not self.update_board(self.LLM_in):
                    ret = self.fixing_result_llm(output_text)
                    if not ret:
                        break
                self.update_input_from_llm()
                         
obj = chess_game()
obj.play_game() 
