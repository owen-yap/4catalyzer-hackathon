from typing import Union

from fastapi import FastAPI

import requests
import torch
from PIL import Image
from io import BytesIO
import os
from diffusers import StableDiffusionInstructPix2PixPipeline
import io


app = FastAPI()

# model stuff
device = "cuda"
# model_id_or_path = "runwayml/stable-diffusion-v1-5"
model_id_or_path = "../opt/run-overnight"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float16, low_cpu_mem_usage=False, ignore_mismatched_sizes=True)
pipe = pipe.to(device)

prompts = {
    "h2h": "This is an image of a normal brain MRI scan from axial view. It should be grey scale and clearly show brain structure. Do not modify the input image.",
    "h2uh": "Given an input image of a normal brain MRI scan from axial view, modify the image by inserting a brain lesion within the MRI image. This brain lesion is caused by an ischaemic stroke. The lesion should appear relatively lighter compared to its surroundings brain tissue in the image.",
    "uh2uhm": "Given an input image of an unhealthy brain MRI scan from axial view that contains brain lesions, modify the image to colour the lesions light red.",
    "h2uhm": "Given an input image of a normal brain MRI scan from axial view, modify the image by inserting a brain lesion within the MRI image, and colour the lesions light red. This brain lesion is caused by an ischaemic stroke.",
    "uhm2uhm": "This is an image of an unhealthy brain MRI scan from axial view that contains brain lesions. The lesions are coloured light red."
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/generate")
async def generate(num_inference_steps: int, image_guidance_scale: float, guidance_scale: float, image_url: str,):
    generated_urls = infer(image_url, num_inference_steps, image_guidance_scale, guidance_scale)
    return {"generated_urls": generated_urls}



def infer(image_url, num_inference_steps, image_guidance_scale, guidance_scale):
    response = requests.get(image_url)
    response.raise_for_status()
    init_image = Image.open(io.BytesIO(response.content)).convert("RGB")

    prompt = "modify the image by inserting brain lesions within the MRI image, and highlight the brain lesions in bright red color."
    print("generating")
    generator = torch.Generator("cuda").manual_seed(40)
        
    images = pipe(prompt, image=init_image,
                num_inference_steps = num_inference_steps, #int
                image_guidance_scale = image_guidance_scale, #float
                guidance_scale = guidance_scale, #float
                num_images_per_prompt=1,
                generator=generator).images

    print("done")
    uploaded_urls = []
    for idx, image in enumerate(images):
        # Convert the Pillow image to bytes (in-memory representation)
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='JPEG')
        img_bytes.seek(0)

        cdn_upload_url = "https://api.upload.io/v2/accounts/12a1yU7/uploads/binary"
        headers = {
            "Authorization": "Bearer public_12a1yU77jroPKckv6W5q5GBXUpv4",
            "Content-Type": "image/jpeg"  # Change this to match the actual image MIME type
        }
        cdn_response = requests.post(cdn_upload_url, headers=headers, data=img_bytes)
        cdn_response.raise_for_status()  # Check for any errors in the CDN upload
        uploaded_url = cdn_response.json().get("fileUrl")  # Assuming the CDN API returns the uploaded URL in the response
        uploaded_urls.append(uploaded_url)

    return uploaded_urls
