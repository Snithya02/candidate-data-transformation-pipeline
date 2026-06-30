import pandas as pd


def parse_csv(file_path):

    df = pd.read_csv(file_path)

    print(df)          # <-- Add this line
    print(df.columns)  # <-- Add this line

    candidates = []

    for _, row in df.iterrows():
        candidates.append(row.to_dict())

    return candidates