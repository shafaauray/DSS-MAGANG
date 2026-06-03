import pandas as pd

def saw(df, bobot):

    data = df.copy()

    benefit = ["C1","C3","C4","C5","C6"]

    cost = ["C2"]

    for col in benefit:
        data[col] = data[col]/data[col].max()

    for col in cost:
        data[col] = data[col].min()/data[col]

    data["Skor"] = (
        data["C1"]*bobot[0] +
        data["C2"]*bobot[1] +
        data["C3"]*bobot[2] +
        data["C4"]*bobot[3] +
        data["C5"]*bobot[4] +
        data["C6"]*bobot[5]
    )

    return data.sort_values(
        by="Skor",
        ascending=False
    )