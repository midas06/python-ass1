import os.path
from model.Processor import *

class CmdFunction(object):

    def __init__(self):
        self.processor = Processor()

    def load_file(self, file_path):
        self.processor.validator.empty_bad_data()
        #self.processor.database.empty_database()
        if file_path == "":
            #self.a.empty_data()
            #print("No file/path entered")
            return "No file/path entered"
        elif not self.processor.check_path(file_path):
            #self.a.empty_data()
            #print("File/path not found")
            return "File/path not found"
        else:
            #self.a.empty_data()
            self.processor.add_data(file_path)
            #print("File loaded")
            #print("Good data: " + str(self.processor.database.getLength()))
            #print("Bad data: " + str(self.processor.validator.get_bad_data_len()))
            return "File loaded\nGood data: " + str(self.processor.database.getLength()) + "\nBad data: " + str(self.processor.validator.get_bad_data_len())


    def display_good(self, theMessage):
        if self.processor.filer.get_file_path() == None:
            print("No data to display. Please load a file")
        elif self.processor.database.getLength() == 0:
            print("No good data to display.")
        else:
            self.processor.database.print_all()


    def display_bad(self, msg):
        if self.processor.filer.get_file_path() == None:
            print("No data to display. Please load a file")
            #return "No data to display. Please load a file"
        elif len(self.processor.validator.export_baddata()) == 0:
            #print("No bad data to display.")
            print("No bad data to display.")
        else:
            self.processor.validator.print_bad_data()
            #print(self.processor.validator.get_all_bad_data())

    def edit_bad(self, value):
        if self.processor.filer.get_file_path() == None:
            #print("No data to edit. Please load a file")
            return "No data to edit. Please load a file"
        elif len(self.processor.validator.export_baddata()) == 0:
            #print("No bad data to edit.")
            return "No bad data to edit."
        else:
            self.processor.process_bad()

    """
    def quit(self, theMessage):

        quit = input("Are you sure you want to quit? Y/N \n>>>")
        if quit == 'Y':
            return True
        elif quit == 'N':
            pass
        else:
            print("Invalid answer")
            pass
    """
"""
    def doctests(self, msg):

        >>> c.load_file("")
        No file/path entered

        >>> c.display_good("")
        No data to display. Please load a file

        >>> c.display_bad("")
        No data to display. Please load a file

        >>> c.load_file("test.txt")
        File loaded
        Good data: 0
        Bad data: 3

        >>> c.load_file("test.txt")
        File loaded
        Good data: 0
        Bad data: 3

        >>> c.load_file("test.csv")
        File loaded
        Good data: 200
        Bad data: 0

        >>> c.load_file("test.txt")
        File loaded
        Good data: 0
        Bad data: 3


if __name__ == "__main__":
    import doctest
    c = CmdFunction()
    doctest.testmod()
"""
"""
c = CmdFunction()
value = ["id_", "gender", "age", "sales", "bmi", "income"]
correctInput = ["w111, F, 11, 111, Normal, 111"]
for i in range(len(value)):
    print(c.processor.editor.set_newvalue(correctInput[i], value[i]) == correctInput[i])
"""