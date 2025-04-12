import pandas as pd
from glob import glob

def preprocess_data(file_path):
    df = pd.read_excel(file_path, skiprows=1)
    
    # drop the unnamed column
    df = df.drop(df.columns[0], axis=1)

    # normalize column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    return df

if __name__ == "__main__":
    file_paths = glob("data/*.xls")
    latam_data = preprocess_data(file_paths[0])
    
    latam_data.to_csv("data/latam_data.csv", index=False)