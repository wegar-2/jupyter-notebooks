# jupyter-notebooks

Various jupyter notebooks.

## A. Setup

Install dependencies from *uv.lock*:
```commandline
uv sync
```

Additionally, install data package [*moddata*](https://github.com/wegar-2/moddata.git):
```commandline
uv pip install git+https://github.com/wegar-2/moddata.git
```


## B. Contents
1. [EURPLN FX rate overview](./notebooks/01_eurpln_overview.ipynb) - quick look 
at the exchange rate's log-returns, histograms, KDE, ACF and PACF
2. [Basic stationarity tests](./notebooks/02_stationarity_testing_using_arch.ipynb) - review of 
most common stationarity tests (ADF, KPSS, PP) in *arch*
3. [ARMA models - choosing lags based on ACF and PACF](./notebooks) - tbd
4. [Fractional differencing with *tsfracdiff*](./notebooks) - tbd

