#!/usr/bin/env python3
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="KifKif a powerful tool that allows you to check the KifKifness of two files.")
    parser.add_argument('--file1', '-f1', help="first file path")
    parser.add_argument('--file2', '-f2', help="second file path")

    args = parser.parse_args()
    if ( not args.file1 or  not args.file2):
        print("Error: you must specify two files")
        exit(1)
    
    ret = os.popen("grep -F -x -f  %s %s" % (args.file1, args.file2)).read()

    

    if ret == open(args.file1, "r").read():
        print("C'est KifKif yal Khou")
    elif ret == "":
        print("C'est pas KifKif yal hmar")
    else:
        ret = os.popen("grep -F -n -x -f  %s %s" % (args.file1, args.file2)).read()

        print("Que hadom KifKif :\n %s" % ret, end="")

if __name__ == "__main__":
    main()