import sys;
from PyPDF2 import PdfMerger;
import argparse;
import os;

INVALID_FILE_TYPE = "Invalid file type. Only PDF files are allowed.";
INVALID_PATH = "Invalid path. Please check the path and try again.";

def validate_file(filename):
    if not os.path.exists(filename):
        print(INVALID_FILE_TYPE%(filename));
        sys.exit(1);
    elif not filename.endswith(".pdf"):
        print(INVALID_FILE_TYPE%(filename));
        sys.exit(1);
    return;

def main():
    parser = argparse.ArgumentParser(description='Merge PDF files');
    parser.add_argument("pdf", nargs = '*', metavar = "pdfs", type = str, 
                    help = "PDF files to be merged in the order you want them to be merged.");
    parser.add_argument("-o", "--output", nargs=1, type=str,
                    metavar = "output_destination", default = "out.pdf", help="Output destination filename");
    args = parser.parse_args();
    if(args.pdf is None):
        print(str(args.pdf));
        sys.exit(1);
    merger = PdfMerger();
    for pdf in args.pdf:
        validate_file(pdf);
        merger.append(pdf);
    merger.write(args.output[0]);
    merger.close();

if __name__ == "__main__":
    main();