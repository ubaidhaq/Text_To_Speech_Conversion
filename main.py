import pytesseract
from PIL import Image 
from pytesseract import image_to_string 
from gtts import gTTS
pytesseract.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img=Image.open('C:/Users/Admin/Desktop/Text_To_Speech_Conversion/image4.jpg')

text=image_to_string(img)

speech=gTTS(text)
speech.save('C:/Users/Admin/Desktop/Text_To_Speech_Conversion/Speech.mp3')
