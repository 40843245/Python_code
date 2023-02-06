
import aspose.words as aw

# Create a blank document.
doc = aw.Document()

# Use a document builder to add content to the document.
builder = aw.DocumentBuilder(doc)
# Write a new paragraph in the document with the text "Hello World!".
builder.writeln("Hello, World!")

# Save the document in DOCX format. Save format is automatically determined from the file extension.
doc.save("output.docx")
