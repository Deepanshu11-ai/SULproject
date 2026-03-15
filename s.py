import pandas as pd
import numpy as np
import os


# --------------------------------
# Convert Volume Values
# --------------------------------
def convert_volume(x):

    if pd.isna(x):
        return np.nan

    x = str(x).replace(",", "").strip()

    if "M" in x:
        return float(x.replace("M", "")) * 1_000_000

    elif "K" in x:
        return float(x.replace("K", "")) * 1_000

    elif "B" in x:
        return float(x.replace("B", "")) * 1_000_000_000

    else:
        return float(x)


# --------------------------------
# Build Indicator Dataset
# --------------------------------
def build_indicator_dataset(df):

    df = df.sort_values("date").reset_index(drop=True)

    # Returns
    df["return"] = df["close"].pct_change()

    # Volume change
    df["volume_change"] = df["volume"].pct_change()

    # Volatility
    df["volatility"] = df["return"].rolling(10).std()

    # Moving averages
    df["sma10"] = df["close"].rolling(10).mean()
    df["sma50"] = df["close"].rolling(50).mean()

    df["sma_ratio"] = df["sma10"] / df["sma50"]

    # MACD
    ema12 = df["close"].ewm(span=12, adjust=False).mean()
    ema26 = df["close"].ewm(span=26, adjust=False).mean()

    df["macd"] = ema12 - ema26

    # RSI
    delta = df["close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    df["rsi"] = 100 - (100 / (1 + rs))

    # Target (next-day return)
    df["target"] = df["close"].shift(-1) / df["close"] - 1

    return df


# --------------------------------
# Main Processing Function
# --------------------------------
def process_file(input_file, output_file):

    print("Loading file:", input_file)

    df = pd.read_csv(input_file)

    print("Rows loaded:", len(df))

    # Rename columns
    df = df.rename(columns={
        "Price": "close",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Vol.": "volume",
        "Change %": "change_percent"
    })

    # Convert date
    df["date"] = pd.to_datetime(df["Date"], format="mixed")
    df = df.drop(columns=["Date"])

    # Convert price columns to numeric
    price_cols = ["close", "open", "high", "low"]

    for col in price_cols:
        df[col] = df[col].astype(str).str.replace(",", "").astype(float)

    # Convert volume column
    df["volume"] = df["volume"].apply(convert_volume)

    # Convert change percent
    df["change_percent"] = df["change_percent"].str.replace("%", "").astype(float)

    # Build indicators
    df = build_indicator_dataset(df)

    # Fill early indicator NaNs
    df = df.bfill()

    # Remove rows without target
    df = df.dropna(subset=["target"])

    # Select only ML features
    indicator_df = df[[
        "rsi",
        "macd",
        "sma_ratio",
        "volume_change",
        "volatility",
        "target"
    ]]

    print("Final dataset rows:", len(indicator_df))

    # Ensure output folder exists
    folder = os.path.dirname(output_file)

    if folder != "":
        os.makedirs(folder, exist_ok=True)

    print("Saving file to:", output_file)

    indicator_df.to_csv(output_file, index=False)

    print("Dataset saved successfully")


# --------------------------------
# Run Script
# --------------------------------
if __name__ == "__main__":

    input_file = "/Users/deepanshus/StockMarketPredictor/Project/data/raw/IT/LTIM Historical Data (1).csv"

    output_file = "/Users/deepanshus/StockMarketPredictor/Project/data/Cleaned/IT/LTIM_indicator_dataset.csv"

    process_file(input_file, output_file)