#!/bin/bash

# Set the model name variable
MODEL_NAME="runwayml/stable-diffusion-v1-5"

# Set other variables (if needed)
TRAIN_DATA_PATH="/home/ubuntu/4catalyzer-hackathon/data/train/"
OUTPUT_DIR="/home/ubuntu/4catalyzer-hackathon/opt/run-overnight/"

# The 'accelerate launch' command with the variables    
accelerate launch --mixed_precision="fp16" train_instruct_pix2pix.py \
    --pretrained_model_name_or_path=$MODEL_NAME \
    --train_data_dir=$TRAIN_DATA_PATH \
    --output_dir=$OUTPUT_DIR \
    --resolution=256 --random_flip \
    --train_batch_size=6 --gradient_accumulation_steps=4 \
    --max_train_steps=15000 \
    --checkpointing_steps=500 --checkpoints_total_limit=5 \
    --learning_rate=5e-05 --max_grad_norm=1 --lr_warmup_steps=0 \
    --conditioning_dropout_prob=0.05 \
    --mixed_precision=fp16 \
    --seed=42 \
    --original_image_column="input_image" \
    --edit_prompt_column="edit_prompt" \
    --edited_image_column="edited_image" \

    # --push_to_hub 
    # --gradient_checkpointing \
    # --enable_xformers_memory_efficient_attention \

    
