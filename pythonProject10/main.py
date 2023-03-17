import PyPDF2
import pyttsx3
#import subprocess
# Open the PDF file
with open('pradeep1.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    #pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    #pdf_file.close()
    #subprocess.run(['open', 'pradeep.pdf'], check=True)

    # Extract the text from the PDF file
    text =''
    for page in pdf_reader.pages:
        text += page.extract_text()


    # Create a text-to-speech engine
    engine = pyttsx3.init()

    # Set the rate and volume of the speech
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)

    # Say the text
    engine.say(text)
    engine.runAndWait()

