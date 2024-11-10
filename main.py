import fitz  # PyMuPDF
import requests
import os
from pydub import AudioSegment
from pydub.playback import play

# PDF to Text Extraction Function
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            text += page.get_text()
    return text

# Text-to-Speech Conversion Function (using iSpeech API as an example)
def text_to_speech(text, output_file):
    # API URL and parameters (replace 'YOUR_API_KEY' with an actual key)
    url = "https://api.ispeech.org/api/rest"
    params = {
        'apikey': 'YOUR_API_KEY',  # Replace with your actual iSpeech API key
        'action': 'convert',
        'text': text,
        'voice': 'usenglishfemale',  # Choose a voice (check iSpeech API docs for options)
        'format': 'mp3'
    }
    
    # Making the request to the TTS API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print("Text-to-Speech conversion successful. Audio saved as:", output_file)
    else:
        print("Error in TTS API request:", response.status_code, response.text)

# Main Function: PDF to Audiobook
def pdf_to_audiobook(pdf_path, audio_output_path):
    # Step 1: Extract text from the PDF
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)
    if not text.strip():
        print("No text found in PDF.")
        return
    
    # Step 2: Convert text to speech
    print("Converting text to speech...")
    text_to_speech(text, audio_output_path)

    # Step 3: Play the generated audio file
    print("Playing audio...")
    audio = AudioSegment.from_mp3(audio_output_path)
    play(audio)

# Example usage
pdf_path = 'pdf\sample.pdf'           # Path to your PDF file
audio_output_path = 'audio\output.mp3'  # Path to save the audio file

pdf_to_audiobook(pdf_path, audio_output_path)
