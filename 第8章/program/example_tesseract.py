import pytesseract
from PIL import Image
image = Image.open('验证码.png')
code = pytesseract.image_to_string(image)
print(code)

