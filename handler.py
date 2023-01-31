import runpod
import os
import time
import torch
from diffusers import StableDiffusionPipeline



## load your model(s) into vram here
pipe = StableDiffusionPipeline.from_pretrained("rvorias/realms_adventurers_v1")
pipe = pipe.to("cuda")

def handler(event):
    prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]

    return image


runpod.serverless.start({
    "handler": handler
})