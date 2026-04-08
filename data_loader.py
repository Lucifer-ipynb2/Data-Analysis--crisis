import pandas as pd

def load_data():

    events = pd.read_csv("data/geopolitical_events.csv")
    exports = pd.read_csv("data/iran_oil_exports.csv")
    prices = pd.read_csv("data/oil_prices_daily.csv")
    risk = pd.read_csv("data/risk_indicators.csv")
    sanctions = pd.read_csv("data/sanctions_timeline.csv")

    prices['date'] = pd.to_datetime(prices['date'])
    risk['date'] = pd.to_datetime(risk['date'])
    events['date'] = pd.to_datetime(events['date'])
    sanctions['date'] = pd.to_datetime(sanctions['date'])

    return events, exports, prices, risk, sanctions
