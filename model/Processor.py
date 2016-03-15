from model.Validator import *
from model.FileHandler import *
from model.Database import *
from model.Editor import *
from model.Plotter import *
import os.path


class Processor(object):

    def __init__(self):
        self.filer = FileHandler()
        self.validator = Validator()
        self.database = Database()
        self.editor = Editor()
        self.plotter = Plotter()
    """
    def add_data(self, fileloc):
        self.filer.set_filepath(fileloc)
        self.filer.load_file()
        self.filer.strip_tags()
        self.validator.set_raw_data(self.filer.export())
        self.validator.parse_data()
        self.database.add_people(self.validator.export_gooddata())
    """
    def add_data(self, fileloc):
        #strippedString = fileloc.strip()
        #if strippedString is "":
            #return self.filer.get_file_path()
        #else:
            #try:

                #self.validator.empty_raw_data()
                #self.database.empty_database()

                self.filer.set_filepath(fileloc)
                self.filer.load_file()
                self.filer.strip_tags()
                self.validator.set_raw_data(self.filer.export())
                self.validator.parse_data()
                self.database.add_people(self.validator.export_gooddata())
            #except FileNotFoundError as not_found_err:
                #print("File not found")
            #jess
            #except IOError as not_found_err:
                #print("No such file or directory: " + fileloc)
                #return IOError

    def check_path(self, fileloc): #checks if file exist
        exist = False
        if os.path.isfile(fileloc) == True:
            exist = True
        return  exist

    def process_bad(self):
        if self.validator.has_baddata():
            self.editor.set_raw(self.validator.export_baddata())
            self.editor.edit()
            self.database.add_people(self.editor.export_gooddata())


    def serializetest(self):
        self.database.serialize()
        self.database.deserialize()

    def pie_bmi(self):
        dist = self.database.get_bmi_distribution()
        self.plotter.pie_bmi(dist["normal"], dist["overweight"], dist["obese"], dist["underweight"])

    def pie_gender(self):
        dist = self.database.get_gender_distribution()
        self.plotter.pie_gender(dist["males"], dist["females"])

    def scatter_sales(self):
        sales_list = self.database.get_sales_ordered()
        self.plotter.scatter_sales(sales_list)


# a = Processor()
# a.add_data("test.csv")
# a.scatter_sales()