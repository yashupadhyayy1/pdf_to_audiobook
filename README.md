# PDF Text-to-Speech

This script uses the PyPDF2 and pyttsx3 libraries to extract text from a PDF file and convert it to speech using text-to-speech (TTS) technology.

## Dependencies

Make sure you have the following dependencies installed:

- PyPDF2
- pyttsx3

You can install them using the following command:


## Usage

1. Place the PDF file you want to convert in the same directory as this script.
2. Replace the `*/*.pdf` in the `book = open(' */*.pdf','rb')` line with the relative path or filename of your PDF file.
3. Run the script.

The script will read each page of the PDF file, extract the text, and convert it to speech using the default system TTS engine.

## Visualization

The script does not provide any visual output, but it converts the text from each page of the PDF file into speech using the default system TTS engine.

Note: The visualization of this code is auditory rather than visual. The script reads out the text from each page of the PDF file using the computer's speakers or audio output device.

## Important Note

Uncommenting the line `# pyttsx3.init().say(text)` and commenting out `speaker.say(text)` will enable the TTS to be played immediately after each page is processed, without waiting for the entire script to complete.
