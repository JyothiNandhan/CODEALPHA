import pytesseract
from PIL import Image
from gtts import gTTS
import os

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image_path="C:\\Users\\LENOVO\\Desktop\\swami-vivekananda-quotes-images.jpg"


img=Image.open(image_path)

text_convert=pytesseract.image_to_string(img)

text_to_speech=gTTS(text_convert)


audiofile="output.mp3"
text_to_speech.save(audiofile)
os.system("output.mp3")