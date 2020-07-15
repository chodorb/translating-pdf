from PyPDF2 import PdfFileReader, PdfFileWriter
from googletrans import Translator

trans = Translator()




file_path = 'pdf.pdf'
pdf = PdfFileReader(file_path)
 
with open('translation_pl.txt', 'w', encoding='utf=8') as f:
    for page_num in range(pdf.numPages):
       
        pageObj = pdf.getPage(page_num)
 
        try: 
            txt = pageObj.extractText()
            t = trans.translate(txt,dest='pl',src='auto')
        except:
            pass
        else:
            f.write(f'Page {page_num+1}\n')
            f.write(t.text)
    f.close()


with open('translation_en.txt', 'w', encoding='utf=8') as f:
    for page_num in range(pdf.numPages):
       
        pageObj = pdf.getPage(page_num)
 
        try: 
            txt = pageObj.extractText()
            t = trans.translate(txt,dest='en',src='auto')
        except:
            pass
        else:
            f.write(f'Page {page_num+1}\n')
            f.write(t.text)
    f.close()

with open('translation_fr.txt', 'w', encoding='utf=8') as f:
    for page_num in range(pdf.numPages):
       
        pageObj = pdf.getPage(page_num)
 
        try: 
            txt = pageObj.extractText()
            t = trans.translate(txt,dest='fr',src='auto')
        except:
            pass
        else:
            f.write(f'Page {page_num+1}\n')
            f.write(t.text)
    f.close()