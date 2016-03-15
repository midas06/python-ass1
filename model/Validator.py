from model.Person import *
import re



class Validator:

    def __init__(self):
        self._good_data = {}
        self._bad_data = []
        self._raw_data = None

    def set_raw_data(self, new_data):
        self._raw_data = new_data

    def to_obj(self, a_string):
        str_list = a_string.split(",")
        new_person = Person(str_list[0], str_list[1], str_list[2], str_list[3], str_list[4], str_list[5])
        return new_person

    def parse_data(self):
        for i in self._raw_data:
            if self.isvalid(i):
                p = self.to_obj(i)
                self._good_data.update({p.get_id(): p})
            else:
                self._bad_data.append(i)

    def export_gooddata(self):
        return self._good_data

    def export_baddata(self):
        return self._bad_data

    def has_baddata(self):
        return len(self._bad_data) > 0

    ###
        # clean methods
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

        return a_gender

    @staticmethod
    def clean_age(an_age):
        if len(an_age) == 1:
            an_age = "0" + an_age
        return an_age

    @staticmethod
    def clean_sale(a_sale):
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
    def hasvalid_id(an_id):
        id = Validator.clean_id(an_id)
        pattern = re.compile('^([A-Z]{1}[0-9]{3})+$')

        if pattern.match(id) is None:
            return False

        return True

    @staticmethod
    def hasvalid_gender(a_gender):
        g = Validator.clean_gender(a_gender)
        if g == 'M' or g == 'F':
            return True

        return False

    @staticmethod
    def hasvalid_age(an_age):
        a = Validator.clean_age(an_age)
        pattern = re.compile('^([0-9]{2})+$')

        if pattern.match(a) is None:
            return False

        return True

    @staticmethod
    def hasvalid_sales(a_sale):
        s = Validator.clean_sale(a_sale)
        pattern = re.compile('^([0-9]{3})+$')

        if pattern.match(s) is None:
            return False

        return True

    @staticmethod
    def hasvalid_bmi(an_index):
        i = Validator.clean_bmi(an_index)
        valid = ["Normal", "Overweight", "Obesity", "Underweight"]

        if i in valid:
            return True

        return False

    @staticmethod
    def hasvalid_income(an_income):
        i = Validator.clean_income(an_income)
        pattern = re.compile('^([0-9]{2,3})+$')

        if pattern.match(i) is None:
            return False

        return True

    def isvalid(self, a_string):
        str_list = a_string.split(",")
        if self.hasvalid_id(str_list[0]) and self.hasvalid_gender(str_list[1]) and self.hasvalid_age(str_list[2]) and self.hasvalid_sales(str_list[3]) and self.hasvalid_bmi(str_list[4]) and self.hasvalid_income(str_list[5]):
            return True

        return False


    #jess
    def print_bad_data(self):
        for i in self._bad_data:
            print(i)

    def get_all_bad_data(self):
        result = ""
        for i in self._bad_data:
            result += i + "\n"
        return result


    def empty_bad_data(self): #empty bad data every time a file with bad data is loaded
        self._bad_data = []
        #print("CURRENT BAD:" + str(len(self._bad_data)))

    def get_bad_data_len(self):
        return len(self._bad_data)

    def empty_raw_data(self): #well it fixed the last issue :D
        self._raw_data = None

    def test(self):
        # for i in self._raw_data:
        #     if self.isvalid(i):
        #         p = self.to_obj(i)
        #         self._good_data.update({p.get_id(): p})
        #     else:
        #         self._bad_data.append(i)


            #j = i.split(",")
            # if self.hasvalid_id(j):
            #     print("matches")
            # else:
            #     print("nope")

            # if (self.hasvalid_gender(j)):
            #     print("yep")
            # else:
            #     print("NOPE")

            # if (self.hasvalid_sales(j)):
            #     print("yep")
            # else:
            #     print("NOPE")
            #
            # if (self.hasvalid_age(j)):
            #     print("yep")
            # else:
            #     print("NOPE")
            #
            # if (self.hasvalid_bmi(j)):
            #     print("yep")
            # else:
            #     print("NOPE")
            #
            # if(self.hasvalid_income(j)):
            #     print("yep")
            # else:
            #     print("NOPE")

        # for value in self._good_data:
        #     print(value)
        #
        self.parse_data()
        print(self._good_data.items())
        for i in self._bad_data:
            print("BAD " + i)

        # print(self.clean_id("a12314234"))
        # # print(self.clean_gender("m"))
        # # s = self.clean_age("2")
        # # print(self.hasvalid_age(s))
        # # sale = self.clean_sales("d")
        # # print(self.hasvalid_sales(sale))

"""
v = Validator()

print(v.clean_gender("Female"))
"""