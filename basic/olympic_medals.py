import pandas as pd

# #matches, gold, silver, bronze, total / summer -winter-combined total

class OlympicMedals(object):
    pass

    def read_wiki(self) -> object:
        df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
        print(df)
        return df

    """def show_summer(self, df):
        summer = df.iloc[:,:5]
        summer.columns =['# Matches', ]"""
