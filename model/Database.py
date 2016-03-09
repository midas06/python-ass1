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