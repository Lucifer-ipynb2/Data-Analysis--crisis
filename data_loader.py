import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_data():

    events = pd.read_csv(os.path.join(BASE_DIR, "geopolitical_events.csv"))
    exports = pd.read_csv(os.path.join(BASE_DIR, "iran_oil_exports.csv"))
    prices = pd.read_csv(os.path.join(BASE_DIR, "oil_prices_daily.csv"))
    risk = pd.read_csv(os.path.join(BASE_DIR, "risk_indicators.csv"))
    sanctions = pd.read_csv(os.path.join(BASE_DIR, "sanctions_timeline.csv"))

    return events, exports, prices, risk, sanctions
