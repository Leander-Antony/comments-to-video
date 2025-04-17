from utils.describe_image import describe
from utils.image_gen import generate_image
from utils.video_gen import generate_video
import pandas as pd

prompt = pd.read_csv("prompts_for_image.csv")
for i in range(len(prompt)):
    print(prompt.iloc[i, 0])
    generate_image(prompt.iloc[i, 0], f"generated_images/image_{i}")
