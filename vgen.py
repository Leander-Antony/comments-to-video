import shutil
from gradio_client import Client
import os

# Initialize client
client = Client("hysts/zeroscope-v2")

# Generate the video
result = client.predict(
    prompt="a picture of a person standing on a cliff with a sword",
    seed=0,
    num_frames=24,
    num_inference_steps=25,
    api_name="/run"
)

# Get the temp video path
temp_video_path = result['video']

# Set target path to same directory as this script
target_dir = os.path.dirname(os.path.abspath(__file__))
target_path = os.path.join(target_dir, "generated_video.mp4")

# Copy the file
shutil.copy(temp_video_path, target_path)
print(f"Video saved to: {target_path}")
