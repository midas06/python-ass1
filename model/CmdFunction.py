from Processor import *


class CmdFunction(object):

    def __init__(self):
        self.processor = Processor()

    def load_file(self, file_path):
        self.processor.validator.empty_bad_data()
        if file_path == "":
            return "No file/path entered"
        else:
            try:
                self.processor.add_data(file_path)
                return "File loaded\nGood data: " + str(self.processor.database.get_length()) + "\nBad data: " + str(self.processor.validator.get_bad_data_len())
            except IOError as not_found_err:
                return "File/path not found"
            except UnicodeDecodeError as bad_format_err:
                return "Not a valid File type"

    def pickle_load_file(self, file_path):
        self.processor.validator.empty_bad_data()
        if file_path == "":
            return "No file/path entered"
        else:
            try:
                self.processor.add_data(file_path)
                return "File loaded\nGood data: " + str(self.processor.database.get_length()) + "\nBad data: " + str(self.processor.validator.get_bad_data_len())
            except IOError as not_found_err:
                return "File/path not found"
            except UnicodeDecodeError as bad_format_err:
                return "Not a valid File type"

    def display_good(self, theMessage):
        if self.processor.filer.get_file_path() == None and self.processor.database.get_length() == 0:
            print("No data to display. Please load a file or run deserialize")
        else:
            self.processor.database.print_all()

    def display_bad(self, msg):
        if self.processor.filer.get_file_path() == None and self.processor.database.get_length() == 0:
            print("No data to display. Please load a file")
        elif len(self.processor.validator.export_bad_data()) == 0:
            print("No bad data to display.")
        else:
            self.processor.validator.print_bad_data()

    def edit_bad(self, value):
        if self.processor.filer.get_file_path() == None and self.processor.database.get_length() == 0:
            return "No data to edit. Please load a file"
        elif len(self.processor.validator.export_bad_data()) == 0:
            return "No bad data to edit."
        else:
            self.processor.process_bad()

    def display_graphs(self, input):
        if self.processor.database.get_length() != 0:
            if input == "1":
                self.processor.pie_bmi()
            elif input == "2":
                self.processor.pie_gender()
            elif input == "3":
                self.processor.scatter_sales()
            elif input == "4":
                self.processor.bar_bmi_vs_gender()
        else:
            print("No data has been loaded")

    def serialize(self, option):
        if option == 0:
            o = 0
        elif option == 1:
            self.processor.set_file_path(input("Please enter the directory you wish to save to:\n"))
            o = 1
        try:
            self.processor.serialize(o)
        except OSError as no_dir_err:
            print("Directory not found")

    def deserialize(self, option):
        if option == 0:
            self.processor.deserialize(0)
        elif option == 1:
            self.processor.set_file_path(input("Please enter the directory you wish to load from:\n"))
            self.processor.deserialize(1)


