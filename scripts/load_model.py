import subprocess
import re
model = "chess_black_moves_0"
model = "chess_big_data_simple"
def run_llm(input_text, model):
    # Define the command and arguments
    script_path = r'D:\git\scripture_gpt\TensorRT-LLM\examples\run.py'
    args = [
        '--input_text',
        f"{input_text}",
        '--engine_dir',
         f"D:\git\scripture_gpt\models\{model}\engine_output",
        '--max_output_len',
        '128'
    ]
    
    # Run the command
    process = subprocess.run(['python', script_path] + args, capture_output=True, text=True)
    
    return process.stdout


def extract_result(out, itr_=1):
    # Regular expression to find the output following "Output 3:"
    # Regular expression to find the first output move

    regex_chess_01_model = r'Output \d+:\.(\S+)'
    regex_chess_black_moves_0_model = r'Output \d+:\s*\d+\.(\S+)'
    regex_chess_big_data =r"Output \[Text 0 Beam 0\]: \"(.*?)\""

    # Use regex to find the first move after the chess moves provided in the input
    first_move_full_text = re.search(regex_chess_big_data, out)
    if first_move_full_text:
        move_sequence = first_move_full_text.group(1)
        # From the move sequence, extract the first move
        first_output_move = move_sequence.split(" ")[itr_]
    
    return first_output_move



def get_llm_out(text):
    out = run_llm(text,model)
    move = extract_result(out)
    return move