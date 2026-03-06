import numpy as np
import pandas as pd

from statsmodels.tsa.arima_process import arma_generate_sample
from statsmodels.tsa.arima.model import ARIMA


def generate_arma_sample(
        ar_lags_coefs: np.ndarray,
        ma_lags_coefs: np.ndarray,
        n_obs: int,
        sigma: float
):
    values = arma_generate_sample(
        ar=np.r_[1, ar_lags_coefs.reshape(1, -1)],
        ma=np.r_[1, ma_lags_coefs.reshape(1, -1)],
        nsample=n_obs,
        scale=sigma,
    )
    return pd.DataFrame(data={"y": values.flatten()})


if __name__ == "__main__":
    pass
