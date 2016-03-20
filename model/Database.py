import pickle
import os
import sys


class Database(object):

    def __init__(self):
        self._database = {}
        self.serialize_location = ""

    def add_people(self, new_data):
        self._database.update(new_data)

    def set_directory(self, new_location):
        self.serialize_location = new_location

    def get_directory(self):
        print (self.serialize_location)
        return str(self.serialize_location)

    def serialize(self, option):
        if option == 0:
            with open('database.pickle', 'wb') as f:
                pickle.dump(self._database, f)
            f.close()
        elif option == 1:
            with os.fdopen(os.open(self.serialize_location + "\database.pickle", os.O_WRONLY | os.O_CREAT, 0o777), 'wb') as f:
                pickle.dump(self._database, f)

    def deserialize(self,option):
        default_file = sys.argv[1]
        print(default_file)
        if option == 0:
            with open(default_file, 'rb') as f:
                self._database = pickle.load(f)
        elif option == 1:
            with open(self.serialize_location + "\\" + default_file, 'rb') as f:
                self._database = pickle.load(f)

    def get_person_by_id(self, an_id):
        for key, value in self._database.items():
            if key == an_id:
                return value

    def get_test_data(self):
        result = []
        for i in self._database:
            c = self._database.get(i)
            result.append(str(i) + "," + str(c.get_gender()) + "," + str(c.get_age()) + "," + str(c.get_sales()) + "," + str(c.get_bmi()) + "," + str(c.get_income()))
        return result

    def print_all(self):
        for i in self._database:
            c = self._database.get(i)
            print(i + "\t" + c.get_gender() + "\t" + c.get_age() + "\t" + c.get_sales() + "\t" + c.get_bmi() + "\t\t" + c.get_income())

    def get_length(self):
        return len(self._database)

    def empty_database(self):
        self._database = {}

    def get_male_bmi(self):
        male = [0,0,0,0]
        for key, value in self._database.items():
            bmi = value.get_bmi()
            gender = value.get_gender()
            if gender == "M":
                if bmi == "Normal":
                    male[0] += 1
                elif bmi == "Overweight":
                    male[1] +=1
                elif bmi == "Obesity":
                    male[2] +=1
                elif bmi == "Underweight":
                    male[3] +=1
        return male

    def get_female_bmi(self):
        female = [0,0,0,0]
        for key, value in self._database.items():
            bmi = value.get_bmi()
            gender = value.get_gender()
            if gender == "F":
                if bmi == "Normal":
                    female[0] += 1
                elif bmi == "Overweight":
                    female[1] +=1
                elif bmi == "Obesity":
                    female[2] +=1
                elif bmi == "Underweight":
                    female[3] +=1
        return female

    def get_bmi_distribution(self):
        norm, ov, ob, uw = 0, 0, 0, 0

        for key, value in self._database.items():
            b = value.get_bmi()
            if b == "Overweight":
                ov += 1
            elif b == "Underweight":
                uw += 1
            elif b == "Normal":
                norm += 1
            elif b == "Obesity":
                ob += 1

        dist = {"normal" : norm, "overweight" : ov, "obese": ob, "underweight": uw}
        return dist

    def get_gender_distribution(self):
        m, f = 0, 0

        for k, v in self._database.items():
            g = v.get_gender()
            if g == 'M':
                m += 1
            else:
                f += 1

        dist = {"males": m, "females": f}
        return dist

    def get_sales_ordered(self):
        sales_list = []

        for k, v in self._database.items():
            print(v.get_sales())
            sales_list.append(int(v.get_sales()))

        return sorted(sales_list)


