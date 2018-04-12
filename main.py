import sys
import argparse
from processFile import processFile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFilePath", type=str)
    parser.add_argument("stringSize", type=int)
    args = parser.parse_args()

    filePath = args.inputFilePath
    n = args.stringSize
    #print(filePath)

    process = processFile(filePath, n)
    process.readFile()


if __name__ == "__main__":
    main()