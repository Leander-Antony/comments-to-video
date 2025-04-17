from utils.describe_image import describe
from utils.image_gen import generate_image
from utils.video_gen import generate_video

# generate_image("""In the ruins of "Carnival Chaos," a lone figure stands amidst twisted carnival games and flaming Ferris wheels. His eyes widen in horror as he realizes his friend's betrayal - not because it hurts, but because it's just so... Neutral.""","image1")

cpt = describe("image1.png")
print(cpt)