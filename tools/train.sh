#!/bin/bash

# Set the model name variable
MODEL_NAME="runwayml/stable-diffusion-v1-5"

# Set other variables (if needed)
TRAIN_DATA_PATH="/home/ubuntu/4catalyzer-hackathon/data/dummy/train"
OUTPUT_DIR="/home/ubuntu/4catalyzer-hackathon/opt/"

# The 'accelerate launch' command with the variables    
accelerate launch --mixed_precision="fp16" train_instruct_pix2pix.py \
    --pretrained_model_name_or_path=$MODEL_NAME \
    --dataset_name=sayakpaul/instructpix2pix-1000-samples \
    --resolution=256 --random_flip \
    --train_batch_size=1 --gradient_accumulation_steps=4 \
    --max_train_steps=15000 \
    --checkpointing_steps=5000 --checkpoints_total_limit=1 \
    --learning_rate=5e-05 --max_grad_norm=1 --lr_warmup_steps=0 \
    --conditioning_dropout_prob=0.05 \
    --mixed_precision=fp16 \
    --seed=42 \
    # --original_image_column="image" \
    # --edit_prompt_column="prompt" \
    # --edited_image_column="edited_image" \

    # --push_to_hub 
    # --gradient_checkpointing \
    # --enable_xformers_memory_efficient_attention \

    
    # --train_data_dir=$TRAIN_DATA_PATH \
    # --output_dir=$OUTPUT_DIR \
