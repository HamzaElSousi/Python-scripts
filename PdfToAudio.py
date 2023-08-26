import os
import PyPDF2
from gtts import gTTS

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_audio(text, audio_path, language="en"):
    tts = gTTS(text, lang=language)
    tts.save(audio_path)

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    if not os.path.exists(pdf_path):
        print("PDF file does not exist.")
        return

    text = pdf_to_text(pdf_path)

    audio_path = os.path.splitext(pdf_path)[0] + ".mp3"
    text_to_audio(text, audio_path)

    print(f"Audio file generated: {audio_path}")

if __name__ == "__main__":
    main()
