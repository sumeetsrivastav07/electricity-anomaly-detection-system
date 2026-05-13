def generate_ai_insights(df):

    insights = []

    # Peak hour
    peak_hour = (
        df.groupby('Hour')
        ['Global_active_power']
        .mean()
        .idxmax()
    )

    insights.append(
        f"Peak electricity usage occurs around hour {peak_hour}."
    )

    # High severity count
    high_count = len(
        df[df['Severity'] == 'High']
    )

    insights.append(
        f"The system detected {high_count} high-severity anomalies."
    )

    # Hybrid anomalies
    total_anomalies = (
        df['Hybrid_Anomaly']
        .sum()
    )

    insights.append(
        f"A total of {total_anomalies} abnormal electricity events were identified."
    )

    # Usage recommendation
    insights.append(
        "Reducing appliance usage during peak hours may improve energy efficiency."
    )

    return insights