import pandas as pd


def normalize_email(email):

    if pd.isna(email):
        return ""

    return str(email).strip().lower()