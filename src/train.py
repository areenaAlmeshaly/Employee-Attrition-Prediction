
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def train_model(df, target):
    X = df.drop(columns=target)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.7,random_state=42,stratify=y)

    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train,test_size=0.2,random_state=42,stratify=y_train)

    model = Pipeline([("scaler", StandardScaler()),("logistic", LogisticRegression(max_iter=5000,class_weight="balanced"))])

    model.fit(X_train, y_train)
    probs = model.predict_proba(X_test)[:, 1]

    return model,y_test, probs
