from moddata import load_data
import numpy as np
import pandas as pd

from tsfresh.feature_extraction import extract_features, MinimalFCParameters
from tsfresh.utilities.dataframe_functions import impute
from tsfresh.feature_extraction import EfficientFCParameters
from tsfresh import select_features


def make_data() -> tuple[pd.DataFrame, pd.Series]:

    data = load_data("sunspots")
    data["day"] = data["day"].astype("datetime64[ns]")
    data = data.set_index("day")
    data["y"] = data["daily_sunspots_number"].shift(-1)

    data = data["2011-01-01":"2015-12-31"]
    data = data.reset_index(drop=False)
    X = data[["day", "daily_sunspots_number"]]
    y = pd.Series(data=data["y"].values, index=data.index)
    return X, y


def manual_roll_time_series(
        data: pd.DataFrame,
        window_size: int,
) -> pd.DataFrame:

    chunks: list[pd.DataFrame] = []

    for j in range(window_size-1, data.shape[0], 1):
        chunk = data.iloc[j-(window_size-1):j+1, :]
        chunk["window_id"] = j
        chunk["window_time"] = np.arange(window_size)
        chunks.append(chunk)

    return pd.concat(chunks, axis=0)


if __name__ == "__main__":

    # 1. load the data
    X, y = make_data()

    # 2. transform data to rolling format before running auto features generation
    rolling_sunspots = manual_roll_time_series(data=X, window_size=60)

    # 3. extract features
    features = extract_features(
        rolling_sunspots.drop(columns=["day"]),
        column_id="window_id",
        column_sort="window_time",
        default_fc_parameters=EfficientFCParameters(),
        # n_jobs=1,
        disable_progressbar=False,
    )
    features = impute(features)

    filtered_features = select_features(
        X=features,
        y=y[59:],
    )



    print("halt")
