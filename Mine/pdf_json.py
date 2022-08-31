import json    
import PyPDF2

path = r"C:\Users\DM\Desktop\pdf\1_zhuxuyi.pdf"
pdf_file = open(r"C:\Users\DM\Desktop\pdf\1_zhuxuyi.pdf", 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()

page_content = page_content.replace('练习1','')
page_content = page_content.replace('1','')
page_content = page_content.replace("https://ibaotu.com/https://ibaotu.com/",'')

x= page_content.split()
# print(x)

new_path = path.replace('.pdf', ".json")

dict = {"字符": x}

with open(new_path, "a", encoding="utf-8") as f:
    f.write(json.dumps(dict, ensure_ascii=False, indent=2))
