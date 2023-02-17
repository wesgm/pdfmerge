import sys;
from PyPDF2 import PdfMerger;
import argparse;
import os;
'''
TODO:
-Move merging logic to a separate class/function
-Add cli options to build files
'''
INVALID_PATH = "Invalid path. Please check the path and try again.";
INVALID_DIR = "Invalid directory. Please check the path and try again.";

def main():
    parser = argparse.ArgumentParser(prog = "pdfmerge", description="Merge PDF files");
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.1");
    parser.add_argument("-d", "--dir", metavar="dir", type=str, nargs='?', default=None, help="Path to directory to merge all PDF files in the directory");
    parser.add_argument("files", nargs = '*', metavar = "files", type = str, default = [],
                    help = "PDF files to be merged in the order you want them to be merged.");
    parser.add_argument("-o", "--output", nargs='?', type=str,
                    metavar = "output", default = "merged-files.pdf", help="Output destination of the merged PDF file. Default is merged-files.pdf");
    args = parser.parse_args();
    print(args.output)
    if(args.dir is None and len(args.files) == 0):
        print("No files specified. Please try again.");
        sys.exit(1);
    if(args.dir is not None):
        if not os.path.exists(args.dir):
            print(INVALID_PATH%(args.dir));
            sys.exit(1);
        if not os.path.isdir(args.dir):
            print(INVALID_DIR%(args.dir));
            sys.exit(1);
        files = os.listdir(args.dir);
        files = [os.path.join(args.dir, file) for file in files if file.endswith(".pdf")];
        args.files = files;
    merger = PdfMerger();
    #if dir is specified, then we ignore the -f option and just merge all of the file in dir
    #if dir is not specified, then we merge the files specified in -f option
    for file in args.files:
        if not os.path.exists(file):
            print(INVALID_PATH%(file));
            sys.exit(1);
        if(file.endswith(".pdf")):
            merger.append(file);
    merger.write(args.output);
    merger.close();

if __name__ == "__main__":
    main();