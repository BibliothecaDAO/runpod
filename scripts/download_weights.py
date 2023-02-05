#!/usr/bin/env python

import os

import torch
from diffusers import StableDiffusionPipeline

os.makedirs("diffusers-cache", exist_ok=True)

pipe = StableDiffusionPipeline.from_pretrained(
    "rvorias/realms_adventurers_v1",
    cache_dir="diffusers-cache",
)
