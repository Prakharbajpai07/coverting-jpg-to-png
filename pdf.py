import PyPDF2
with open('dummy.pdf', 'rb') as file: # we opens a pdf file here
    reader = PyPDF2.PdfFileReader(file) #pdf is read and pdf object is return
    print(reader.numPages) #returns the no. of pages in the pdf
    page = reader.getPage(0) #returns page object
    print(page.rotateClockwise(90)) #make the pdf_page anticlockwise and return it
    writer = PyPDF2.PdfFileWriter() #create  a pdf write object
    writer.addPage(page) #add page to the pdf
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
    
