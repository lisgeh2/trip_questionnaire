import pandas as pd
from config import WEIGHTING
import HandleMeta
from helpers import clean_value_labels


class ValueCalcHouse:
    def __init__(self, df, col, value_labels=None, meta=None, weighting=WEIGHTING):
        self.df = df
        self.col = col
        if value_labels is None:
            value_labels = HandleMeta.get_value_labels(meta, col) or {}
            value_labels = clean_value_labels(value_labels)
        self.value_labels = value_labels
        self.weighting = weighting
        
    def give_codes(self):
            if self.value_labels != {}:
                return list(self.value_labels.keys())
            werte = self.df[self.col]
            gueltig = werte[werte.notna() & (werte < 99999990) & werte.ne(97)]   # NaN und Sentinels raus
            return sorted(gueltig.unique())

    def give_counts(self, dont_round = False):
        counts = []
        for k in self.give_codes():
            zeilen_mit_k = self.df[self.df[self.col] == k]
            if dont_round:
                counts.append((zeilen_mit_k[self.weighting].sum()))
            else:
                counts.append(int(round((zeilen_mit_k[self.weighting].sum()), 0)))
        return counts

    def give_percentages(self):
        counts = self.give_counts(dont_round = True)
        total = sum(counts)
        if total == 0:
            return [0.0 for _ in counts]
        return [round(count / total * 100, 1) for count in counts]

    def give_total_n(self):
        counts = self.give_counts()
        total = sum(counts)
        return int(round(total, 0))

    def give_n(self):
            n_list = []
            for k in self.give_codes():
                zeilen_mit_k = self.df[self.df[self.col] == k]
                n_list.append(int(len(zeilen_mit_k)))
            return n_list

    def give_mean(self):
        """Gewichteter Mittelwert über alle gültigen Codes."""
        zeilen = self.df[self.df[self.col].isin(self.give_codes())]
        gewichte = zeilen[self.weighting]
        if gewichte.sum() == 0:
            return None
        return (zeilen[self.col] * gewichte).sum() / gewichte.sum()