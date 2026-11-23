
import pandas as pd

"""def binary_series(df):
     df = df.copy()

     categorical_cols = df.select_dtypes(include=["object", "category"]).columns
     
     for col in categorical_cols:
        values = df[col].dropna().unique()

        if len(values) == 2:

            sorted_values = sorted(values)
            df[col] = df[col].map({sorted_values[0]: 0,sorted_values[1]: 1})
            
     return df"""

"""def non_binary_series(df):
    df = df.copy()

    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    for col in categorical_cols:

        if df[col].nunique() == 2:
            df[col] = binary_series(df[col])

        elif df[col].nunique() > 2:
            encoded = pd.get_dummies(df[col], prefix=col,dtype=int)

            df=pd.concat([df, encoded], axis=1)
            df.drop(columns=[col], inplace=True)

    return df"""

def non_binary_series(df):
    df = df.copy()

    df["Attrition"] = df["Attrition"].map({
        "No": 0,
        "Yes": 1
    })

    categorical_cols = [
        col for col in df.select_dtypes(include=["object", "category"]).columns
        if col != "Attrition"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        dtype=int
    )

    return df