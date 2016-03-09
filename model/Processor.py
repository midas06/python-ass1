from model.Person import *
from model.Validator import *
from model.FileHandler import *


class Processor(object):

    def __init__(self):
        self.filer = FileHandler()
        self.validator = Validator()

    def run(self, fileloc):
        self.filer.set_filepath(fileloc)
        self.filer.load_file()
        self.filer.strip_tags()
        self.validator.set_raw_data(self.filer.export())
        # d = self.validator.get_gooddata()
        self.validator.parse_data()
        d = self.validator._good_data
        print(d.items())
a = Processor()
a.run("test.csv")
