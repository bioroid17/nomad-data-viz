import pandas as pd

conditions = ["confirmed", "deaths", "recovered"]

daily_df = pd.read_csv("data/daily_report.csv")
totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)
totals_df = totals_df.rename(columns={"index": "condition"})

country_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
country_df = (
    country_df.groupby("Country_Region")
    .sum()
    .sort_values(by="Confirmed", ascending=False)
    .reset_index()
)

dropdown_options = country_df.sort_values("Country_Region").reset_index()
dropdown_options = dropdown_options["Country_Region"]


def make_country_df(country):

    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = df.loc[df["Country/Region"] == country]
        df = (
            df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"])
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})

        return df

    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df


def make_global_df():

    def make_df(condition):
        df = pd.read_csv(f"data/time_{condition}.csv")
        df = (
            df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
            .sum()
            .reset_index(name=condition)
        )
        df = df.rename(columns={"index": "date"})
        return df

    final_df = None
    for condition in conditions:
        condition_df = make_df(condition)
        if final_df is None:
            final_df = condition_df
        else:
            final_df = final_df.merge(condition_df)
    return final_df
