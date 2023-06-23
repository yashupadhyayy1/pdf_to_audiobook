# Open the PDF file
book = open('your_file_Location.pdf', 'rb')

# Create a PdfFileReader object to read the PDF data
pdfdata = PyPDF2.PdfFileReader(book)

# Get the total number of pages in the PDF
pages = pdfdata.numPages

# Iterate through each page
for i in range(536):
    # Get the specific page
    page = pdfdata.getPage(i)

    # Extract the text from the page
    text = page.extractText()

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Uncomment the line below to directly play the text as audio
    # '''pyttsx3.init().say(text)'''

    # Convert the text to speech
    speaker.say(text)

    # Run the text-to-speech engine and wait until speech is complete
    speaker.runAndWait()
