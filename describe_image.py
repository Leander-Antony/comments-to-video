from transformers import AutoProcessor, BlipForConditionalGeneration
from PIL import Image


processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
# image = Image.open(requests.get('image.pngs', stream=True).raw)
image = Image.open("image.png")
text = "A picture of"

inputs = processor(images=image, text=text, return_tensors="pt")

outputs = model.generate(**inputs)
caption = processor.tokenizer.decode(outputs[0], skip_special_tokens=True)
print(caption)