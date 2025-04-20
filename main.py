from utils.describe_image import describe
from utils.image_gen import generate_image
from utils.video_gen import generate_video
import pandas as pd
import json

prompt = pd.read_csv("prompts_for_image.csv")
for i in range(len(prompt)):
    print(prompt.iloc[i, 0])
    generate_image(prompt.iloc[i, 0], f"generated_images/image_{i}")


captions = {}
for i in range(70):
    image_path = f"generated_images/image_{i}.png"
    caption = describe(image_path)
    captions[i] = caption

with open("captions.json", "w") as f:
    json.dump(captions, f, indent=4)



captions = pd.read_json("captions.json", typ='series').reset_index()
captions.columns = ['id', 'caption']
captions = captions.caption
prompts = pd.read_csv("prompts_for_image.csv")

all_prompts = []
for i in range(len(prompts)):
    combined = f" {prompts.iloc[i, 0]} description: {captions[i]}"
    all_prompts.append(combined)


for i in range(10, len(all_prompts)):
    print(all_prompts[i])
    generate_video(all_prompts[i], f"video_{i}.mp4")

print(all_prompts[10:19])