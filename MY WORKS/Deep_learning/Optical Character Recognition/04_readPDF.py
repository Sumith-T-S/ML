import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "/home/sumith/Downloads/Workouts ML/02.Deep Learning/Optical Character Recognition/data/Resume.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

for text in recognized_text:
	print(text)
