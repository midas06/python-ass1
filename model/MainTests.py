import unittest
from model.CmdFunction import *


class MainTests(unittest.TestCase):
    def setUp(self):
        self.c = CmdFunction()

    def tearDown(self):
        print("next")

    def test_new_file_data_cleared(self):
        """
        Test that good and bad data is erased each time a new file is loaded
        :return:
        """
        self.c = CmdFunction()
        self.c.load_file("test.txt")
        self.assertTrue(self.c.processor.database.getLength() == 0)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 3)

        self.c = CmdFunction()
        self.c.load_file("test.txt")
        self.assertTrue(self.c.processor.database.getLength() == 0)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 3)

        self.c = CmdFunction()
        self.c.load_file("test.csv")
        self.assertTrue(self.c.processor.database.getLength() == 200)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 0)


    def test_gender(self):
        """
        Accepts full words for gender i.e. Male and Female and changes them to M and F
        :return:
        """
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data("N520,Female,57,346,Normal,98")
        self.c.processor.validator.parse_data()
        self.c.processor.database.add_people(self.c.processor.validator.export_gooddata())

        #display fixed data

    def test_edit_data(self):
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data(T109,M,74,861,-,22)
        self.c.processor.validator.parse_data()
        self.c.display_bad()

    """
    def test_edit_file(self):

        self.c = CmdFunction()
        value = ["id_", "gender", "age", "sales", "bmi", "income"]
        correctInput = ["w111, F, 11, 111, Normal, 111"]
        for i in range(len(value)):
            self.assertTrue(self.c.processor.editor.set_newvalue(correctInput[i], value[i]) == correctInput[i])
        #self.c.processor.editor.set_newvalue()

"""



if __name__ == "__main__":
    unittest.main(verbosity=2)