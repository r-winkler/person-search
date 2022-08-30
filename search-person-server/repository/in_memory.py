import pandas as pd


def dataset():
    df = pd.read_csv('datasets/names_of_switzerland.csv')
    df.columns = ['name', 'firstname']
    return df


class InMemoryRepository(object):
    def __init__(self):
        self.db = dataset()

    def find_all(self):
        return self.db
