import os
import traceback


class processFile:

    def __init__(self, filePath, n):
        self.location = filePath
        self.n = n
        self.count = 0
        # self.match = False

        # print(self.location)

    def readFile(self):

        # proceed only if the file exists on the given path
        if os.path.exists(self.location):
            #print("ok, so the path exists..")
            # read the file inside of a try-catch block so that you can catch any IO exceptions if thrown
            try:
                with open(self.location) as inputFile:

                    # read each line in the file
                    for line in inputFile:
                        result = self.processLines(line)

                        # if the pattern found in line is valid, add to the count and print the line
                        if result:
                            self.count += 1
                            print(str(line))

                print(self.count)

            # catch the exception if thrown and print the stack
            except IOError as e:
                print("Encountered an IOError ({0}): {1}".format(e.errno, e.strerror))
            except Exception as ex:
                print(traceback.format_exc())

        # print the error message if file not found and return to the caller
        else:
            print("The file does not exist at the path provided.")
            return

    def processLines(self, line):

        k = self.n
        # test
        #print("in processLines")

        # treating line as a string
        currLine = str(line)
        # test
        print('\n' + currLine)

        # get the length of current line/string
        length = len(currLine)
        # test
        print("line size" + str(length))

        # structure to check if there is a palindrome, if so , return true
        match = False
        #i = 0
        #while self.n <= lineSize:
        for k in range(k, length):

            # fix the starting index
            i = 0
            while i < (length - k + 1):
                #i = 0
            #for i in range (0 , )
                # test
                # print("i=" + str(i))

                # get the ending index of substring from starting index i and length k
                j = i + k - 1
                # test
                # print("j=" + str(j))

                # checking for sub-string from ith index to jth index if
                # st[i+1] to st[(j-1)] is a palindrome

                # test
                #first = currLine[i]+currLine[i+1]
                #second = currLine[j-1]+currLine[j]
                #print("*******")
                #print(first)
                #print(second)
                #print("*******")
                #print()

                # check if the current number of characters form a palindromic string
                #if currLine[i] == currLine[j] and currLine[i+1] == currLine[j-1]:


                if currLine[i] == currLine[j]:

                    # self.match = False
                    first = currLine[i]
                    second = currLine[j]

                    mid = int((i + j + 1)/2)

                    for x in range(i+1, mid):

                        for y in range(j-1, mid-1, -1):

                            first = first + currLine[x]
                            second = second + currLine[y]
                                # if length of current line is the number of characters to be searched, it is a valid match
                                #if length == self.n:
                                #    match = True

                                # if the characters before the palindrome string are  '[' and ']', then match is invalid
                                #elif currLine[i - 1] == "[" and currLine[j + 1] == ']':
                                #    match = False

                                #else:
                                #    match = True

                    if first == second:
                        if length == self.n:
                            match = True
                        elif currLine[i - 1] == "[" and currLine[j + 1] == ']':
                            match = False
                        else:
                            match = True

                    print(first)
                    print(second)
                    # match = True

                    print(match)
                    return match

                else:
                    match = False
                    print(match)

                i += 1
