# [Lesionize](https://lesionize.io) - Synthetic Stroke Lesion Generation for MRI Data

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Nutlope/strokeGPT&env=REPLICATE_API_KEY&project-name=stroke-GPT&repo-name=strokeGPT)

[![Lesionize](./assets/screenshot.png)](https://strokeGPT.io)

## How it works

Lesionize utilizes a latent diffusion model to generate synthetic stroke lesions that mimic those found in ischemic stroke patient MRI scans. This functionality is specifically designed to assist stroke detection and segmentation projects by providing augmented data for training and improving stroke detection models.

The application allows users to upload an image of an MRI scan. The uploaded images are then processed using the latent diffusion model through a Next.js API route, and the generated image with synthetic stroke lesions is returned to the user. The latent diffusion model is hosted on [Replicate](https://replicate.com), and [Upload](https://upload.io) is used for image storage.

### Datasets procured

For the purposes of this application, MRI DWI Images of the axial plane were gathered from two main datasets
1) [ISLES22 Grand Challenge Dataset](https://isles22.grand-challenge.org/dataset/) -- This dataset contains MRI DWI images of the brains of stroke patients. The lesions within the brain have been annotated on the MRI images.
2) [OpenNeuro NIMH Healthy Research Volunteer Dataset](https://openneuro.org/datasets/ds004215/versions/1.0.0) -- This dataset contains MRI DWI images of the brains of healthy patients.

The data was processed and cleaned to allow Hugging Face to curate our custom dataset using ImageFolder.

### Training Approach

We utilized the [InstructPix2Pix](https://huggingface.co/docs/diffusers/training/instructpix2pix) training approach and pipeline for our use case.

This pipeline takes in an input image and prompt, and outputs the input image edited according to the prompt's specifications.

Thus, each training data object consisted of the following data:
- input image: the MRI DWI scan of the brain of a healthy patient
- prompt: a prompt describing the type of lesions to insert into the MRI scan of the healthy brain
- edited image: the MRI DWI scan of the brain of a patient with stroke lesions

Thus, we allow the model to pick up "instructions" from the prompt, to amend the input image.

The training script can be found within the diffusers module, or by clicking [here](https://github.com/huggingface/diffusers/blob/aae27262f408957ff53c64b3a18581959e8fd8e0/src/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion_instruct_pix2pix.py#L139)

## Running Locally

### Installing the dependencies.

```bash
npm install
```

### Running the application.

Then, run the application in the command line, and it will be available at `http://localhost:3000`.

```bash
npm run dev
```

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Nutlope/strokeGPT&env=REPLICATE_API_KEY&project-name=stroke-GPT&repo-name=strokeGPT)