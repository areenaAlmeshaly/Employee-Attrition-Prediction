import numpy as np

def create_features(df):
    df_fe = df.copy()

    df_fe["LowWorkExperience"] = np.where(df_fe["TotalWorkingYears"] == 0, 1, 0)

    df_fe["lowIncome"] = np.where(df_fe["MonthlyIncome"] <= 3202, 1, 0)

    df_fe["RoleStagnation"] = (df_fe["YearsInCurrentRole"] / (df_fe["YearsAtCompany"] + 1))

    df_fe["PromotionRate"] = (df_fe["YearsAtCompany"] /(df_fe["YearsSinceLastPromotion"] + 1))

    df_fe = df_fe.drop(columns=["EmployeeCount","StandardHours","EmployeeNumber","Over18"],errors="ignore")

    return df_fe