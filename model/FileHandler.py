class FileHandler(object):
    """
    Deals with importing data from files, and converting to a list of strings.
    """

    def __init__(self):
        self._filepath = None
        self._filedata = None

    def set_filepath(self, new_filepath):
        self._filepath = new_filepath

    def load_file(self):
        with open(self._filepath, 'r') as f:
            temp = f.read()
            self._filedata = temp.splitlines()

    def strip_tags(self):
        opening_line = self._filedata[0]
        str_array = opening_line.split(",")
        if str_array[0] == "ID":
            del self._filedata[0]

    def export(self):
        return self._filedata

    def get_file_path(self):
        return self._filepath

