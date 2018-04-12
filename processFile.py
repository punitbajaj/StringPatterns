import os
import traceback
import re


class processFile:

    def __init__(self, filePath, n):
        """
        Constructor for initialization
        :param filePath: path where the file to be read can be found
        :param n: length of the pattern to be found
        """
        self.location = filePath
        self.n = n
        self.count = 0

    def readFile(self):
        """Takes the  file path provided, opens the file and reads it one line at a time.

        Throws an exception if it cannot find or read the file.

        Prints the line if a valid pattern is found and also prints the total number of
        lines with valid pattern."""

        # proceed only if the file exists on the given path
        if os.path.exists(self.location):

            # read the file inside of a try-catch block so that you can catch any IO exceptions if thrown
            try:
                with open(self.location) as inputFile:

                    # read each line in the file
                    for line in inputFile:
                        result = self.findPattern(line)

                        # if the pattern found in line is valid, add to the count and print the line
                        if result:
                            self.count += 1
                            print(str(line))

                # print how many lines with valid patterns are found
                print("number of lines with pattern: " + str(self.count))

            # catch the exception if thrown and print the stack
            except IOError as e:
                print("Encountered an IOError ({0}): {1}".format(e.errno, e.strerror))
            except Exception as ex:
                print("Unexpected error encountered: " + traceback.format_exc())

        # print the error message if file not found and return to the caller
        else:
            print("The file does not exist at the path provided.")
            return

    def findPattern(self, line):
        """
        Takes the current line being read and finds if a valid pattern exists in it.

        :param line:
        :return: match - True/False depending on if a valid pattern is found
        """

        k = self.n

        # treating line as a string
        currLine = str(line)

        # get the length of current line/string
        length = len(currLine)

        # list to store all the matching patterns found in current line
        matchingPatterns = []

        for i in range(0, (length - k + 1)):

            # get the ending index of substring from starting index i and length k
            j = i + k - 1

            # check if the current number of characters form a palindromic string
            if currLine[i] == currLine[j] and currLine[i+1] == currLine[j-1]:

                # construct the palindrome string
                found = currLine[i] + currLine[i+1] + currLine[j-1] + currLine[j]

                matchingPatterns.append(found)

            #else:
            #    match = False

            i += 1

        # print(matchingPatterns)
        match = self.validate(matchingPatterns, currLine)
        return match

    def validate(self, matchingPatterns, currLine):
        """
        Function validates if all the patterns found in the current line are
        correct or not by making sure they are not within square brackets

        :param matchingPatterns: list of all the patterns found in current line
        :param currLine: current line being processed
        :return: match: Tur/False based on the validiry
        """

        match = False

        # create pattern to extract content from within square brackets
        pattern = '\[(.*?)\]'

        # extract content within all square brackets from the current line
        bracketStrings = re.findall(pattern, currLine)

        # if the constructed palindrome string is found to be in the content from any brackets,
        # the pattern would be invalid or else valid
        for string in matchingPatterns:

            if any(string in item for item in bracketStrings):
                match = False
            else:
                match = True

        # return match

        return match
