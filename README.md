# jupyter-notebooks

Storage of various jupyter notebooks.

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

