#!/bin/bash

# Set the model name variable
MODEL_NAME="runwayml/stable-diffusion-v1-5"

# Set other variables (if needed)
DATASET_ID="fusing/instructpix2pix-1000-samples"

# The 'accelerate launch' command with the variables
accelerate launch --mixed_precision="fp16" train_instruct_pix2pix.py \
    --pretrained_model_name_or_path="$MODEL_NAME" \
    --dataset_name="$DATASET_ID" \
    --enable_xformers_memory_efficient_attention \
    --resolution=256 --random_flip \
    --train_batch_size=4 --gradient_accumulation_steps=4 --gradient_checkpointing \
    --max_train_steps=15000 \
    --checkpointing_steps=5000 --checkpoints_total_limit=1 \
    --learning_rate=5e-05 --max_grad_norm=1 --lr_warmup_steps=0 \
    --conditioning_dropout_prob=0.05 \
    --mixed_precision=fp16 \
    --seed=42 \
    --push_to_hub