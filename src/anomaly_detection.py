from sklearn.ensemble import IsolationForest


def detect_rule_based_anomalies(df):

    high_threshold = (
        df['Global_active_power'].mean()
        + 2 * df['Global_active_power'].std()
    )

    df['Rule_Based_Anomaly'] = (
        df['Global_active_power']
        > high_threshold
    )

    return df


def detect_isolation_forest_anomalies(df):

    ml_features = [
        'Global_active_power',
        'Rolling_Mean_24',
        'Rolling_STD_24',
        'Deviation',
        'Hour',
        'Weekday'
    ]

    X = df[ml_features]

    iso_forest = IsolationForest(
        contamination=0.01,
        random_state=42
    )

    iso_forest.fit(X)

    df['IF_Anomaly'] = (
        iso_forest.predict(X)
    )

    return df


def create_hybrid_anomaly(df):

    df['Hybrid_Anomaly'] = (
        (df['Rule_Based_Anomaly'] == True)
        |
        (df['IF_Anomaly'] == -1)
    )

    return df