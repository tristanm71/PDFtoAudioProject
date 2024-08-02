import pyttsx3
import PyPDF2

file = input("Enter a file")
book = open(file, 'rb')
if not book:
    exit()

pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)
speaker = pyttsx3.init()
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
