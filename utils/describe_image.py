from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image

def describe(image):
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    image = Image.open(f"{image}")
    text = "An illustration of"

    inputs = processor(images=image, text=text, return_tensors="pt")

    outputs = model.generate(**inputs)
    caption = processor.tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption