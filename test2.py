from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


image_path = "tax-invoice-1-8-1000x1000.webp"
img = Image.open(image_path)

text = pytesseract.image_to_string(Image.open(image_path))
print(text)


filename = "text2.txt"
with open(filename, "w") as f:
    f.write(text)