from PIL import Image
import pytesseract



img = Image.open("text.png")
text = pytesseract.image_to_string(img, lang="eng") # resmi text'e çeviriyor
print(text)

