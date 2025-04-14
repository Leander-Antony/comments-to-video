import shutil
from gradio_client import Client
import os

def generate_video(prompt, filename="generated_video.mp4", seed=0, num_frames=24, num_inference_steps=25):
    client = Client("hysts/zeroscope-v2")

    result = client.predict(
        prompt=prompt,
        seed=seed,
        num_frames=num_frames,
        num_inference_steps=num_inference_steps,
        api_name="/run"
    )

    temp_video_path = result['video']

    target_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(target_dir, filename)

    shutil.copy(temp_video_path, target_path)
    print(f"Video saved to: {target_path}")
    return target_path

generate_video("a cyberpunk samurai walking in the rain", filename="samurai_rain.mp4")