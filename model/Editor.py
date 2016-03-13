from model.Validator import *
from model.Person import *


class Editor(object):

    def __init__(self):
        self._raw_data = None
        self._good_data = {}

    def set_raw(self, new_data):
        self._raw_data = new_data

    def edit(self):
        for s in self._raw_data:
            self.validate(s)



    def validate(self, a_string):
        print("bad data: \n" + a_string)
        list_ = a_string.split(',')

        id_ = list_[0]
        if len(list_) > 1:
            gender = list_[1]
        else:
            gender = ""
        if len(list_) > 2:
            age = list_[2]
        else:
            age = ""
        if len(list_) > 3:
            sales = list_[3]
        else:
            sales = ""
        if len(list_) > 4:
            bmi = list_[4]
        else:
            bmi = ""
        if len(list_) > 5:
            income = list_[5]
        else:
            income = ""

        while not Validator.hasvalid_id(id_):
            id_ = self.set_newvalue("A123", "id")

        while not Validator.hasvalid_gender(gender):
            gender = self.set_newvalue("M", "gender")

        while not Validator.hasvalid_age(age):
            age = self.set_newvalue("01", "age")

        while not Validator.hasvalid_sales(sales):
            sales = self.set_newvalue("001", "sales")

        while not Validator.hasvalid_bmi(bmi):
            bmi = self.set_newvalue("Normal, Overweight, Obesity,Underweight", "bmi")

        while not Validator.hasvalid_income(income):
            income = self.set_newvalue("00-100", "income")

        p = Person(Validator.clean_id(id_), Validator.clean_gender(gender), Validator.clean_age(age), Validator.clean_sale(sales), Validator.clean_bmi(bmi), Validator.clean_income(income))

        self._good_data.update({p.get_id(): p})

    def set_newvalue(self, correct_input, value):
        return input("correct format is: " + correct_input + "\nSet a new " + value + ":\n")

    def export_gooddata(self):
        return self._good_data


