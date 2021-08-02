import pandas as pd

# 2
from python.titanic.model.dataset import Dataset


class TitanicService(object):
    dataset = Dataset()  # constructorrrrr

    def new_model(self, payload: str) -> object:
        """this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)"""
        return pd.read_csv(f"/data/{payload}.csv")

    def create_train(self):
        return None

    def count_survived_dead(self):
        return []

    def create_label(self):
        return None

    def drop_feature(self, *feature):
        return None

    def embarked_nominal(self):  # QSC
        return None

    def fare_ordinal(self):  # paid or not
        return None

    def title_nominal(self):  # mr mrs miss master ms
        return None

    def gender_nominal(self):  # mf
        return None

    def age_ordinal(self):  #
        return None

    def create_k_fold(self):  #
        return None

    def accuracy_by_classifier(self):  #
        return ""

