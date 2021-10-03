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
    print(args.action)
    

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
    
        