from pathlib import Path
import PyPDF2
import os, sys
import warnings



def print_header():
    print("|" + "=" * 93 +"|")
    print("|" + "-" * 37 + " PDF Pages Counter " + "-" * 37 + "|")
    print("|" + "=" * 93 +"|")
    print("| Pages |", " " * 33, "PDF Name", " " * 40, "|")
    print("|-------|" + "-" * 85 + "|")


def print_footer(couldnt_analyze, total_pages=0 ):
    print("|", " " * 5, "|", " " * 83, "|")
    print("|-------|" + "-" * 85 + "|")
    print("| Total |", total_pages, " " * (81 - len(str(total_pages))), " |")
    print("|" + "=" * 93 +"|")
    print("|" + " " * 93 +"|")
    show_unable_message(couldnt_analyze)    
    print("|" + "=" * 93 +"|")
    print("| author's github: natansantoz" + " " * 64 + "|")
    print("|" + "=" * 93 +"|")


def get_pdf_names():
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
        pdf_names = list(Path(exe_path).rglob("*.pdf" ))
        return pdf_names
    elif __file__:
        path = os.path.dirname(os.path.abspath(__file__))
        pdf_names = list(Path(path).rglob("*.pdf" ))
        return pdf_names


def extract_pdf_name(pdf_path):
    pdf_name = pdf_path
    pdf_name = pdf_name.split("\\")
    pdf_name = pdf_name[-1]
    pdf_name = pdf_name[:83]
    return pdf_name


def generate_pages_and_pdf_name_string(qtd_pages, pdf_name):
    string = "|  " + str(qtd_pages) + (5 - len(str(qtd_pages)) ) * " " + \
        "| " + pdf_name + " |"

    if len(string) <= 94:
        string = string[:-1]
        string = string + " " * (94 - len(string)) + "|"
    return string


def print_books_and_pages(pdf_names):
    total_pages = 0
    couldnt_analyze = []

    for pdf in pdf_names:
        pdf_path = str(pdf)
        pdf_name = extract_pdf_name(pdf_path)
        
        with open(pdf_path, 'rb') as file:
            try:
                readpdf = PyPDF2.PdfFileReader(file)
                qtd_pages = readpdf.numPages
                total_pages += qtd_pages
                
                pages_and_pdf_name = generate_pages_and_pdf_name_string(qtd_pages, pdf_name)
                print(pages_and_pdf_name)
            except:
                couldnt_analyze.append(pdf_name)
    
    return total_pages, couldnt_analyze


def show_unable_message(couldnt_analyze):
    if len(couldnt_analyze) > 0:
        print("| Unable to analyze the "+ str(len(couldnt_analyze)) 
        + " following pdfs: " + " " * 52 + "|")
        
        print("|" + "-" * 93 + "|")

        for pdf_name in couldnt_analyze:
            print("| " + pdf_name + " " * (92 - len(pdf_name)) + "|")



warnings.filterwarnings("ignore")

print_header()     

pdf_names = get_pdf_names()
total_pages, couldnt_analyze = print_books_and_pages(pdf_names)

print_footer(couldnt_analyze, total_pages)

os.system('pause')
