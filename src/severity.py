def classify_anomaly_severity(df):

    df['Anomaly_Score'] = (
        abs(df['Deviation'])
    )

    low_threshold = (
        df['Anomaly_Score']
        .quantile(0.90)
    )

    medium_threshold = (
        df['Anomaly_Score']
        .quantile(0.97)
    )

    def classify(score):

        if score >= medium_threshold:
            return 'High'

        elif score >= low_threshold:
            return 'Medium'

        else:
            return 'Low'

    df['Severity'] = (
        df['Anomaly_Score']
        .apply(classify)
    )

    return df