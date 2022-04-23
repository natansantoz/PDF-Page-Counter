import PyPDF2
import os, sys
import warnings



def print_header():
    print("|=============================================================================================|")
    print("|------------------------------------- PDF Pages Counter -------------------------------------|")
    print("|=============================================================================================|")
    print("| Pages |", " " * 33, "Book Name", " " * 39, "|")
    print("|-------|-------------------------------------------------------------------------------------|")


def print_footer(total_pages=0):
    print("|", " " * 5, "|", " " * 83, "|")
    print("|-------|-------------------------------------------------------------------------------------|")
    print("| Total |", total_pages, " " * (81 - len(str(total_pages))), " |")
    print("|=============================================================================================|")
    print("| author's github: natansantoz                                                                |")
    print("|=============================================================================================|")


def get_pdf_names():
    if getattr(sys, 'frozen', False):
        exe_path = os.path.dirname(sys.executable)
        pdf_names = [f for f in os.listdir(exe_path) if f.endswith('.pdf')]
        return pdf_names
    elif __file__:
        path = os.path.dirname(os.path.abspath(__file__))
        pdf_names = [f for f in os.listdir(path) if f.endswith('.pdf')]
        return pdf_names


def print_books_and_pages(pdf_names):
    total_pages = 0
    for pdf in pdf_names:
        with open(pdf, 'rb') as file:

            pdf = pdf.strip()
            readpdf = PyPDF2.PdfFileReader(file)
            pages = readpdf.numPages
            total_pages += pages
            pdf = pdf[:83]

            string = "|  " + str(pages) + (5 - len(str(pages)) ) * " " + "| " + pdf + " |"

            if len(string) <= 94:
                string = string[:-1]
                string = string + " " * (94 - len(string)) + "|"
            print(string)
    return total_pages



warnings.filterwarnings("ignore")

print_header()     

pdf_names = get_pdf_names()
total_pages = print_books_and_pages(pdf_names)

print_footer(total_pages)

os.system('pause')