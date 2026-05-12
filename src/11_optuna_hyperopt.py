from functools import partial

import numpy as np
from optuna import create_study, Trial
from scipy.optimize import rosen
from sklearn.datasets import make_classification

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.metrics import (
    roc_auc_score, accuracy_score, precision_score, recall_score, f1_score,
    make_scorer)


def objective(trial: Trial) -> float:
    x1 = trial.suggest_float("x1", -20, 20)
    x2 = trial.suggest_float("x2", -20, 20)
    return rosen([x1, x2])


def run_rosen_optimization() -> None:
    study = create_study(direction="minimize")
    study.optimize(func=objective, n_trials=200)
    print(f"{study.best_params=}")


def hyperopt_objective(
        trial: Trial,
        X,
        y,
        folds_num
):

    model = DecisionTreeClassifier(
        criterion=trial.suggest_categorical(
            "criterion", choices=["gini", "entropy", "log_loss"]),
        max_depth=trial.suggest_int("max_depth", 1, 50),
        random_state=123,
        max_features=trial.suggest_int("max_features", 1, 10)
    )

    res = cross_validate(
        estimator=model,
        X=X,
        y=y,
        cv=KFold(n_splits=folds_num),
        scoring=make_scorer(roc_auc_score)
    )

    return np.mean(res["test_score"])


def run_hyperopt_example():

    X, y = make_classification(
        n_samples=1_250,
        n_classes=2,
        n_features=10,
        n_informative=2,
        n_redundant=2,
        return_X_y=True,
        random_state=123
    )

    X_train, X_test, y_train, y_test = (
        train_test_split(X, y, test_size=0.2, random_state=123))

    study = create_study(direction="maximize")
    objective_function = partial(
        hyperopt_objective,
        X=X_train,
        y=y_train,
        folds_num=10
    )

    study.optimize(objective_function, n_trials=50)
    best_params = study.best_params

    champion_model = DecisionTreeClassifier(**best_params)
    champion_model.fit(X=X_train, y=y_train)

    y_test_hat_class = champion_model.predict(X_test)
    y_test_hat_proba = champion_model.predict_proba(X_test)

    accuracy_ = accuracy_score(y_test, y_test_hat_class)
    f1_score_ = f1_score(y_test, y_test_hat_class)
    precision_ = precision_score(y_test, y_test_hat_class)
    recall_ = recall_score(y_test, y_test_hat_class)
    roc_auc_ = roc_auc_score(y_test, y_test_hat_proba[:, 1])

    print(f"{accuracy_=}")
    print(f"{f1_score_=}")
    print(f"{precision_=}")
    print(f"{recall_=}")
    print(f"{roc_auc_=}")



if __name__ == "__main__":
    # run_rosen_optimization()
    run_hyperopt_example()
