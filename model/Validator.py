from Person import *
import re


class Validator:

    def __init__(self):
        self._good_data = {}
        self._bad_data = []
        self._raw_data = None

    def set_raw_data(self, new_data):
        self._raw_data = new_data

    def to_obj(self, a_list):
        new_person = Person(a_list[0], a_list[1], a_list[2], a_list[3], a_list[4], a_list[5])
        return new_person

    def parse_data(self):
        for i in self._raw_data:
            a_list = self.clean_input(i)

            if self.isvalid(a_list):
                p = self.to_obj(a_list)
                self._good_data.update({p.get_id(): p})
            else:
                self._bad_data.append(i)

    def export_good_data(self):
        return self._good_data

    def export_bad_data(self):
        return self._bad_data

    def has_bad_data(self):
        return len(self._bad_data) > 0

    ###
        # clean methods

    @staticmethod
    def clean_input(an_input):
        the_input = an_input.replace(" ", "")
        the_input = the_input.split(",")
        try:
            the_input[0] = Validator.clean_id(the_input[0])
            the_input[1] = Validator.clean_gender(the_input[1])
            the_input[2] = Validator.clean_age(the_input[2])
            the_input[3] = Validator.clean_sales(the_input[3])
            the_input[4] = Validator.clean_bmi(the_input[4])
            the_input[5] = Validator.clean_income(the_input[5])
        except IndexError as e:
            pass
        return the_input

    @staticmethod
    def clean_id(an_id):
        an_id = an_id.title()
        if len(an_id) > 4:
            ex = len(an_id) - 4
            an_id = an_id[:-ex]

        return an_id

    @staticmethod
    def clean_gender(a_gender):
        if len(a_gender) > 1:
            ex = len(a_gender) - 1
            a_gender = a_gender[:-ex]

        return a_gender.title()

    @staticmethod
    def clean_age(an_age):
        if len(an_age) == 1:
            an_age = "0" + an_age
        return an_age

    @staticmethod
    def clean_sales(a_sale):
        if len(a_sale) == 1:
            a_sale = "00" + a_sale
        elif len(a_sale) == 2:
            a_sale = "0" + a_sale
        return a_sale

    @staticmethod
    def clean_bmi(an_index):
        return an_index.title()

    @staticmethod
    def clean_income(an_income):
        if len(an_income) == 1:
            an_income = "0" + an_income
        return an_income

    ###
        # validate methods
    @staticmethod
    def has_valid_id(an_id):
        pattern = re.compile('^([A-Z]{1}[0-9]{3})+$')

        if pattern.match(an_id) is None:
            return False

        return True

    @staticmethod
    def has_valid_gender(a_gender):
        if a_gender == 'M' or a_gender == 'F':
            return True

        return False

    @staticmethod
    def has_valid_age(an_age):
        pattern = re.compile('^([0-9]{2})+$')

        if pattern.match(an_age) is None:
            return False

        return True

    @staticmethod
    def has_valid_sales(a_sale):
        pattern = re.compile('^([0-9]{3})+$')

        if pattern.match(a_sale) is None:
            return False

        return True

    @staticmethod
    def has_valid_bmi(an_index):
        valid = ["Normal", "Overweight", "Obesity", "Underweight"]

        if an_index in valid:
            return True

        return False

    @staticmethod
    def has_valid_income(an_income):
        pattern = re.compile('^([0-9]{2,3})+$')

        if pattern.match(an_income) is None:
            return False
        return True

    def isvalid(self, a_list):
        if self.has_valid_id(a_list[0]) and self.has_valid_gender(a_list[1]) and self.has_valid_age(a_list[2]) and self.has_valid_sales(a_list[3]) and self.has_valid_bmi(a_list[4]) and self.has_valid_income(a_list[5]):
            return True

        return False

    def print_bad_data(self):
        for i in self._bad_data:
            print(i)

    def get_all_bad_data(self):
        result = ""
        for i in self._bad_data:
            result += i + "\n"
        return result

    def empty_bad_data(self):
        self._bad_data = []

    def get_bad_data_len(self):
        return len(self._bad_data)
