from moddata import load_data
from timeseriescv.cross_validation import CombPurgedKFoldCV
from lightgbm import LGBMClassifier



if __name__ == "__main__":
    banks = load_data("pl_banking_stocks")
