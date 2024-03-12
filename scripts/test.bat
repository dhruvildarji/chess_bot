set modelDir=chess_01
set input_text=%2

set current_dir=D:\git\scripture_gpt\

cd %current_dir%\TensorRT-LLM\examples

python %current_dir%\TensorRT-LLM\examples\run.py   --input_text "Input 3: W1.e4 - B1Nf6 - W2.Nf3" --engine_dir=%current_dir%\models\%modelDir%\engine_output --max_output_len 128

set tmp_dir=%CD%
