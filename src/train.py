
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_model(df, target, threshold=0.3):
    X = df.drop(columns=target)
    y = df[target]


    X_train, X_test, y_train, y_test = train_test_split( X, y, train_size=0.7, random_state=42, stratify=y)
    model = Pipeline([("scaler", StandardScaler()),("logistic", LogisticRegression(max_iter=5000,class_weight="balanced"))])

    model.fit(X_train, y_train)

    probs = model.predict_proba(X_test)[:, 1]

    return model, X_test, y_test, probs