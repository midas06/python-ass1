from FileHandler import *
from Database import *
from Editor import *
from Plotter import *


class Processor(object):

    def __init__(self):
        self.filer = FileHandler()
        self.validator = Validator()
        self.database = Database()
        self.editor = Editor()
        self.plotter = Plotter()

    def add_data(self, fileloc):
        self.database.empty_database()
        self.filer.set_filepath(fileloc)
        self.filer.load_file()
        self.filer.strip_tags()
        self.validator.set_raw_data(self.filer.export())
        self.validator.parse_data()
        self.database.add_people(self.validator.export_good_data())

    def process_bad(self):
        if self.validator.has_bad_data():
            self.editor.set_raw(self.validator.export_bad_data())
            self.editor.edit()
            self.database.add_people(self.editor.export_good_data())

    def set_file_path(self, new_path):
        self.database.set_directory(new_path)

    def get_file_path(self):
        return self.database.get_directory()

    def serialize(self, option):
        self.database.serialize(option)

    def deserialize(self, option):
        self.database.empty_database()
        self.database.deserialize(option)

    def pie_bmi(self):
        dist = self.database.get_bmi_distribution()
        self.plotter.pie_bmi(dist["normal"], dist["overweight"], dist["obese"], dist["underweight"])

    def pie_gender(self):
        dist = self.database.get_gender_distribution()
        self.plotter.pie_gender(dist["males"], dist["females"])

    def scatter_sales(self):
        sales_list = self.database.get_sales_ordered()
        self.plotter.scatter_sales(sales_list)

    def bar_bmi_vs_gender(self):
        self.plotter.bar_bmi_vs_gender(self.database.get_male_bmi(),self.database.get_female_bmi() )
