# import PyPDF2
# import sys
# import os

# merger = PyPDF2.PdfMerger()

# for file in os.listdir(os.curdir):
#     if file .endswith(".pdf"):

#         # print(file)
#         merger.append(file)
#     merger.write("combined.pdf")


import PyPDF2
import os

merger = PyPDF2.PdfMerger()
def merge(file):
    merger.append(file)
    merger.write("combined.pdf")

def main():
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merge(file)

if __name__ == ("__main__"):
    main()

