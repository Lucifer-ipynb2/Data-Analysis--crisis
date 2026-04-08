import pandas as pd

def merge_datasets(prices, risk):

    df = prices.merge(risk, on="date", how="left")

    return df


def compute_correlations(df):

    corr = df.corr(numeric_only=True)

    return corr


def yearly_oil_trend(prices):

    prices['year'] = prices['date'].dt.year

    trend = prices.groupby("year")['brent_usd'].mean().reset_index()

    return trend
