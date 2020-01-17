from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os.path import splitext
import pdftotext
from gtts import gTTS

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filelocation = askopenfilename() # open the dialog GUI

with open(filelocation, "rb") as f:  # open the file in reading (rb) mode and call it f
    pdf = pdftotext.PDF(f)  # store a text version of the pdf file f in pdf variable

pdf = ''.join(pdf); # join the text together

final_file = gTTS(text=pdf, lang='en')  # store file in variable
outname = splitext(filelocation)[0] + '.mp3'
final_file.save(outname)  # save file to computer

