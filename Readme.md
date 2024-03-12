# Chess Bot Repository

Chess Bot created based on Large Language Model GPT2

It is infered and acclerated by TensorRT-LLM library

# Build the Model

You can create the model using following code

```

python scripts/finetune.py --epochs=20 --output_dir=./models/output_chess --train_file_path=./data/chess/big_chess_text2.txt
```

Once the directory is made, run the

```
cd web-app
python app.py
```

## Clone the repository

```
git clone https://github.com/dhruvildarji/scripture_gpt.git
cd scripture_gpt
git submodule update
```

## Installing TensorRT-LLM

This is the first and most important step.
We didnt do reinvent anything here. Nvidia's TensorRT-LLM library has very neat and clean documentation to install this lib.

Please use following link to build this library in your windows system.

https://github.com/NVIDIA/TensorRT-LLM/tree/v0.7.1

Once its installed follow next steps.

## Supported OS

Windows system only

## Model Selection

For this project, we've chosen to work with the GPT-2 model, which has 124M parameters. This smaller model size allows for quicker loading and finetuning times, making it an efficient choice for our purposes.

### Why GPT-2?

- **Efficiency:** The GPT-2 model, due to its smaller size, can be finetuned rapidly with various parameters.
- **TensorRT-LLM Library:** Our goal is to utilize the TensorRT-LLM library to accelerate these finetuned models, optimizing for performance.
- **Limited Resources:** We had only RTX 4070 GPU with 8 GB of VRAM only. Not lot of models can be loaded with 8 Gig of VRAM
