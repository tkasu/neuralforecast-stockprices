# Learning neuralforecaset with stock price data

## Installation

`poetry install`

## Usage

### Download dataset

1. Create and configure Kaggle API access from: https://www.kaggle.com/settings
1. Download the data: `poetry run kaggle datasets download -p ./data/ nelgiriyewithana/world-stock-prices-daily-updating`
1. Unzip and convert the data to parquet: `poetry run python -m neuralforecast_stockprices.zip_to_parquet`

### Run code examples

1. `poetry run jupyter notebook`
1. Open browser in a given url
1. Select example notebook from `notebooks/`

### Format files and notebooks

`poetry run black .`
