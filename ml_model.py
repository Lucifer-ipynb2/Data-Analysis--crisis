from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(df):

    features = [
        "opec_production_mbd",
        "us_rig_count",
        "brent_risk_premium_usd",
        "energy_security_index"
    ]

    df = df.dropna()

    X = df[features]
    y = df["brent_usd"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()

    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)

    return model, score
