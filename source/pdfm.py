import argparse


def getArguments():
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

def verifyArguments(args):
    """
    Description: Function to verify arguments based on options.
    Arguments:
        args: received arguments.
    Returns:
        None.
    """
    if args.action == "split" and not args.parts:
        print("Value for parts is mandatory when action is split")
        usage()
        exit(1)
    
    if args.action == "merge" and not args.files:
        print("List of files is mandatory when action is merge")
        usage()
        exit(1)
    
def usage():
    print("Utility to either merge the given files, or split files into multiple PDFs")
    print("pdfm.py -a split -p parts or pdfm.py --action split --parts parts")  
    print("pdfm.py -a merge -f file1,file2 or pdfm.py --action split --files file1,file2") 

def main():
    """
    Description: Main function to start the program.
    Arguments:
        No Args.
    Returns:
        None.
    """
    args = getArguments()
    verifyArguments(args)

if __name__ == '__main__':
    main()
    
        