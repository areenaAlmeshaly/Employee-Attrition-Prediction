
import pandas as pd

def binary_series(series):
    values = series.dropna().unique()

    if len(values) == 2:
        sorted_values=sorted(values)
        return series.map({
            sorted_values[0]: 0,
            sorted_values[1]: 1})

    return series


def non_binary_series(df):
    df = df.copy()

    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in categorical_cols:

        if df[col].nunique() == 2:
            df[col] = binary_series(df[col])

        elif df[col].nunique() > 2:
            encoded = pd.get_dummies(df[col], prefix=col,dtype=int)

            df=pd.concat([df, encoded], axis=1)
            df.drop(columns=[col], inplace=True)

    return df
