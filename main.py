import getopt
import sys


class CalendarEntry:
    def __init__(self, titles, entries):
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

            titles = ""

            for x in lines:
                if x != "\n":
                    titles += x
                else:
                    break

            lines = lines.replace(titles, "").replace("\n", " ").replace('"', '').split(",")

            titles = titles.replace('"', '').split(",")

            print(titles)

            EntryObjects = list()
            entry = ""
            index = 0
            for x in lines:
                entry += x + ";@!"
                index += 1
                if index % (len(titles) - 1) == 0:
                    EntryObjects.append(CalendarEntry(titles, entry))
                    entry = ""

            for x in EntryObjects:
                x.printData()

        except Exception:
            print("Could not open the file.")
            raise


if __name__ == "__main__":
    main(sys.argv[1:])
