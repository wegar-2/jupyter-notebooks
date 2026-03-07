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
3. [ARMA models - choosing lags based on ACF and PACF](./notebooks) - 
demonstration of using ACF and PACF plots to recover parameters of the 
simulated ARMA process - TBD
4. [Fractional differencing with *tsfracdiff*](./notebooks/04_fractional_differencing_with_ts_fracdiff.ipynb) - using
package *tsfracdiff* package to search for least fractional order of integration
that makes the given package stationary according to a specified test
5. [Good-looking stock price plot](./notebooks/05_good-looking_stock_price_chart.ipynb) - 
templates for making stock price plots that look more pleasant for the eye
6. [Splitting data into train, validation and test datasets](./notebooks) - tbd
7. [Drawing periodogram of a discrete-time process](./notebooks) - tbd
8. [Testing for cointegration (non-fractional)](./notebooks) - tbd
9. [Gold prices 1960-1971](./notebooks/09_gold_price_1960-1971.ipynb) - plot
of monthly average gold prices with select important events from 
political and financial history marked
