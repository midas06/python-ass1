from model.Validator import *
from model.FileHandler import *
from model.Database import *
from model.Editor import *


class Processor(object):

    def __init__(self):
        self.filer = FileHandler()
        self.validator = Validator()
        self.database = Database()
        self.editor = Editor()

    def add_data(self, fileloc):
        self.filer.set_filepath(fileloc)
        self.filer.load_file()
        self.filer.strip_tags()
        self.validator.set_raw_data(self.filer.export())
        self.validator.parse_data()
        self.database.add_people(self.validator.export_gooddata())


    def process_bad(self):
        if self.validator.has_baddata():
            self.editor.set_raw(self.validator.export_baddata())
            self.editor.edit()

    def serializetest(self):
        self.database.serialize()
        self.database.deserialize()


a = Processor()
a.add_data("test.csv")
a.serializetest()