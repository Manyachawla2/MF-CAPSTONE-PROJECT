import pandas as pd
import os

path = "data/raw"

for file in os.listdir(path):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(path, file))

        print("\nDataset:", file)
        print("Shape:", df.shape)
        print("Data Types:")
        print(df.dtypes)
        print("Head:")
        print(df.head())