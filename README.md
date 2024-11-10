
# Convert PDF to Audiobook

This Python project enables you to convert PDF files into audio files, allowing you to create audiobooks from any PDF document. It uses PyMuPDF for text extraction from PDFs and an external Text-to-Speech (TTS) API (e.g., iSpeech API) to generate the audio output.

## Features

- Extract text from PDF documents
- Convert extracted text to speech using a TTS API
- Save the generated audio as an MP3 file
- Play the audio file after conversion for immediate listening

## Prerequisites

Before running the code, you need to install the following Python packages:

```bash
pip install requirments.txt
```

Additionally, ensure you have `ffmpeg` installed, which is required by the `pydub` library for handling audio files. You can install `ffmpeg` via:

- **Windows**: [Download and Install](https://ffmpeg.org/download.html)
- **macOS** (via Homebrew): `brew install ffmpeg`
- **Linux** (Debian/Ubuntu): `sudo apt update && sudo apt install ffmpeg`

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Prathamesh326/Convert-PDF-to-Audiobook.git
   cd Convert-PDF-to-Audiobook
   ```

2. Replace `'YOUR_API_KEY'` in the `text_to_speech` function with your actual API key from [iSpeech](https://www.ispeech.org/api).

3. Update the paths in the example usage section of `pdf_to_audiobook` with the paths to your PDF files and preferred output location.

## Usage

To convert a PDF file to an audiobook, call the `pdf_to_audiobook` function with the PDF path and the output path for the audio file:

```python
pdf_path = 'path/to/your/sample.pdf'           # Path to your PDF file
audio_output_path = 'path/to/save/output.mp3'  # Path to save the audio file

pdf_to_audiobook(pdf_path, audio_output_path)
```

### Functions Overview

- `extract_text_from_pdf(pdf_path)`: Extracts text content from the given PDF file.
- `text_to_speech(text, output_file)`: Converts the extracted text into audio using the iSpeech API and saves it as an MP3.
- `pdf_to_audiobook(pdf_path, audio_output_path)`: Complete pipeline function that extracts text, converts it to speech, and plays the audio.

## Example

```python
# Main Function: PDF to Audiobook
pdf_to_audiobook('pdf/sample.pdf', 'audio/output.mp3')
```

This will:
1. Extract text from `sample.pdf`
2. Convert the text to speech
3. Save the audio as `output.mp3`
4. Play the generated audio file

## Notes

- Ensure your PDF file has textual content (not scanned images or graphics) for successful text extraction.
- API usage may incur costs if using a paid TTS service.

## License

This project is open-source and available under the MIT License.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss your idea.

## Contact

For any questions or suggestions, feel free to reach out at: [https://github.com/Prathamesh326](https://github.com/Prathamesh326)

---

Enjoy your audiobooks!
