import getopt
import sys


class Calendar:
    """
    Summarizes all entries.

    Attributes:

    """

    def __init__(self, csvFileInput):
        self.titles = []
        self.entries = []

        titles = ""

        for lines in csvFileInput:
            if lines != "\n":
                titles += lines
            else:
                break

        lines = csvFileInput.replace(titles, "").replace("\n", " ").replace('"', '').split(",")

        self.titles = titles.replace('"', '').split(",")

        print(titles)

        entry = ""
        index = 0
        for lines in lines:
            entry += lines + ";@!"
            index += 1
            if index % (len(titles) - 1) == 0:
                self.entries.append(CalendarEntry(titles, entry))
                entry = ""

    def printCalendar(self):
        for entry in self.entries:
            print(entry)


class CalendarEntry:
    """
    A single entry.

    Attributes:

    """

    def __init__(self, titles, entries):
        """
        The constructor for CalendarEntry class.

        Parameters:

        """
        self.titleData = {}

        for titleIndex in range(len(titles)):
            self.titleData[titles[titleIndex]] = entries.split(";@!")[titleIndex]

        # var = self.data.split(";@!")

    def printData(self):
        print(self.titleData)


def main(argv):
    inputfile = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hoi:v", ["help", "output=", "input="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    output = None
    verbose = False
    for opt, arg in opts:
        if opt == "-v":
            verbose = True
        elif opt in ("-h", "--help"):
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

    if inputfile != "":
        try:
            csvFile = open(inputfile, mode="r")  # opening the file in read mode
            lines = csvFile.read()  # reading the file and splitting into lines
            # titles = lines[0].replace('"', '').split(",")  # isolating titles/columns
            # columns = len(titles)

        except OSError:
            print("Could not open/read file:", inputfile)
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
