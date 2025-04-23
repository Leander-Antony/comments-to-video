## 📽️ Project Workflow

1. **Scrape Top Comments**  
   → Extracts top comments from funny YouTube videos using the YouTube API.

2. **Generate Prompts**  
   → Converts those comments into visual storytelling prompts using a language model.

3. **Image Generation**  
   → Uses image generation models (Stable Diffusion) to visualize each prompt.

4. **Image Description**  
   → Generates a caption or description for each image to guide animation.

5. **Animation**  
   → Uses AI to animate images based on their content and descriptions.

6. **Compilation**  
   → Merges the animated clips into a single, humorous video file.

---

## 🛠️ Tech Stack

- **Languages**: Python
- **APIs/Models**:
  - YouTube Data API 
  - Ollama (llama3)
  - runwayml/stable-diffusion-v1-5 (for image generation)
  - Salesforce/blip-image-captioning-base (for generate captions/descriptions)
  - hysts/zeroscope-v2 (for video generation)
  - moviepy (to combine the videos)


