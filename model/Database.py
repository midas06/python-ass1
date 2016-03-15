import pickle


class Database(object):

    def __init__(self):
        self._database = {}

    def add_people(self, new_data):
        self._database.update(new_data)

    def serialize(self):
        with open('database.pickle', 'wb') as f:
            pickle.dump(self._database, f)
        f.close()

    def deserialize(self):
        with open('database.pickle', 'rb') as f:
            # self._database = pickle.load(f)
            db = pickle.load(f)
            f.close()
        for i in db:
            print(i)

    def print_g(self):
        for i in self._database:
            c = self._database.get(i)
            print(i, c.get_income())

    #jess
    def print_all(self):
        #result = ""
        for i in self._database:
            c = self._database.get(i)
            #result += str(i) + "\t" + str(c.get_gender()) + "\t" + str(c.get_age()) + "\t" + str(c.get_sales()) + "\t" + str(c.get_bmi()) + "\t\t" + str(c.get_income())
            print(i + "\t" + c.get_gender() + "\t" + c.get_age() + "\t" + c.get_sales() + "\t" + c.get_bmi() + "\t\t" + c.get_income())
            #return result

    def getLength(self):
        return len(self._database)

    def empty_database(self):
        self._database.clear()
        #print(len(self._database))


    def get_age_array(self):
        result = []
        for i in self._database:
            c = self._database.get(i)
            #result += str(i) + "\t" + str(c.get_gender()) + "\t" + str(c.get_age()) + "\t" + str(c.get_sales()) + "\t" + str(c.get_bmi()) + "\t\t" + str(c.get_income())
            #print(c.get_age())
            #return result
            result.append(c.get_age())
        return result

    def get_sales_array(self):
        result = []
        for i in self._database:
            c = self._database.get(i)
            result.append(c.get_sales())
        return result


