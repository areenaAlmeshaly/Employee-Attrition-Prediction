
import mlflow
import mlflow.sklearn

from src.load_data import load_data
from src.validate_data import validate
#from src.features import binary_series
from src.features import non_binary_series
from src.feature_engineering import create_features
from src.train import train_model
from src.evaluate_model import evaluate_model


def main():

    df = load_data("data/IBM Data.csv")
    validate(df)
    # df = binary_series(df)
    df = non_binary_series(df)
    df = create_features(df)

    
    mlflow.set_experiment("Employee Attrition")

    with mlflow.start_run():

        model, y_test, probs = train_model(df, target="Attrition")
        metrics = evaluate_model(y_test,probs,threshold=0.35)

        mlflow.log_params({
            "model": "LogisticRegression",
            "max_iter": 5000,
            "class_weight": "balanced",
            "threshold": 0.35})

        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, "model")


if __name__ == "__main__":
    main()
