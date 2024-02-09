from zipfile import ZipFile

import polars as pl

ZIPFILE_PATH = "./data/world-stock-prices-daily-updating.zip"
CSVFILE_NAME = "World-Stock-Prices-Dataset.csv"


def main():
    with ZipFile(ZIPFILE_PATH) as zipfile:
        with zipfile.open(CSVFILE_NAME) as file:
            df = pl.read_csv(file, try_parse_dates=True)

    df.write_parquet(
        "./data/stock_prices",
        use_pyarrow=True,
        pyarrow_options={"partition_cols": ["Ticker"]},
    )


if __name__ == "__main__":
    main()
