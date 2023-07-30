import requests
import torch
from PIL import Image
from io import BytesIO
import os

from diffusers import StableDiffusionImg2ImgPipeline

device = "cuda"
# model_id_or_path = "runwayml/stable-diffusion-v1-5"
model_id_or_path = "./opt/run-overnight"
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16, low_cpu_mem_usage=False, ignore_mismatched_sizes=True)
pipe = pipe.to(device)

prompts = {
    "h2h": "This is an image of a normal brain MRI scan from axial view. It should be grey scale and clearly show brain structure. Do not modify the input image.",
    "h2uh": "Given an input image of a normal brain MRI scan from axial view, modify the image by inserting a brain lesion within the MRI image. This brain lesion is caused by an ischaemic stroke. The lesion should appear relatively lighter compared to its surroundings brain tissue in the image.",
    "uh2uhm": "Given an input image of an unhealthy brain MRI scan from axial view that contains brain lesions, modify the image to colour the lesions light red.",
    "h2uhm": "Given an input image of a normal brain MRI scan from axial view, modify the image by inserting a brain lesion within the MRI image, and colour the lesions light red. This brain lesion is caused by an ischaemic stroke.",
    "uhm2uhm": "This is an image of an unhealthy brain MRI scan from axial view that contains brain lesions. The lesions are coloured light red."
}

# # Assuming the 'data' folder is in the same directory as your script
data_folder = "./data/train/"

# # Replace 'sketch-mountains-input.jpg' with the actual filename if needed
image_filename = 'healthy_images/sub-ON21834/caseON21834_dwi_slice_40.png'

# Replace 'sketch-mountains-input.jpg' with the actual filename if needed
# image_filename = 'lesion_images/sub-strokecase0002/case0002_dwi_slice_30.png'

# Build the full path to the image file
image_path = os.path.join(data_folder, image_filename)

# Open and resize the image
init_image = Image.open(image_path).convert("RGB")
# init_image = init_image.resize((768, 512))

prompt = prompts["h2uhm"]

images = pipe(prompt=prompt, image=init_image, strength=0.01, guidance_scale=7.5).images

for idx, image in enumerate(images):
    healthy_output_file = os.path.basename(image_filename)
    output_path = f"./viz/{healthy_output_file}"
    init_image.save(output_path)

    pred_output_path = f"./viz/{os.path.splitext(os.path.basename(image_filename))[0]}-generated-{idx}.jpg"
    image.save(pred_output_path)


# API CALLS
