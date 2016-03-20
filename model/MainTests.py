import unittest
from CmdFunction import *


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
        self.assertTrue(self.c.processor.database.get_length() == 0)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 3)

        self.c = CmdFunction()
        self.c.load_file("test.txt")
        self.assertTrue(self.c.processor.database.get_length() == 0)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 3)

        self.c = CmdFunction()
        self.c.load_file("test.csv")
        self.assertTrue(self.c.processor.database.get_length() == 200)
        self.assertTrue(self.c.processor.validator.get_bad_data_len() == 0)

    def test_gender(self):
        """
        Accepts full words for gender i.e. Male and Female as an input and changes them to M and F
        :return:
        """
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data(["N520,Female,57,346,Normal,98"])
        self.c.processor.validator.parse_data()
        self.c.processor.database.add_people(self.c.processor.validator.export_good_data())
        self.assertEqual(self.c.processor.database.get_test_data(),["N520,F,57,346,Normal,98"])

    def test_age(self):
        """
        Accepts single numbers for age as an input and adds 0 before the number i.e. 8 to 08
        :return:
        """
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data(["A558,F,8,885,Normal,517"])
        self.c.processor.validator.parse_data()
        self.c.processor.database.add_people(self.c.processor.validator.export_good_data())
        self.assertEqual(self.c.processor.database.get_test_data(), ["A558,F,08,885,Normal,517"])

    def test_case(self):
        """
        Accepts lower case letters and outputs in the correct format
        :return:
        """
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data(["a558,f,8,885,normal,517"])
        self.c.processor.validator.parse_data()
        self.c.processor.database.add_people(self.c.processor.validator.export_good_data())
        p = Person(self.c.processor.validator.clean_id("a558"), self.c.processor.validator.clean_gender("f"), self.c.processor.validator.clean_age("8"), self.c.processor.validator.clean_sales("885"), self.c.processor.validator.clean_bmi("normal"), self.c.processor.validator.clean_income("517"))
        self.c.processor.database.add_people({p.get_id(): p})
        self.assertEqual(self.c.processor.database.get_test_data(), ["A558,F,08,885,Normal,517"])

    def test_separate_good_bad_data(self):
        """
        Separates good and bad data
        :return:
        """
        self.c = CmdFunction()
        self.c.processor.validator.set_raw_data(["T109,M,74,861,-,22"])
        self.c.processor.validator.parse_data()
        self.c.processor.database.add_people(self.c.processor.validator.export_good_data())
        self.assertTrue(self.c.processor.validator.export_good_data() == {})
        self.assertTrue(self.c.processor.validator.export_bad_data() == ["T109,M,74,861,-,22"])

    def test_delete_bad_data(self):
        """
        Bad data can be deleted
        :return:
        """
        self.c.processor.editor.set_raw(["T109,M,74,861,-,22"])
        a_string = self.c.processor.editor.export_bad_data()[0]
        self.c.processor.editor.remove_from_raw(a_string)
        self.assertEqual(self.c.processor.editor.export_bad_data(), [])

    def test_edit_bad_data(self):
        """
        Bad data can be edited
        :return:
        """
        self.c=CmdFunction()
        self.c.processor.editor.set_raw(["T109,m,74,861,-,22"])
        self.assertEqual(self.c.processor.database.get_length(), 0)
        a_string = self.c.processor.editor.export_bad_data()[0]
        edited_bmi_input = 'Normal'
        p=Person(self.c.processor.validator.clean_id("T109"), self.c.processor.validator.clean_gender("m"), self.c.processor.validator.clean_age("74"), self.c.processor.validator.clean_sales("861"), self.c.processor.validator.clean_bmi(edited_bmi_input), self.c.processor.validator.clean_income("22"))
        self.c.processor.editor.export_bad_data().remove(a_string)
        self.c.processor.database.add_people({p.get_id(): p})
        self.assertEqual(self.c.processor.database.get_length(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)

