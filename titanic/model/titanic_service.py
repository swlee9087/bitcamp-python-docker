import pandas as pd

# 2
from python.titanic.model.dataset import Dataset
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier


class TitanicService(object):
    dataset = Dataset()  # constructorrrrr

    def new_model(self, payload: str) -> object:
        """this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)"""
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)  # del "Survived' col from dataset

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:  # data features to omit from set because they are irrelevant as death cause
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

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

