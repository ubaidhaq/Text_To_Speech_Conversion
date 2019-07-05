For Text Extraction
download an exe file from the following link
https://github.com/UB-Mannheim/tesseract/wiki 
install it in C drive 

Then open cmd and execute these two commands
pip install pytesseract
pip install pillow 

run this line in your python script 
pytesseract.pytesseract.tesseract_cmd= r"<your path>\Tesseract-OCR\tesseract.exe"

For Speech conversion
execute this command in cmd 
pip install gTTS

provide the path of the image in Image.open() function
execute main.py

Exceptions:
Not working accurately with stylish writing styles.


Sample images and mp3 file is uploaded. 