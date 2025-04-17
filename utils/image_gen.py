import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")
# prompt = "A lone swordsman standing on the edge of a cliff at twilight, his silhouette illuminated by a glowing red moon in the background, tattered cloak flowing in the wind, sparks of lightning in the distance, ethereal cherry blossom petals floating around, cinematic lighting, ultra-detailed, atmospheric, 4k"

def generate_image(prompt,filename):
    image = pipe(prompt).images[0]
    image.save(f"{filename}.png")
