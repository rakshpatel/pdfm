"""
Simple utility to work with PDF
"""
import math
import argparse
import sys
import PyPDF2

def get_arguments():
    """
    Description: Function to receive arguments for proram.
    Arguments:
        No Args.
    Returns:
        Argumens received.
    """
    parser = argparse.ArgumentParser(description='Process PDF files.')
    parser.add_argument(
        "-a",
        "--action",
        type=str,
        help="action=merge/split.",
        required=True
        )

    parser.add_argument(
        "-p",
        "--parts",
        type=int,
        help="files to be split into no of parts."
    )

    parser.add_argument(
        "-f",
        "--files",
        type=str,
        help="list of files to be merged. comma/space separated."
    )
    args = parser.parse_args()
    return args

def verify_arguments(args):
    """
    Description: Function to verify arguments based on options.
    Arguments:
        args: received arguments.
    Returns:
        True/False based on validations.
    """

    if args.action == "split" and (not args.parts or not args.files):
        print("Value for parts and files is mandatory when action is split")
        usage()
        return False
    

    if args.action == "merge" and not args.files:
        print("List of files is mandatory when action is merge")
        usage()
        return False
    return True

def usage():
    """
    Description: Prints usage information
    Arguments:
        No Args.
    Returns:
        None.
    """
    print("Utility to either merge the given files, or split files into multiple PDFs")
    print("pdfm.py -a split -p parts or pdfm.py --action split --parts parts")
    print("pdfm.py -a merge -f file1,file2 or pdfm.py --action split --files file1,file2")

def pdf_split(file, parts):
    """
    Description: Split the given pdf file into multiple files
    Arguments:
        file: File to be splitted.
        parts: No of parts. File should be split into parts.
    Returns:
        None.
    """
    print(file, parts)
    with open(file, 'rb') as file_object:
        reader = PyPDF2.PdfFileReader(file_object)
        num_pages = reader.numPages
        page_per_pdf = math.ceil(num_pages/parts)
        print("Each part will contain, approximately {} pages.\nLast file may contain less based on total pages in original file.".format(page_per_pdf))
        if parts > num_pages:
            print("File can't be split into {} parts, as it has only {} pages. Parts should be <= {}".format(parts, num_pages, num_pages))
            sys.exit(1)
        
        for page in range(num_pages):
            if page % page_per_pdf == 0:
                print("Write")

def main():
    """
    Description: Main function to start the program.
    Arguments:
        No Args.
    Returns:
        None.
    """
    args = get_arguments()
    if verify_arguments(args):
        if args.action == "split":
            pdf_split(args.files, args.parts)

if __name__ == '__main__':
    main()
