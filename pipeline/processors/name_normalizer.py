import pandas as pd


def normalize_name(name):

    if pd.isna(name):
        return ""

    words = str(name).split()

    return " ".join(word.capitalize() for word in words)