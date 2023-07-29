import requests
import torch
from PIL import Image
from io import BytesIO
import os

from diffusers import StableDiffusionImg2ImgPipeline

device = "cuda"
model_id_or_path = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16)
pipe = pipe.to(device)

# Assuming the 'data' folder is in the same directory as your script
data_folder = "./data/dummy/"

# Replace 'sketch-mountains-input.jpg' with the actual filename if needed
image_filename = '1.jpg'

# Build the full path to the image file
image_path = os.path.join(data_folder, image_filename)

# Open and resize the image
init_image = Image.open(image_path).convert("RGB")
# init_image = init_image.resize((768, 512))

prompt = "insert a brain lesion into the image, retaining most of the image"

images = pipe(prompt=prompt, image=init_image, strength=0.01, guidance_scale=7.5).images

for idx, image in enumerate(images):
    output_path = f"./opt/{os.path.splitext(os.path.basename(image_filename))[0]}-generated-{idx}.jpg"
    image.save(output_path)