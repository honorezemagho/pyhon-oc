#! /usr/bin/env python3
# coding: utf-8

import os
import logging as lg

import pandas as pd
import numpy as np


lg.basicConfig(level=lg.DEBUG)


import os
import pandas as pd


class SetOfParliamentMembers:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "setOfParliamentMember: {} members".format(len(self.dataframe))

    def data_from_csv(self, csv_file):
        self.dataframe = pd.read_csv(csv_file, sep=";",  engine = 'python')

    def data_from_dataframe(self, dataframe):
        self.dataframe = dataframe

    def display_chart(self):
        # à venir, patience !
        pass

    def split_by_political_party(self):
        result = {}
        data = self.dataframe

        all_parties = data["parti_ratt_financier"].dropna().unique()

        for party in all_parties:
            data_subset = data[data.parti_ratt_financier == party]
            subset = SetOfParliamentMembers('MPs from party "{}"'.format(party))
            subset.data_from_dataframe(data_subset)
            result[party] = subset

        return result


def launch_analysis(data_file, by_party=False, info=False):
    sopm = SetOfParliamentMembers("All MPs")
    sopm.data_from_csv(os.path.join("data", data_file))
    sopm.display_chart()

    if by_party:
        for party, s in sopm.split_by_political_party().items():
            s.display_chart()
    if info:
        print(sopm)


if __name__ == "__main__":
    launch_analysis("current_mps.csv")
