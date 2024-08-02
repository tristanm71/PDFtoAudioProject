import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)
speaker = pyttsx3.init()
for num in range(7, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()