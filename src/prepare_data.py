import pandas as pd
from pathlib import Path

# Read the data
def process_data(input_dir: str, output_file:str) -> Path:

    df = pd.read_parquet(input_dir)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(df["text"].tolist()))

    return Path(output_file)
